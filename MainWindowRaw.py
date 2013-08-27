# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\LEDMatrixCodeGenerate\MainWindowRaw.ui'
#
# Created: Sun Jun 16 01:01:59 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(744, 426)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 401, 341))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.pushButton_copy = QtGui.QPushButton(self.centralwidget)
        self.pushButton_copy.setGeometry(QtCore.QRect(580, 350, 161, 51))
        self.pushButton_copy.setObjectName(_fromUtf8("pushButton_copy"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(410, 0, 331, 341))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_generate = QtGui.QPushButton(self.centralwidget)
        self.pushButton_generate.setGeometry(QtCore.QRect(410, 350, 161, 51))
        self.pushButton_generate.setObjectName(_fromUtf8("pushButton_generate"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 350, 401, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_copy.setText(_translate("MainWindow", "Copy", None))
        self.pushButton_generate.setText(_translate("MainWindow", "Generate", None))
        self.pushButton.setText(_translate("MainWindow", "Clear", None))

