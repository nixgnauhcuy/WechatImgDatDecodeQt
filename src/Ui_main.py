# Form implementation generated from reading ui file 'f:\tmp\WechatImgDatDecodeQt_dev\src\main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 436)
        self.centralWidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.widget = QtWidgets.QWidget(parent=self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 611, 391))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.decodePushButton = QtWidgets.QPushButton(parent=self.widget)
        self.decodePushButton.setObjectName("decodePushButton")
        self.gridLayout.addWidget(self.decodePushButton, 2, 0, 1, 1)
        self.savePathPushButton = QtWidgets.QPushButton(parent=self.widget)
        self.savePathPushButton.setObjectName("savePathPushButton")
        self.gridLayout.addWidget(self.savePathPushButton, 1, 1, 1, 1)
        self.logPlainTextEdit = QtWidgets.QPlainTextEdit(parent=self.widget)
        self.logPlainTextEdit.setObjectName("logPlainTextEdit")
        self.gridLayout.addWidget(self.logPlainTextEdit, 3, 0, 1, 1)
        self.savePathLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.savePathLineEdit.setReadOnly(True)
        self.savePathLineEdit.setObjectName("savePathLineEdit")
        self.gridLayout.addWidget(self.savePathLineEdit, 1, 0, 1, 1)
        self.pathLineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.pathLineEdit.setReadOnly(True)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.gridLayout.addWidget(self.pathLineEdit, 0, 0, 1, 1)
        self.pathPushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pathPushButton.setObjectName("pathPushButton")
        self.gridLayout.addWidget(self.pathPushButton, 0, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(parent=self.widget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WechatImgDatDecode"))
        self.decodePushButton.setText(_translate("MainWindow", "转换"))
        self.savePathPushButton.setText(_translate("MainWindow", "保存路径"))
        self.pathPushButton.setText(_translate("MainWindow", "选择路径"))
