import binascii
import os
import re
import sys
import threading

from PyQt6.QtCore import QFile, QIODeviceBase, pyqtSignal
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow

import main_qrc
from Ui_main import Ui_MainWindow

class MyPyQT_Form(QMainWindow, Ui_MainWindow):

    updateSignal = pyqtSignal(str)
    progressSignal = pyqtSignal(int)

    PNG_HEADER = (0x89, 0x50)
    JPG_HEADER = (0xFF, 0xD8)
    GIF_HEADER = (0x47, 0x49)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(":/icon/main.ico"))

        self.pattern = re.compile(r'\d{4}-\d{2}')
        self.progressBar.setHidden(True)

        self.pathPushButton.clicked.connect(self.pathPushButtonEvent)
        self.savePathPushButton.clicked.connect(self.savePathPushButtonEvent)
        self.decodePushButton.clicked.connect(self.decodePushButtonEvent)
        self.updateSignal.connect(self.updateUI)
        self.progressSignal.connect(self.updateProgress)

    def updateUI(self, message):
        self.logPlainTextEdit.appendPlainText(message)
    
    def updateProgress(self, value):
        self.progressBar.setValue(value)

    def wechatImgDatDecode(self, img_path, save_path, total_files):
        processed_files = 0

        for foldername, subfolders, filenames in os.walk(img_path):
            if "Image" not in subfolders:
                continue
            
            for foldername, subfolders, filenames in os.walk(os.path.join(foldername, "Image")):
                for name in subfolders:
                    if self.pattern.match(name):
                        decode_folder_path = os.path.join(foldername, name)
                        save_folder_path = os.path.join(save_path, name)
                        if not os.path.exists(save_folder_path):
                            os.mkdir(save_folder_path)

                        decode_files = os.listdir(decode_folder_path)
                        for decode_file in decode_files:
                            if decode_file.endswith('.dat'):
                                with open(os.path.join(decode_folder_path, decode_file), 'rb') as dat_file:
                                    hex_data = binascii.hexlify(dat_file.read(2)).decode('utf-8')
                                    tmp_h = int(hex_data[:2], 16)
                                    tmp_l = int(hex_data[2:4], 16)

                                    file_type = None
                                    file_decode_num = None
                                    headers = [
                                        (self.PNG_HEADER, '.png'),
                                        (self.JPG_HEADER, '.jpg'),
                                        (self.GIF_HEADER, '.gif')
                                    ]
                                    for header, ext in headers:
                                        if tmp_h ^ header[0] == tmp_l ^ header[1]:
                                            file_type = ext
                                            file_decode_num = tmp_h ^ header[0]
                                            break
                                    
                                    if file_type is None:
                                        continue
   
                                    save_file_path = os.path.join(save_folder_path, decode_file.replace(".dat", file_type))
                                    if os.path.exists(save_file_path):
                                        self.updateSignal.emit('已存在，跳过：' + save_file_path)
                                        continue
                                    else:
                                        self.updateSignal.emit(save_file_path)

                                    with open(save_file_path, 'wb') as output_file:
                                        dat_file.seek(0)
                                        file_data = dat_file.read()
                                        block_data = bytearray(file_data)
                                        for i in range(len(block_data)):
                                            block_data[i] ^= file_decode_num
                                        output_file.write(block_data)

                            processed_files += 1
                            self.progressSignal.emit(processed_files)

        self.updateSignal.emit('Done!')
        self.statusBar.showMessage('转换完成')

    def pathPushButtonEvent(self):
        _path = QFileDialog.getExistingDirectory(self, '请选择MsgAttach文件夹', './')
        self.pathLineEdit.setText(_path)

    def savePathPushButtonEvent(self):
        _path = QFileDialog.getExistingDirectory(self, '请选择要保存的路径', './')
        self.savePathLineEdit.setText(_path)

    def decodePushButtonEvent(self):
        if self.pathLineEdit.text() == '' or not os.path.exists(self.pathLineEdit.text()):
            self.updateUI(self.pathLineEdit.text() + '，转换文件路径出错，请检查!')
            return
        
        if self.savePathLineEdit.text() == '' or not os.path.exists(self.savePathLineEdit.text()):
            self.updateUI(self.savePathLineEdit.text() + '，保存文件路径出错，请检查!')
            return
        
        self.logPlainTextEdit.clear()
        self.statusBar.showMessage('转换中...')

        total_files = 0
        for foldername, subfolders, filenames in os.walk(self.pathLineEdit.text()):
            if "Image" not in subfolders:
                continue
            for foldername, subfolders, filenames in os.walk(os.path.join(foldername, "Image")):
                for name in subfolders:
                    if self.pattern.match(name):
                        decode_folder_path = os.path.join(foldername, name)
                        total_files += len([f for f in os.listdir(decode_folder_path) if f.endswith('.dat')])

        self.progressBar.setMaximum(total_files)
        self.progressBar.setHidden(False)
        self.progressBar.setValue(0)

        decode_thread = threading.Thread(target=self.wechatImgDatDecode, args=(self.pathLineEdit.text(), self.savePathLineEdit.text(), total_files))
        decode_thread.start()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    f = QFile(":/qss/main.qss")
    f.open(QIODeviceBase.OpenModeFlag.ReadOnly)
    app.setStyleSheet(str(f.readAll(), encoding="utf-8"))
    f.close()

    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec())

