import sys
import os
import binascii
import threading
import main_qrc

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

        self.pathPushButton.clicked.connect(self.pathPushButtonEvent)
        self.decodePushButton.clicked.connect(self.decodePushButtonEvent)
        self.updateSignal.connect(self.updateUI)

    
    def updateUI(self, message):
        self.logPlainTextEdit.appendPlainText(message)


    def wechatImgDatDecode(self, img_path):
        dat_files_path = []
        files = os.listdir(img_path)
        for file in files:
            if file.endswith('.dat'):
                dat_files_path.append(img_path + '/' + file)

        for dat_file in dat_files_path:
            with open(dat_file, 'rb') as file:
                hex_data = binascii.hexlify(file.read(2)).decode('utf-8')
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

                output_file_path = dat_file.replace(".dat", file_type)
                if os.path.exists(output_file_path):
                    self.updateSignal.emit('已存在，跳过：' + output_file_path)
                    continue
                else:
                    self.updateSignal.emit(output_file_path)

                with open(output_file_path, 'wb') as output_file:
                    file.seek(0)
                    file_data = file.read()
                    block_data = bytearray(file_data)
                    for i in range(len(block_data)):
                        block_data[i] ^= file_decode_num
                    output_file.write(block_data)
        self.updateSignal.emit('Done!')
        self.statusBar.showMessage('转换完成')


    def pathPushButtonEvent(self):
        _path = QFileDialog.getExistingDirectory(self, '请选择图片所在文件夹', './')
        self.pathLineEdit.setText(_path)

    def decodePushButtonEvent(self):
        if self.pathLineEdit.text() == '':
            return
        
        self.logPlainTextEdit.clear()
        self.statusBar.showMessage('开始转换...')
        decode_thread = threading.Thread(target=self.wechatImgDatDecode, args=(self.pathLineEdit.text(),))
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

