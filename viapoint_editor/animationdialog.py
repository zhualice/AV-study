# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AnimationDialog.ui'
#
# Created: Mon Aug 25 10:00:35 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AnimationDialog(object):
    def setupUi(self, AnimationDialog):
        AnimationDialog.setObjectName(_fromUtf8("AnimationDialog"))
        AnimationDialog.resize(624, 569)
        self.buttonBox = QtGui.QDialogButtonBox(AnimationDialog)
        self.buttonBox.setGeometry(QtCore.QRect(430, 520, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(AnimationDialog)
        self.label.setGeometry(QtCore.QRect(10, 8, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(AnimationDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 320, 601, 71))
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 51, 31))
        self.label_5.setStyleSheet(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.text_audio = QtGui.QLineEdit(self.groupBox)
        self.text_audio.setGeometry(QtCore.QRect(80, 25, 331, 21))
        self.text_audio.setStyleSheet(_fromUtf8(""))
        self.text_audio.setReadOnly(True)
        self.text_audio.setObjectName(_fromUtf8("text_audio"))
        self.text_signal = QtGui.QLineEdit(self.groupBox)
        self.text_signal.setGeometry(QtCore.QRect(80, 50, 331, 20))
        self.text_signal.setStyleSheet(_fromUtf8(""))
        self.text_signal.setText(_fromUtf8(""))
        self.text_signal.setReadOnly(True)
        self.text_signal.setObjectName(_fromUtf8("text_signal"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 51, 21))
        self.label_6.setStyleSheet(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.button_audio = QtGui.QPushButton(self.groupBox)
        self.button_audio.setGeometry(QtCore.QRect(420, 26, 31, 21))
        self.button_audio.setObjectName(_fromUtf8("button_audio"))
        self.button_signal = QtGui.QPushButton(self.groupBox)
        self.button_signal.setGeometry(QtCore.QRect(420, 50, 31, 21))
        self.button_signal.setObjectName(_fromUtf8("button_signal"))
        self.check_signal = QtGui.QCheckBox(self.groupBox)
        self.check_signal.setGeometry(QtCore.QRect(470, 20, 111, 31))
        self.check_signal.setObjectName(_fromUtf8("check_signal"))
        self.button_select_data = QtGui.QPushButton(self.groupBox)
        self.button_select_data.setGeometry(QtCore.QRect(470, 50, 101, 20))
        self.button_select_data.setObjectName(_fromUtf8("button_select_data"))
        self.label_animation_name = QtGui.QPushButton(AnimationDialog)
        self.label_animation_name.setGeometry(QtCore.QRect(90, 8, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_animation_name.setFont(font)
        self.label_animation_name.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_animation_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_animation_name.setStyleSheet(_fromUtf8("QPushButton {\n"
"    text-align: left;\n"
"    color: blue;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"    border: none;\n"
"    outline: none;\n"
"}"))
        self.label_animation_name.setFlat(True)
        self.label_animation_name.setObjectName(_fromUtf8("label_animation_name"))
        self.label_4 = QtGui.QLabel(AnimationDialog)
        self.label_4.setGeometry(QtCore.QRect(350, 10, 31, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line = QtGui.QFrame(AnimationDialog)
        self.line.setGeometry(QtCore.QRect(10, 30, 601, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_animation_file = QtGui.QLabel(AnimationDialog)
        self.label_animation_file.setGeometry(QtCore.QRect(390, 10, 211, 16))
        self.label_animation_file.setObjectName(_fromUtf8("label_animation_file"))
        self.groupBox_2 = QtGui.QGroupBox(AnimationDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 420, 591, 71))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.line_2 = QtGui.QFrame(AnimationDialog)
        self.line_2.setGeometry(QtCore.QRect(10, 400, 601, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(AnimationDialog)
        self.line_3.setGeometry(QtCore.QRect(10, 300, 601, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.groupBox_3 = QtGui.QGroupBox(AnimationDialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 49, 601, 251))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(340, 30, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.button_add = QtGui.QPushButton(self.groupBox_3)
        self.button_add.setEnabled(False)
        self.button_add.setGeometry(QtCore.QRect(270, 180, 21, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_add.setFont(font)
        self.button_add.setObjectName(_fromUtf8("button_add"))
        self.button_up = QtGui.QToolButton(self.groupBox_3)
        self.button_up.setEnabled(False)
        self.button_up.setGeometry(QtCore.QRect(270, 50, 21, 24))
        self.button_up.setArrowType(QtCore.Qt.UpArrow)
        self.button_up.setObjectName(_fromUtf8("button_up"))
        self.table_variables = QtGui.QTableView(self.groupBox_3)
        self.table_variables.setGeometry(QtCore.QRect(340, 50, 256, 192))
        self.table_variables.setAlternatingRowColors(True)
        self.table_variables.setObjectName(_fromUtf8("table_variables"))
        self.table_variables.horizontalHeader().setDefaultSectionSize(120)
        self.table_variables.horizontalHeader().setSortIndicatorShown(False)
        self.table_variables.horizontalHeader().setStretchLastSection(True)
        self.table_variables.verticalHeader().setDefaultSectionSize(20)
        self.table_variables.verticalHeader().setMinimumSectionSize(20)
        self.button_remove = QtGui.QPushButton(self.groupBox_3)
        self.button_remove.setEnabled(False)
        self.button_remove.setGeometry(QtCore.QRect(270, 210, 21, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_remove.setFont(font)
        self.button_remove.setObjectName(_fromUtf8("button_remove"))
        self.list_list = QtGui.QListWidget(self.groupBox_3)
        self.list_list.setGeometry(QtCore.QRect(0, 50, 256, 191))
        self.list_list.setObjectName(_fromUtf8("list_list"))
        self.button_down = QtGui.QToolButton(self.groupBox_3)
        self.button_down.setEnabled(False)
        self.button_down.setGeometry(QtCore.QRect(270, 80, 21, 24))
        self.button_down.setArrowType(QtCore.Qt.DownArrow)
        self.button_down.setObjectName(_fromUtf8("button_down"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.button_interaction = QtGui.QToolButton(self.groupBox_3)
        self.button_interaction.setEnabled(False)
        self.button_interaction.setGeometry(QtCore.QRect(575, 30, 21, 17))
        self.button_interaction.setObjectName(_fromUtf8("button_interaction"))
        self.button_plot = QtGui.QPushButton(AnimationDialog)
        self.button_plot.setGeometry(QtCore.QRect(10, 520, 101, 27))
        self.button_plot.setObjectName(_fromUtf8("button_plot"))
        self.button_export = QtGui.QPushButton(AnimationDialog)
        self.button_export.setGeometry(QtCore.QRect(120, 520, 101, 27))
        self.button_export.setObjectName(_fromUtf8("button_export"))
        self.button_play_test = QtGui.QPushButton(AnimationDialog)
        self.button_play_test.setGeometry(QtCore.QRect(230, 520, 101, 27))
        self.button_play_test.setObjectName(_fromUtf8("button_play"))

        self.retranslateUi(AnimationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AnimationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AnimationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AnimationDialog)

    def retranslateUi(self, AnimationDialog):
        AnimationDialog.setWindowTitle(QtGui.QApplication.translate("AnimationDialog", "Animation", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AnimationDialog", "Animation:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("AnimationDialog", "Signal Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AnimationDialog", "Audio File:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AnimationDialog", "Signal File:", None, QtGui.QApplication.UnicodeUTF8))
        self.button_audio.setText(QtGui.QApplication.translate("AnimationDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.button_signal.setText(QtGui.QApplication.translate("AnimationDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.check_signal.setText(QtGui.QApplication.translate("AnimationDialog", "Use audio signal", None, QtGui.QApplication.UnicodeUTF8))
        self.button_select_data.setText(QtGui.QApplication.translate("AnimationDialog", "Select data...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_animation_name.setText(QtGui.QApplication.translate("AnimationDialog", "New Animation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AnimationDialog", "File:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_animation_file.setText(QtGui.QApplication.translate("AnimationDialog", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("AnimationDialog", "Animation Options", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("AnimationDialog", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AnimationDialog", "Parameter Variables", None, QtGui.QApplication.UnicodeUTF8))
        self.button_add.setToolTip(QtGui.QApplication.translate("AnimationDialog", "Add animation to queue", None, QtGui.QApplication.UnicodeUTF8))
        self.button_add.setText(QtGui.QApplication.translate("AnimationDialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.button_up.setToolTip(QtGui.QApplication.translate("AnimationDialog", "Move animation up", None, QtGui.QApplication.UnicodeUTF8))
        self.button_up.setText(QtGui.QApplication.translate("AnimationDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.button_remove.setToolTip(QtGui.QApplication.translate("AnimationDialog", "Remove selected animation", None, QtGui.QApplication.UnicodeUTF8))
        self.button_remove.setText(QtGui.QApplication.translate("AnimationDialog", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.button_down.setToolTip(QtGui.QApplication.translate("AnimationDialog", "Move animation down", None, QtGui.QApplication.UnicodeUTF8))
        self.button_down.setText(QtGui.QApplication.translate("AnimationDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AnimationDialog", "List", None, QtGui.QApplication.UnicodeUTF8))
        self.button_interaction.setText(QtGui.QApplication.translate("AnimationDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.button_plot.setText(QtGui.QApplication.translate("AnimationDialog", "Plot signals", None, QtGui.QApplication.UnicodeUTF8))
        self.button_export.setText(QtGui.QApplication.translate("AnimationDialog", "Export output", None, QtGui.QApplication.UnicodeUTF8))
        self.button_play_test.setText(QtGui.QApplication.translate("AnimationDialog", "Play test video", None, QtGui.QApplication.UnicodeUTF8))

