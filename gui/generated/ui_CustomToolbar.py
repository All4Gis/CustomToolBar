# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.resources\ui_CustomToolbar.ui'
#
# Created: Fri Jun 12 23:44:23 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import resources_rc


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CustomToolbarDialog(object):
    def setupUi(self, CustomToolbarDialog):
        CustomToolbarDialog.setObjectName(_fromUtf8("CustomToolbarDialog"))
        CustomToolbarDialog.resize(833, 443)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CustomToolbarDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(CustomToolbarDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 25, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(CustomToolbarDialog)
        self.pushButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/images/expand.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(CustomToolbarDialog)
        self.pushButton_2.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/images/collapse.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_6.addWidget(self.pushButton_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
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
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.new_btn = QtGui.QPushButton(CustomToolbarDialog)
        self.new_btn.setCursor(QtCore.Qt.PointingHandCursor)
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
        self.rename_btn.setCursor(QtCore.Qt.PointingHandCursor)
        self.rename_btn.setStyleSheet(_fromUtf8("border:1px solid #6E6E6E;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"min-width: 3em;\n"
"padding: 2px;"))
        self.rename_btn.setFlat(True)
        self.rename_btn.setObjectName(_fromUtf8("rename_btn"))
        self.verticalLayout.addWidget(self.rename_btn)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.delete_btn = QtGui.QPushButton(CustomToolbarDialog)
        self.delete_btn.setEnabled(False)
        self.delete_btn.setCursor(QtCore.Qt.PointingHandCursor)
        self.delete_btn.setStyleSheet(_fromUtf8("border:1px solid #6E6E6E;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"min-width: 3em;\n"
"padding: 2px;"))
        self.delete_btn.setFlat(True)
        self.delete_btn.setObjectName(_fromUtf8("delete_btn"))
        self.verticalLayout.addWidget(self.delete_btn)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.Save_btn = QtGui.QPushButton(CustomToolbarDialog)
        self.Save_btn.setCursor(QtCore.Qt.PointingHandCursor)
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
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.pushButton_3 = QtGui.QPushButton(CustomToolbarDialog)
        self.pushButton_3.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_8.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(CustomToolbarDialog)
        self.pushButton_4.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_8.addWidget(self.pushButton_4)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(CustomToolbarDialog)
        QtCore.QObject.connect(self.ToolBars, QtCore.SIGNAL(_fromUtf8("itemPressed(QTreeWidgetItem*,int)")), CustomToolbarDialog.QgisToolsClick)
        QtCore.QObject.connect(self.MyToolsBars, QtCore.SIGNAL(_fromUtf8("itemClicked(QTreeWidgetItem*,int)")), CustomToolbarDialog.MyToolsClick)
        QtCore.QObject.connect(self.rename_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.RenameToolBar)
        QtCore.QObject.connect(self.new_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.NewToolBar)
        QtCore.QObject.connect(self.delete_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.DeleteToolBar)
        QtCore.QObject.connect(self.Save_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.SaveTools)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.ExpandQgis)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.CollapseQgis)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.ExpandMyTools)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.CollapseMyTools)
        QtCore.QMetaObject.connectSlotsByName(CustomToolbarDialog)

    def retranslateUi(self, CustomToolbarDialog):
        CustomToolbarDialog.setWindowTitle(QtGui.QApplication.translate("CustomToolbarDialog", "Create customs ToolBars", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setToolTip(QtGui.QApplication.translate("CustomToolbarDialog", "Expand all", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setToolTip(QtGui.QApplication.translate("CustomToolbarDialog", "Collapse all", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("CustomToolbarDialog", "Qgis Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.ToolBars.setSortingEnabled(False)
        self.new_btn.setText(QtGui.QApplication.translate("CustomToolbarDialog", "New ToolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.rename_btn.setText(QtGui.QApplication.translate("CustomToolbarDialog", "Rename ToolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_btn.setText(QtGui.QApplication.translate("CustomToolbarDialog", "Delete ToolBar or Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.Save_btn.setText(QtGui.QApplication.translate("CustomToolbarDialog", "Save Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("CustomToolbarDialog", "My ToolBars", None, QtGui.QApplication.UnicodeUTF8))
        self.MyToolsBars.headerItem().setText(0, QtGui.QApplication.translate("CustomToolbarDialog", "ToolBars", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setToolTip(QtGui.QApplication.translate("CustomToolbarDialog", "Expand all", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setToolTip(QtGui.QApplication.translate("CustomToolbarDialog", "Collapse all", None, QtGui.QApplication.UnicodeUTF8))

