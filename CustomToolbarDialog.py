# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CustomToolbar
                                 A QGIS plugin
 Create customs Toolbars for Qgis.
                             -------------------
        begin                : 2015-06-09
        copyright            : (C) 2015 All4Gis.
        email                : franka1986@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation either version 2 of the License, or     *
 #   any later version.                                                    *
 *                                                                         *
 ***************************************************************************/
"""
import os.path
from qgis.core import Qgis as QGis
from qgis.core import QgsApplication

from PyQt5.QtCore import Qt, QFile, QDataStream, QIODevice
from PyQt5.QtWidgets import (QToolBar,
                             QInputDialog,
                             QWidgetAction,
                             QDialog,
                             QTreeWidgetItem,
                             QMessageBox)

from CustomToolBar.About import AboutDialog
from CustomToolBar.gui.ui_CustomToolbar import Ui_CustomToolbarDialog
from CustomToolBar.utils.utils import DelToolBarIface, obtainAction

try:
    from pydevd import *
except ImportError:
    None


class CustomToolbarDialog(QDialog, Ui_CustomToolbarDialog):

    def __init__(self, iface=None):
        QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.hasChanged = False
        self.userhome = os.path.expanduser('~')
        self.filepath = self.userhome + '//.CustomToolBars'
        self.file = QFile(self.filepath)

        self.restore = {}

        try:
            self.listMyToolBars()  # User Tools
            self.PopulateQgisTools()  # Qgis tools
        except Exception:
            self.iface.messageBar().pushMessage("Error: ", " Error loading Custom Toolbars", level=QGis.Critical, duration=3)
            None

        if self.MyToolsBars.isEnabled() is False:
            self.Save_btn.setEnabled(False)

        # Drop user list
        def dropEvent(event):
            self.hasChanged = True
            destinationItem = self.MyToolsBars.itemAt(event.pos()) 
            if destinationItem is None:
                return
            depth = self.depth(destinationItem)

            if depth <= 2:
                if destinationItem.text(0) == "":
                    self.iface.messageBar().pushMessage("Info: ", "You must add the button into a tool.", level=QGis.Info, duration=3)
                    return
                SelectedItem = self.MyToolsBars.currentItem()
                if SelectedItem is not None:
                    if self.depth(SelectedItem) == 1:
                        self.iface.messageBar().pushMessage("Info: ", "You can not put a tool into another.", level=QGis.Info, duration=3)
                        return

                    SelectedItem_Parent = SelectedItem.parent()
                    destinationItem_Parent = destinationItem.parent()
                    if destinationItem_Parent is None:
                        SelectedItem_index = SelectedItem_Parent.indexOfChild(SelectedItem)
                        child = SelectedItem_Parent.takeChild(SelectedItem_index)
                        destinationItem.insertChild(0, SelectedItem)

                    else:
                        SelectedItem_index = SelectedItem_Parent.indexOfChild(SelectedItem)
                        destinationItem_index = destinationItem_Parent.indexOfChild(destinationItem)
                        child = SelectedItem_Parent.child(SelectedItem_index)
                        destinationItem_Parent.insertChild(destinationItem_index + 1, child.clone())

                        if SelectedItem_Parent != destinationItem_Parent:
                            SelectedItem_Parent.takeChild(SelectedItem_index)
                        else: 
                            # Movement from top to bottom
                            if SelectedItem_index < destinationItem_index:
                                SelectedItem_Parent.takeChild(SelectedItem_index)
                            else:
                                # Movement from bottom to top
                                SelectedItem_Parent.takeChild(SelectedItem_index + 1)

                    return

                else:
                    if self.depth(destinationItem) == 1:
                        SelectedItem = self.ToolBars.currentItem()
                        destinationItem.insertChild(0, SelectedItem.clone())
                    if self.depth(destinationItem) == 2:
                        SelectedItem = self.ToolBars.currentItem()
                        SelectedItem_Parent = SelectedItem.parent()
                        SelectedItem_index = SelectedItem_Parent.indexOfChild(SelectedItem)
                        destinationItem_Parent = destinationItem.parent()
                        destinationItem_index = destinationItem_Parent.indexOfChild(destinationItem)
                        child = SelectedItem_Parent.child(SelectedItem_index)
                        destinationItem_Parent.insertChild(destinationItem_index + 1, child.clone())

            else:
                return

            self.MyToolsBars.setCurrentItem(None)
            event.acceptProposedAction()

        self.MyToolsBars.dropEvent = dropEvent

    # We get the depth of the item in the tree
    def depth(self, item):
        depth = 0
        while item is not None:
            item = item.parent()
            depth += 1
        return depth

    # Help Dialog
    def about(self):
        self.About = AboutDialog(self.iface)
        self.About.exec_()

    # Filtering the actions in the Qgis tools.
    def Search(self, text):
        self.filterItem(self.ToolBars.invisibleRootItem(), text)
        if text:
            self.ToolBars.expandAll()
        else:
            self.ToolBars.collapseAll() 
        return

    def filterItem(self, item, text):
        if (item.childCount() > 0):
            show = False
            for i in range(item.childCount()):
                child = item.child(i)
                showChild = self.filterItem(child, text)
                show = showChild or show
            item.setHidden(not show)
            return show
        elif isinstance(item, (QTreeWidgetItem)):
            hide = bool(text) and (text not in item.text(0).lower())
            item.setHidden(hide)
            return not hide
        else:
            item.setHidden(True)
            return False

    # We get Qgis toolbars
    def PopulateQgisTools(self):
        self.ToolBars.clear()
        # Qgis tools.
        toolbars = self.iface.mainWindow().findChildren(QToolBar)
        topitem = QTreeWidgetItem(self.ToolBars)
        topitem.setText(0, "ToolBars") 
        for toolbar in toolbars:
            pitems = QTreeWidgetItem(topitem)
            if toolbar.windowTitle() == '':
                pitems.setText(0, "No Name")
            else:
                pitems.setText(0, toolbar.windowTitle())

            actions = toolbar.actions()

            for action in actions:

                if isinstance(action, QWidgetAction):
                    a = action.defaultWidget().actions()
                    for b in a:
                        # Removed empty values, such as decorative bars in the toolbar,etc..
                        if b.text() == "":
                            continue
                        citems = QTreeWidgetItem(pitems)
                        citems.setIcon(0, b.icon())
                        citems.setText(0, b.iconText()) 
                        citems.setToolTip(0, b.iconText())
                else:
                    if action.text() == "":
                        continue
                    citems = QTreeWidgetItem(pitems)
                    citems.setIcon(0, action.icon())
                    citems.setText(0, action.iconText())
                    citems.setToolTip(0, action.iconText())

        # Menus Actions
        menubar = self.iface.mainWindow().menuBar() 
        topitem = QTreeWidgetItem(self.ToolBars)
        topitem.setText(0, "Menus")
        for action in menubar.actions():
            self.addTreeItemMenu(parentItem=topitem, action=action)

        # Processing ToolBox.(Remove old groups)
#         try:
#             topitem = QTreeWidgetItem(self.ToolBars)
#             topitem.setText(0, "Processing Algorithms")
#             for alg in QgsApplication.processingRegistry().algorithms():
#                 citems = QTreeWidgetItem(topitem)
#                 citems.setIcon(0, alg.icon())
#                 citems.setText(0, alg.displayName())
#                 citems.setToolTip(0, alg.displayName())
#                 topitem.addChild(citems)
#             return
#         except Exception:
#             self.iface.messageBar().pushMessage("Error: ",
#                                                 "Error loading Processing Toolbox.",
#                                                 level=QGis.Critical, duration=3)
#             None

    def addTreeItemMenu(self, parentItem=None, action=None):
        if action.inherits("QMenu"):
            citems = QTreeWidgetItem(parentItem)
            citems.setIcon(0, action.icon())
            citems.setText(0, action.title().replace("&", ""))
            citems.setToolTip(0, action.title().replace("&", ""))
 
        if action.inherits("QAction"):
            citems = QTreeWidgetItem(parentItem)
            citems.setIcon(0, action.icon())
            citems.setText(0, action.iconText())
            citems.setToolTip(0, action.iconText())
        try:
            if action.menu():
                self.addTreeItemActions(citems, action.menu().actions())
        except Exception:
            self.addTreeItemActions(citems, action.actions())

    def addTreeItemActions(self, parentItem, actions):
        for action in actions:
            if action.isSeparator():
                continue

            if action.menu():
                self.addTreeItemMenu(parentItem, action.menu())

            else:
                citems = QTreeWidgetItem(parentItem)
                citems.setIcon(0, action.icon())
                citems.setText(0, action.iconText())
                citems.setToolTip(0, action.iconText())

    # Gestion de clicks en el listado de herramientas de Qgis.
    # Solo se permite mover las herramientas,no las toolbar
    def QgisToolsClick(self):
        item = self.ToolBars.currentItem()
        parent = item.parent()
        self.MyToolsBars.setCurrentItem(None)
        self.rename_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        if parent is None or item.childCount() > 0:
            self.ToolBars.setDragEnabled(False)
        else:
            self.ToolBars.setDragEnabled(True)

    # list of user tools
    def MyToolsClick(self, _):
        selected = self.MyToolsBars.currentItem()
        if selected is not None:
            parent = self.MyToolsBars.currentItem().parent()
            if parent is not None:
                self.rename_btn.setEnabled(False)
                self.delete_btn.setEnabled(True)
            else:
                self.rename_btn.setEnabled(True)
                self.delete_btn.setEnabled(True)

        return

    # Create a new ToolBar
    def NewToolBar(self):
        flags = Qt.Window | Qt.WindowCloseButtonHint
        text, ok = QInputDialog.getText(self, 'ToolBar Name',
                                        'Enter new Toolbar name.',
                                        flags=flags)
        if ok:
            if text == "":
                self.iface.messageBar().pushMessage("Error: ", "Enter Toolbar name.",
                                                    level=QGis.Critical,
                                                    duration=3)
                return
            new_toolbar = QTreeWidgetItem()
            new_toolbar.setText(0, text)
            self.MyToolsBars.invisibleRootItem().addChild(new_toolbar)
            self.MyToolsBars.setEnabled(True)
            self.My_expand.setEnabled(True)
            self.My_Collapse.setEnabled(True)
            self.Save_btn.setEnabled(True)
            self.hasChanged = True
        return

    # Rename only the ToolBar name
    def RenameToolBar(self):
        flags = Qt.Window | Qt.WindowCloseButtonHint
        text, ok = QInputDialog.getText(self, 'ToolBar Name', 'Enter new Toolbar name.', flags=flags)
        if ok:
            if text == "":
                self.iface.messageBar().pushMessage("Error: ", "Enter Toolbar name.", level=QGis.Critical, duration=3)
                return 

            item = self.MyToolsBars.currentItem()
            text_old = item.text(self.MyToolsBars.currentColumn())

            # Rename the toolbar in the iface
            toolbars = self.iface.mainWindow().findChildren(QToolBar)
            for toolbar in toolbars:
                if toolbar.windowTitle() == text_old:
                    toolbar.setWindowTitle(text)

            item.setText(self.MyToolsBars.currentColumn(), text)
            self.hasChanged = True

            for key, value in self.restore.items():
                if text_old == value:
                    self.restore[key] = text
                    return

            self.restore[text_old] = text

        return

    # Remove all toolbar
    def DeleteToolBar(self):
        text = self.MyToolsBars.currentItem().text(0)
        reply = QMessageBox.question(self, "Delete ToolBar",
                                           "Sure you want to delete '" + text + "' ?",
                                           QMessageBox.Yes | 
                                           QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.hasChanged = True
            root = self.MyToolsBars.invisibleRootItem()
            for item in self.MyToolsBars.selectedItems():
                (item.parent() or root).removeChild(item)

            if self.rename_btn.isEnabled():
                DelToolBarIface(text, self.iface)  # We delete the toolbar
                # We restore the list of Qgis tools.
                state = self.saveWidgetState(self.ToolBars) 
                self.PopulateQgisTools()
                self.loadWidgetState(self.ToolBars, state) 

            num_chils = root.childCount()
            if num_chils == 0:
                self.MyToolsBars.setEnabled(False)
                self.rename_btn.setEnabled(False)
                self.delete_btn.setEnabled(False)
                self.My_expand.setEnabled(False)
                self.My_Collapse.setEnabled(False)

        return

    # Restauramos el nombre antiguo si el usuario no guarda los cambios
    def RestoreNameIface(self):
        toolbars = self.iface.mainWindow().findChildren(QToolBar)
        for toolbar in toolbars:
            if len(self.restore) != 0:
                for key, value in self.restore.iteritems():
                    if toolbar.windowTitle() == value:
                        toolbar.setWindowTitle(key)
            else:
                return
        return

    # Creamos la barra de herramientas.
    def CreateToolBar(self, item):
        visible = DelToolBarIface(item.text(0), self.iface)
        self.bar = self.iface.mainWindow().addToolBar(item.text(0))  # La anadimos al click derecho
        self.bar.setVisible(visible)
        return

    #####################################################################################
    ################################    Save and Read    ################################
    #####################################################################################

    # We keep the model with our tools
    def SaveTools(self):
        try:
            if os.path.isfile(self.filepath):
                QFile.remove(self.file)

            self.file.open(QIODevice.WriteOnly)
            datastream = QDataStream(self.file)
            count = self.MyToolsBars.topLevelItemCount()
            datastream.writeUInt32(count)

            for i in range(0, count):
                item = self.MyToolsBars.topLevelItem(i)
                item.write(datastream)
                self.bar = None
                self.CreateToolBar(item)
                self.save_item(item, datastream)

            self.hasChanged = False
            self.file.close()
            # We restore the list of Qgis tools.
            state = self.saveWidgetState(self.ToolBars) 
            self.PopulateQgisTools()
            self.loadWidgetState(self.ToolBars, state)

            self.iface.messageBar().pushMessage("Info: ", "Save correctly.", level=QGis.Info, duration=3)
            self.rename_btn.setEnabled(False)
            self.delete_btn.setEnabled(False)
            self.restore = {}

        except Exception:
            self.iface.messageBar().pushMessage("Error: ", "Error save tools ", level=QGis.Critical, duration=3)
        return

    def save_item(self, item, datastream):

        count = item.childCount()
        datastream.writeUInt32(count)
        for i in range(0, count):
            child = item.child(i)
            child.write(datastream)
            self.bar.addAction(obtainAction(child.text(0), self.iface))
            self.save_item(child, datastream)

    # We get the list of user tools
    def listMyToolBars(self):
        self.MyToolsBars.clear()

        self.file.open(QIODevice.ReadOnly)
        datastream = QDataStream(self.file)
        num_childs = datastream.readUInt32()
        for i in range(0, num_childs):
            self.MyToolsBars.setEnabled(True)
            self.My_expand.setEnabled(True)
            self.My_Collapse.setEnabled(True)
            item = QTreeWidgetItem()
            item.read(datastream)
            self.MyToolsBars.insertTopLevelItem(i, item)
            self.restore_item(datastream, item)
        self.file.close()

    def restore_item(self, datastream, item):
        num_childs = datastream.readUInt32()
        for i in range(0, num_childs):
            child = QTreeWidgetItem()
            child.read(datastream)
            item.addChild(child) 
            self.restore_item(datastream, child)

    #####################################################################################
    ################################         End         ################################
    #####################################################################################

    # Qgis tools
    def CollapseQgis(self):
        self.ToolBars.collapseAll()
        return

    def ExpandQgis(self):
        self.ToolBars.expandAll()
        return

    # User tools
    def CollapseMyTools(self):
        self.MyToolsBars.collapseAll()
        return

    def ExpandMyTools(self):
        self.MyToolsBars.expandAll()
        return

    # Restauramos el estado del listado de herramientas de Qgis cada vez que lo actualizamos
    # (Guardado)
    def saveWidgetState(self, displayWidget):
        expandedIndexes = {}
        count = displayWidget.topLevelItemCount()
        for i in range(0, count):
            item = displayWidget.topLevelItem(i)
            expandedItem = item.isExpanded()
            expandedIndexes.update({i: expandedItem})
        return expandedIndexes

    def loadWidgetState(self, displayWidget, expandedIndexes):
        count = displayWidget.topLevelItemCount()
        for i in range(0, count):
            item = displayWidget.topLevelItem(i)
            try:
                item.setExpanded(expandedIndexes[i])
            except Exception:
                None
        return

    # Close Event
    def closeEvent(self, evt):
        if self.hasChanged:
            ret = QMessageBox.question(self, 'Save',
                    'There are unsaved changes in the model. Save changes?',
                    QMessageBox.Yes | 
                    QMessageBox.No | 
                    QMessageBox.Cancel,
                    QMessageBox.Yes)
            if ret == QMessageBox.Yes:
                self.SaveTools()
                evt.accept()
            if ret == QMessageBox.No:
                self.RestoreNameIface()
                try:
                    self.listMyToolBars()  # User Tools
                except Exception:
                    self.iface.messageBar().pushMessage("Error: ",
                                                        "Error loading Custom Toolbars",
                                                        level=QGis.Critical,
                                                        duration=3)
                    None
                evt.accept()
            if ret == QMessageBox.Cancel:
                evt.ignore()
        else:
            evt.accept()
