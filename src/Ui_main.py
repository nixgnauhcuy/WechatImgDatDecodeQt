from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 420)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pathLineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.pathLineEdit.setGeometry(QtCore.QRect(30, 20, 441, 32))
        self.pathLineEdit.setReadOnly(True)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.pathPushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pathPushButton.setGeometry(QtCore.QRect(480, 20, 91, 34))
        self.pathPushButton.setObjectName("pathPushButton")
        self.decodePushButton = QtWidgets.QPushButton(self.centralWidget)
        self.decodePushButton.setGeometry(QtCore.QRect(120, 100, 451, 31))
        self.decodePushButton.setObjectName("decodePushButton")
        self.logPlainTextEdit = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.logPlainTextEdit.setGeometry(QtCore.QRect(30, 140, 541, 241))
        self.logPlainTextEdit.setObjectName("logPlainTextEdit")
        self.savePathLineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.savePathLineEdit.setGeometry(QtCore.QRect(30, 60, 441, 32))
        self.savePathLineEdit.setReadOnly(True)
        self.savePathLineEdit.setObjectName("savePathLineEdit")
        self.savePathPushButton = QtWidgets.QPushButton(self.centralWidget)
        self.savePathPushButton.setGeometry(QtCore.QRect(480, 60, 91, 34))
        self.savePathPushButton.setObjectName("savePathPushButton")
        self.wechatVersionCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.wechatVersionCheckBox.setGeometry(QtCore.QRect(40, 100, 80, 31))
        self.wechatVersionCheckBox.setObjectName("wechatVersionCheckBox")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WechatImgDatDecode"))
        self.pathPushButton.setText(_translate("MainWindow", "选择路径"))
        self.decodePushButton.setText(_translate("MainWindow", "转换"))
        self.savePathPushButton.setText(_translate("MainWindow", "保存路径"))
        self.wechatVersionCheckBox.setText(_translate("MainWindow", "旧版微信"))
