# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.resources\About.ui'
#
# Created: Wed Aug 19 11:49:01 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(550, 210)
        About.setMinimumSize(QtCore.QSize(550, 210))
        About.setMaximumSize(QtCore.QSize(550, 210))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/images/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.label = QtGui.QLabel(About)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 91))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/img/images/icon.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.plainTextEdit = QtGui.QPlainTextEdit(About)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setGeometry(QtCore.QRect(140, 10, 401, 161))
        self.plainTextEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QtGui.QFrame.Raised)
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton_2 = QtGui.QPushButton(About)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 180, 401, 23))
        self.pushButton_2.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(About)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), About.ShowVideo)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(QtGui.QApplication.translate("About", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit.setPlainText(QtGui.QApplication.translate("About", "Customize ToolBars\n"
"2015-Francisco Raga\n"
"\n"
"\n"
"This plugin allows to create personalized tools, with the buttons the user desires. It is only necessary dragging from the list on the left and dropping in the list on the right, the tools that the user desires to add to any of the previously created toolbars.\n"
"\n"
"In order to ease the use of this plugin, a video with a brief example is attached.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("About", "Show Video example", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
