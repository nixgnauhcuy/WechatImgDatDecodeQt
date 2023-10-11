import sys
import os
import binascii
import threading
import main_qrc
import re

from Ui_main import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon
from PySide6.QtCore import QFile, QIODevice

class MyPyQT_Form(QMainWindow, Ui_MainWindow):

    updateSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon(":/icon/main.ico"))

        self.png_header_h = 0x89
        self.png_header_l = 0x50
        self.jpg_header_h = 0xFF
        self.jpg_header_l = 0xD8
        self.gif_header_h = 0x47
        self.gif_header_l = 0x49

        self.oldWechatDecodeFlag = False

        self.pattern = re.compile(r'\d{4}-\d{2}')

        self.wechatVersionCheckBox.clicked.connect(self.wechatVersionCheckBoxEvent)
        self.pathPushButton.clicked.connect(self.pathPushButtonEvent)
        self.savePathPushButton.clicked.connect(self.savePathPushButtonEvent)
        self.decodePushButton.clicked.connect(self.decodePushButtonEvent)
        self.updateSignal.connect(self.updateUI)

    
    def updateUI(self, message):
        self.logPlainTextEdit.appendPlainText(message)

    def oldwechatImgDatDecode(self, img_path, save_path):
        decode_files_path = []
        files = os.listdir(img_path)
        for file in files:
            if file.endswith('.dat'):
                decode_files_path.append(img_path + '/' + file)

        for decode_file in decode_files_path:
            with open(decode_file, 'rb') as dat_file:
                hex_data = binascii.hexlify(dat_file.read(2)).decode('utf-8')
                tmp_h = int(hex_data[:2], 16)
                tmp_l = int(hex_data[2:4], 16)

                file_type = None
                file_decode_num = None
                if tmp_h^self.png_header_h == tmp_l^self.png_header_l:
                    file_type = '.png'
                    file_decode_num = tmp_h^self.png_header_h
                elif tmp_h^self.jpg_header_h == tmp_l^self.jpg_header_l:
                    file_type = '.jpg'
                    file_decode_num = tmp_h^self.jpg_header_h
                elif tmp_h^self.gif_header_h == tmp_l^self.gif_header_l:
                    file_type = '.gif'
                    file_decode_num = tmp_h^self.gif_header_h
                else:
                    continue

                save_file_path = os.path.join(save_path, os.path.basename(decode_file).replace(".dat", file_type))
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

        self.updateSignal.emit('Done!')
        self.statusBar.showMessage('转换完成')


    def wechatImgDatDecode(self, img_path, save_path):
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
                                    if tmp_h^self.png_header_h == tmp_l^self.png_header_l:
                                        file_type = '.png'
                                        file_decode_num = tmp_h^self.png_header_h
                                    elif tmp_h^self.jpg_header_h == tmp_l^self.jpg_header_l:
                                        file_type = '.jpg'
                                        file_decode_num = tmp_h^self.jpg_header_h
                                    elif tmp_h^self.gif_header_h == tmp_l^self.gif_header_l:
                                        file_type = '.gif'
                                        file_decode_num = tmp_h^self.gif_header_h
                                    else:
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
        self.updateSignal.emit('Done!')
        self.statusBar.showMessage('转换完成')

    def wechatVersionCheckBoxEvent(self):
        if self.wechatVersionCheckBox.isChecked():
            self.oldWechatDecodeFlag = True
        else:
            self.oldWechatDecodeFlag = False

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
        if self.oldWechatDecodeFlag:
            decode_thread = threading.Thread(target=self.oldwechatImgDatDecode, args=(self.pathLineEdit.text(), self.savePathLineEdit.text()))
        else:
            decode_thread = threading.Thread(target=self.wechatImgDatDecode, args=(self.pathLineEdit.text(), self.savePathLineEdit.text()))
        decode_thread.start()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    f = QFile(":/qss/main.qss")
    f.open(QIODevice.ReadOnly)
    app.setStyleSheet(str(f.readAll(), encoding="utf-8"))
    f.close()

    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec())

