# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.resources\ui_CustomToolbar.ui'
#
# Created: Tue Jun 09 23:05:22 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_CustomToolbarDialog(object):
    def setupUi(self, CustomToolbarDialog):
        CustomToolbarDialog.setObjectName(_fromUtf8("CustomToolbarDialog"))
        CustomToolbarDialog.resize(807, 404)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CustomToolbarDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(CustomToolbarDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 25, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.groupBox = QtGui.QGroupBox(CustomToolbarDialog)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.ToolBars = QtGui.QTreeWidget(self.groupBox)
        self.ToolBars.setDragEnabled(True)
        self.ToolBars.setDragDropOverwriteMode(False)
        self.ToolBars.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.ToolBars.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.ToolBars.setAlternatingRowColors(True)
        self.ToolBars.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.ToolBars.setItemsExpandable(True)
        self.ToolBars.setAllColumnsShowFocus(False)
        self.ToolBars.setWordWrap(False)
        self.ToolBars.setObjectName(_fromUtf8("ToolBars"))
        self.ToolBars.headerItem().setText(0, _fromUtf8("ToolBars"))
        self.ToolBars.header().setSortIndicatorShown(False)
        self.ToolBars.header().setStretchLastSection(True)
        self.horizontalLayout_3.addWidget(self.ToolBars)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.new_btn = QtGui.QPushButton(CustomToolbarDialog)
        self.new_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.new_btn.setStyleSheet(_fromUtf8("border:1px solid #6E6E6E;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"min-width: 3em;\n"
"padding: 2px;\n"
""))
        self.new_btn.setFlat(True)
        self.new_btn.setObjectName(_fromUtf8("new_btn"))
        self.verticalLayout.addWidget(self.new_btn)
        self.rename_btn = QtGui.QPushButton(CustomToolbarDialog)
        self.rename_btn.setEnabled(False)
        self.rename_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rename_btn.setStyleSheet(_fromUtf8("border:1px solid #6E6E6E;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"min-width: 3em;\n"
"padding: 2px;"))
        self.rename_btn.setFlat(True)
        self.rename_btn.setObjectName(_fromUtf8("rename_btn"))
        self.verticalLayout.addWidget(self.rename_btn)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.delete_btn = QtGui.QPushButton(CustomToolbarDialog)
        self.delete_btn.setEnabled(False)
        self.delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_btn.setStyleSheet(_fromUtf8("border:1px solid #6E6E6E;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"min-width: 3em;\n"
"padding: 2px;"))
        self.delete_btn.setFlat(True)
        self.delete_btn.setObjectName(_fromUtf8("delete_btn"))
        self.verticalLayout.addWidget(self.delete_btn)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.Save_btn = QtGui.QPushButton(CustomToolbarDialog)
        self.Save_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Save_btn.setStyleSheet(_fromUtf8("border:1px solid #6E6E6E;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"padding: 2px;\n"
""))
        self.Save_btn.setFlat(True)
        self.Save_btn.setObjectName(_fromUtf8("Save_btn"))
        self.verticalLayout.addWidget(self.Save_btn)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.groupBox_2 = QtGui.QGroupBox(CustomToolbarDialog)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.MyToolsBars = QtGui.QTreeWidget(self.groupBox_2)
        self.MyToolsBars.setEnabled(False)
        self.MyToolsBars.setDragEnabled(False)
        self.MyToolsBars.setDragDropOverwriteMode(False)
        self.MyToolsBars.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.MyToolsBars.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.MyToolsBars.setAlternatingRowColors(True)
        self.MyToolsBars.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.MyToolsBars.setAutoExpandDelay(-1)
        self.MyToolsBars.setRootIsDecorated(True)
        self.MyToolsBars.setItemsExpandable(True)
        self.MyToolsBars.setObjectName(_fromUtf8("MyToolsBars"))
        self.horizontalLayout_2.addWidget(self.MyToolsBars)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(CustomToolbarDialog)
        QtCore.QObject.connect(self.ToolBars, QtCore.SIGNAL(_fromUtf8("itemPressed(QTreeWidgetItem*,int)")), CustomToolbarDialog.QgisToolsClick)
        QtCore.QObject.connect(self.MyToolsBars, QtCore.SIGNAL(_fromUtf8("itemClicked(QTreeWidgetItem*,int)")), CustomToolbarDialog.MyToolsClick)
        QtCore.QObject.connect(self.rename_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.RenameToolBar)
        QtCore.QObject.connect(self.new_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.NewToolBar)
        QtCore.QObject.connect(self.delete_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.DeleteToolBar)
        QtCore.QObject.connect(self.Save_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.SaveTools)
        QtCore.QMetaObject.connectSlotsByName(CustomToolbarDialog)

    def retranslateUi(self, CustomToolbarDialog):
        CustomToolbarDialog.setWindowTitle(_translate("CustomToolbarDialog", "Create customs ToolBars", None))
        self.groupBox.setTitle(_translate("CustomToolbarDialog", "Qgis Tools", None))
        self.ToolBars.setSortingEnabled(False)
        self.new_btn.setText(_translate("CustomToolbarDialog", "New ToolBar", None))
        self.rename_btn.setText(_translate("CustomToolbarDialog", "Rename ToolBar", None))
        self.delete_btn.setText(_translate("CustomToolbarDialog", "Delete ToolBar or Tool", None))
        self.Save_btn.setText(_translate("CustomToolbarDialog", "Save Changes", None))
        self.groupBox_2.setTitle(_translate("CustomToolbarDialog", "My ToolBars", None))
        self.MyToolsBars.headerItem().setText(0, _translate("CustomToolbarDialog", "ToolBars", None))

import resources_rc