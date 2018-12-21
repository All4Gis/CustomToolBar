# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.resources\About.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(550, 210)
        About.setMinimumSize(QtCore.QSize(550, 210))
        About.setMaximumSize(QtCore.QSize(550, 210))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/images/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/images/icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(About)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setGeometry(QtCore.QRect(140, 10, 401, 161))
        self.plainTextEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_2 = QtWidgets.QPushButton(About)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 180, 401, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(About)
        self.pushButton_2.clicked.connect(About.ShowVideo)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.plainTextEdit.setPlainText(_translate("About", "Customize ToolBars\n"
"2015-Francisco Raga\n"
"\n"
"\n"
"This plugin allows to create personalized tools, with the buttons the user desires. It is only necessary dragging from the list on the left and dropping in the list on the right, the tools that the user desires to add to any of the previously created toolbars.\n"
"\n"
"In order to ease the use of this plugin, a video with a brief example is attached."))
        self.pushButton_2.setText(_translate("About", "Show Video example"))

from CustomToolBar.gui import resources_rc
