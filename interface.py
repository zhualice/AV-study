# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.ui'
#
# Created: Thu Jun  5 14:10:44 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(503, 371)
        self.wavfile = QtGui.QLineEdit(Dialog)
        self.wavfile.setEnabled(True)
        self.wavfile.setGeometry(QtCore.QRect(10, 50, 391, 27))
        self.wavfile.setReadOnly(True)
        self.wavfile.setObjectName(_fromUtf8("wavfile"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 51, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.selectfile = QtGui.QPushButton(Dialog)
        self.selectfile.setGeometry(QtCore.QRect(410, 50, 85, 27))
        self.selectfile.setObjectName(_fromUtf8("selectfile"))
        self.plotamplitude = QtGui.QPushButton(Dialog)
        self.plotamplitude.setGeometry(QtCore.QRect(10, 330, 111, 27))
        self.plotamplitude.setObjectName(_fromUtf8("plotamplitude"))
        self.startanimation = QtGui.QPushButton(Dialog)
        self.startanimation.setGeometry(QtCore.QRect(394, 330, 101, 27))
        self.startanimation.setObjectName(_fromUtf8("startanimation"))
        self.clearanimation = QtGui.QPushButton(Dialog)
        self.clearanimation.setGeometry(QtCore.QRect(190, 330, 131, 27))
        self.clearanimation.setObjectName(_fromUtf8("clearanimation"))
        self.duration = QtGui.QLabel(Dialog)
        self.duration.setGeometry(QtCore.QRect(10, 90, 141, 17))
        self.duration.setObjectName(_fromUtf8("duration"))
        self.animationsizelabel = QtGui.QLabel(Dialog)
        self.animationsizelabel.setGeometry(QtCore.QRect(200, 90, 191, 17))
        self.animationsizelabel.setObjectName(_fromUtf8("animationsizelabel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "WAV file", None, QtGui.QApplication.UnicodeUTF8))
        self.selectfile.setText(QtGui.QApplication.translate("Dialog", "Select file...", None, QtGui.QApplication.UnicodeUTF8))
        self.plotamplitude.setText(QtGui.QApplication.translate("Dialog", "Plot amplitude", None, QtGui.QApplication.UnicodeUTF8))
        self.startanimation.setText(QtGui.QApplication.translate("Dialog", "Start animation", None, QtGui.QApplication.UnicodeUTF8))
        self.clearanimation.setText(QtGui.QApplication.translate("Dialog", "Clear graphics queue", None, QtGui.QApplication.UnicodeUTF8))
        self.duration.setText(QtGui.QApplication.translate("Dialog", "Sound duration: -", None, QtGui.QApplication.UnicodeUTF8))
        self.animationsizelabel.setText(QtGui.QApplication.translate("Dialog", "Animation data size: -", None, QtGui.QApplication.UnicodeUTF8))

