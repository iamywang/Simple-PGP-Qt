# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_pgp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 240, 400, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.key_label_1 = QtWidgets.QLabel(Dialog)
        self.key_label_1.setGeometry(QtCore.QRect(0, 10, 100, 32))
        self.key_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_1.setObjectName("key_label_1")
        self.key_tf_2 = QtWidgets.QTextEdit(Dialog)
        self.key_tf_2.setGeometry(QtCore.QRect(100, 50, 300, 32))
        self.key_tf_2.setObjectName("key_tf_2")
        self.key_tf_5 = QtWidgets.QTextEdit(Dialog)
        self.key_tf_5.setEnabled(True)
        self.key_tf_5.setGeometry(QtCore.QRect(100, 170, 300, 32))
        self.key_tf_5.setObjectName("key_tf_5")
        self.key_tf_1 = QtWidgets.QTextEdit(Dialog)
        self.key_tf_1.setGeometry(QtCore.QRect(100, 10, 300, 32))
        self.key_tf_1.setObjectName("key_tf_1")
        self.key_label_4 = QtWidgets.QLabel(Dialog)
        self.key_label_4.setGeometry(QtCore.QRect(200, 130, 100, 32))
        self.key_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_4.setObjectName("key_label_4")
        self.key_label_3 = QtWidgets.QLabel(Dialog)
        self.key_label_3.setGeometry(QtCore.QRect(0, 90, 100, 32))
        self.key_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_3.setObjectName("key_label_3")
        self.key_tf_4 = QtWidgets.QTextEdit(Dialog)
        self.key_tf_4.setEnabled(True)
        self.key_tf_4.setGeometry(QtCore.QRect(300, 130, 100, 32))
        self.key_tf_4.setObjectName("key_tf_4")
        self.key_label_2 = QtWidgets.QLabel(Dialog)
        self.key_label_2.setGeometry(QtCore.QRect(0, 50, 100, 32))
        self.key_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_2.setObjectName("key_label_2")
        self.key_label_5 = QtWidgets.QLabel(Dialog)
        self.key_label_5.setGeometry(QtCore.QRect(0, 170, 100, 32))
        self.key_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_5.setObjectName("key_label_5")
        self.key_tf_3 = QtWidgets.QTextEdit(Dialog)
        self.key_tf_3.setGeometry(QtCore.QRect(100, 90, 300, 32))
        self.key_tf_3.setObjectName("key_tf_3")
        self.key_label_6 = QtWidgets.QLabel(Dialog)
        self.key_label_6.setGeometry(QtCore.QRect(0, 130, 100, 32))
        self.key_label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_6.setObjectName("key_label_6")
        self.key_tf_6 = QtWidgets.QTextEdit(Dialog)
        self.key_tf_6.setEnabled(True)
        self.key_tf_6.setGeometry(QtCore.QRect(100, 130, 100, 32))
        self.key_tf_6.setObjectName("key_tf_6")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "新建密钥"))
        self.key_label_1.setText(_translate("Dialog", "姓名"))
        self.key_tf_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.蘋方-簡\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.key_label_4.setText(_translate("Dialog", "RSA密钥长度"))
        self.key_label_3.setText(_translate("Dialog", "密码"))
        self.key_tf_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.蘋方-簡\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4096</p></body></html>"))
        self.key_label_2.setText(_translate("Dialog", "电子邮件"))
        self.key_label_5.setText(_translate("Dialog", "期限"))
        self.key_label_6.setText(_translate("Dialog", "加密方式"))
        self.key_tf_6.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.蘋方-簡\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">RSA</p></body></html>"))

