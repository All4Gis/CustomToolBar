# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.resources\ui_CustomToolbar.ui'
#
# Created: Tue May 24 18:37:54 2016
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
        CustomToolbarDialog.resize(833, 443)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CustomToolbarDialog.setWindowIcon(icon)
        CustomToolbarDialog.setAccessibleDescription(_fromUtf8(""))
        self.verticalLayout_2 = QtGui.QVBoxLayout(CustomToolbarDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.help_btn = QtGui.QPushButton(CustomToolbarDialog)
        self.help_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.help_btn.setStyleSheet(_fromUtf8("text-align:left;"))
        self.help_btn.setFlat(True)
        self.help_btn.setObjectName(_fromUtf8("help_btn"))
        self.horizontalLayout.addWidget(self.help_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.pushButton = QtGui.QPushButton(CustomToolbarDialog)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/images/expand.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(CustomToolbarDialog)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/images/collapse.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_6.addWidget(self.pushButton_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.groupBox = QtGui.QGroupBox(CustomToolbarDialog)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.searchBox = QgsFilterLineEdit(self.groupBox)
        self.searchBox.setObjectName(_fromUtf8("searchBox"))
        self.verticalLayout_4.addWidget(self.searchBox)
        self.ToolBars = QtGui.QTreeWidget(self.groupBox)
        self.ToolBars.setStyleSheet(_fromUtf8(""))
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
        self.ToolBars.header().setVisible(False)
        self.ToolBars.header().setSortIndicatorShown(False)
        self.ToolBars.header().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.ToolBars)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
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
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
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
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
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
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.MyToolsBars = QtGui.QTreeWidget(self.groupBox_2)
        self.MyToolsBars.setEnabled(False)
        self.MyToolsBars.setStyleSheet(_fromUtf8(""))
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
        self.MyToolsBars.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.MyToolsBars)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.My_expand = QtGui.QPushButton(CustomToolbarDialog)
        self.My_expand.setEnabled(False)
        self.My_expand.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.My_expand.setText(_fromUtf8(""))
        self.My_expand.setIcon(icon1)
        self.My_expand.setAutoDefault(False)
        self.My_expand.setFlat(True)
        self.My_expand.setObjectName(_fromUtf8("My_expand"))
        self.verticalLayout_8.addWidget(self.My_expand)
        self.My_Collapse = QtGui.QPushButton(CustomToolbarDialog)
        self.My_Collapse.setEnabled(False)
        self.My_Collapse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.My_Collapse.setText(_fromUtf8(""))
        self.My_Collapse.setIcon(icon2)
        self.My_Collapse.setAutoDefault(False)
        self.My_Collapse.setFlat(True)
        self.My_Collapse.setObjectName(_fromUtf8("My_Collapse"))
        self.verticalLayout_8.addWidget(self.My_Collapse)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem7)
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
        QtCore.QObject.connect(self.My_expand, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.ExpandMyTools)
        QtCore.QObject.connect(self.My_Collapse, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.CollapseMyTools)
        QtCore.QObject.connect(self.searchBox, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), CustomToolbarDialog.Search)
        QtCore.QObject.connect(self.help_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), CustomToolbarDialog.about)
        QtCore.QMetaObject.connectSlotsByName(CustomToolbarDialog)

    def retranslateUi(self, CustomToolbarDialog):
        CustomToolbarDialog.setWindowTitle(_translate("CustomToolbarDialog", "Create customs ToolBars", None))
        self.help_btn.setText(_translate("CustomToolbarDialog", "About", None))
        self.pushButton.setToolTip(_translate("CustomToolbarDialog", "Expand all", None))
        self.pushButton_2.setToolTip(_translate("CustomToolbarDialog", "Collapse all", None))
        self.groupBox.setTitle(_translate("CustomToolbarDialog", "Qgis Tools", None))
        self.searchBox.setToolTip(_translate("CustomToolbarDialog", "Enter algorithm name to filter list", None))
        self.ToolBars.setSortingEnabled(False)
        self.new_btn.setText(_translate("CustomToolbarDialog", "New ToolBar", None))
        self.rename_btn.setText(_translate("CustomToolbarDialog", "Rename ToolBar", None))
        self.delete_btn.setText(_translate("CustomToolbarDialog", "Delete ToolBar or Tool", None))
        self.Save_btn.setText(_translate("CustomToolbarDialog", "Save Changes", None))
        self.groupBox_2.setTitle(_translate("CustomToolbarDialog", "My ToolBars", None))
        self.My_expand.setToolTip(_translate("CustomToolbarDialog", "Expand all", None))
        self.My_Collapse.setToolTip(_translate("CustomToolbarDialog", "Collapse all", None))

from qgis.gui import QgsFilterLineEdit
import resources_rc
