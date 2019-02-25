# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sendForm(object):
    def setupUi(self, sendForm):
        sendForm.setObjectName("sendForm")
        sendForm.resize(780, 542)
        self.textEdit = QtWidgets.QTextEdit(sendForm)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 171, 31))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(sendForm)
        QtCore.QMetaObject.connectSlotsByName(sendForm)

    def retranslateUi(self, sendForm):
        _translate = QtCore.QCoreApplication.translate
        sendForm.setWindowTitle(_translate("sendForm", "UDP发送测试终端"))

