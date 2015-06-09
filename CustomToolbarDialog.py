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
import os
import os.path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtCore import QCoreApplication
from PyQt4.QtCore import QFile
from PyQt4.QtGui import *
from PyQt4.QtGui import QToolBar
import sip
 
from qgis.utils import reloadPlugin,loadPlugin, startPlugin
from About import AboutDialog
from gui.generated.ui_CustomToolbar import Ui_CustomToolbarDialog
from qgis.core import *
from qgis.gui import *
from qgis.gui import QgsMessageBar
 
try:
    import sys
    from pydevd import *
except:
    None
 
 
class CustomToolbarDialog(QtGui.QDialog, Ui_CustomToolbarDialog):
    
    def __init__(self, iface=None):      
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.hasChanged = False    
        self.userhome = os.path.expanduser('~')
        self.filepath=self.userhome + '\.CustomToolBars'
        self.file = QFile(self.filepath)
 
 
        self.AddHelpButton()# Boton de ayuda
  
        try:
            self.listMyToolBars()# Herramientas Usuario
        
        except Exception as e:
            self.iface.messageBar().pushMessage("Error: ", "Error loading tools ", level=QgsMessageBar.CRITICAL, duration=3)
            raise 
 
        self.PopulateQgisTools()# Herramientas Qgis
 
        # Drop listado usuario  
        def dropEvent(event):
            self.hasChanged = True
            destinationItem=self.MyToolsBars.itemAt(event.pos()) 
            if destinationItem is None: 
                return  
            depth = self.depth(destinationItem)    
 
            if depth<=2 :
                if destinationItem.text(0)=="":
                    self.iface.messageBar().pushMessage("Info: ", "You must add the button into a tool.", level=QgsMessageBar.INFO, duration=3)       
                    return      
                SelectedItem=self.MyToolsBars.currentItem()
                if SelectedItem  is not None:
                    if self.depth(SelectedItem)==1:
                        self.iface.messageBar().pushMessage("Info: ", "You can not put a tool into another.", level=QgsMessageBar.INFO, duration=3)       
                        return 
                       
                    SelectedItem_Parent = SelectedItem.parent()
                    destinationItem_Parent= destinationItem.parent()
                    if destinationItem_Parent is None:
                        SelectedItem_index = SelectedItem_Parent.indexOfChild(SelectedItem)
                        child = SelectedItem_Parent.takeChild(SelectedItem_index)
                        destinationItem.insertChild(0,SelectedItem)
                   
                    else:
                        SelectedItem_index = SelectedItem_Parent.indexOfChild(SelectedItem)
                        destinationItem_index = destinationItem_Parent.indexOfChild(destinationItem)
                        child = SelectedItem_Parent.child(SelectedItem_index)
                        destinationItem_Parent.insertChild(destinationItem_index+1, child.clone())
                        
                        if SelectedItem_Parent !=  destinationItem_Parent:    
                            SelectedItem_Parent.takeChild(SelectedItem_index) 
                        else: 
                            #Movimiento de arriba abajo
                            if SelectedItem_index< destinationItem_index:
                                SelectedItem_Parent.takeChild(SelectedItem_index)
                            else:
                            #Movimiento de abajo arriba
                                SelectedItem_Parent.takeChild(SelectedItem_index+1)                    
       
                    return
         
                else:
                    if self.depth(destinationItem) ==1:
                        SelectedItem=self.ToolBars.currentItem()
                        destinationItem.insertChild(0,SelectedItem.clone())
                    if self.depth(destinationItem) ==2:                        
                        SelectedItem=self.ToolBars.currentItem()
                        SelectedItem_Parent = SelectedItem.parent()
                        SelectedItem_index = SelectedItem_Parent.indexOfChild(SelectedItem)
                        destinationItem_Parent= destinationItem.parent()
                        destinationItem_index = destinationItem_Parent.indexOfChild(destinationItem)
                        child = SelectedItem_Parent.child(SelectedItem_index)
                        destinationItem_Parent.insertChild(destinationItem_index+1, child.clone())
 
            else:
                return
            
            self.MyToolsBars.setCurrentItem(None)
            event.acceptProposedAction()
            
        self.MyToolsBars.dropEvent = dropEvent
        
 
    #Obtenemos la profuncidad del item en el arbol
    def depth(self, item):
        depth = 0
        while item is not None:
            item = item.parent()
            depth += 1
        return depth
    
    # Dialogo de ayuda
    def about(self):
        self.About = AboutDialog(self.iface)
        self.About.show()
        self.About.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint) 
        self.About.exec_()
        return
    
    def AddHelpButton(self):
        layout = QVBoxLayout()
        toolBar = QToolBar(self)
        toolBar.addAction(u"Help", self.about)
        toolBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        toolBar.setStyleSheet("QToolBar {border-bottom: 0px solid grey }")
        toolBar.setInputMethodHints(QtCore.Qt.ImhNone)
        toolBar.setMovable(False)
        toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        toolBar.setFloatable(False)
        layout.addWidget(toolBar)
        layout.setMargin(0)
        layout.setSpacing(0)
        layout.addStretch(0)
        self.setLayout(layout)
        return
        
    # Obtenemos las toolbars de qgis
    def PopulateQgisTools(self):
        self.ToolBars.clear()
        toolbars = self.iface.mainWindow().findChildren(QToolBar)
        for toolbar in toolbars:
            a = 0 
            pitems = QtGui.QTreeWidgetItem(self.ToolBars)
            if toolbar.windowTitle() == '':
                pitems.setText(0, "No Name")
            else:   
                pitems.setText(0, toolbar.windowTitle())
            Buttons = toolbar.findChildren(QToolButton)
            for Button in Buttons:
                # Eliminamos el primer caracter que no es un boton como tal
                if a != 0:
                    citems = QtGui.QTreeWidgetItem(pitems)
                    citems.setIcon(0, Button.icon())
                    citems.setText(0, Button.text())
                a += 1
        return  
 
    # Gestion de clicks en el listado de herramientas de Qgis.Solo se permite mover las herramientas,no las toolbar
    def QgisToolsClick(self):
        item = self.ToolBars.currentItem()
        parent = item.parent()
        self.MyToolsBars.setCurrentItem(None)
        
        if parent is None:
            self.ToolBars.setDragEnabled(False)
        else:
            self.ToolBars.setDragEnabled(True)
        return  
    
    # listado de herramientas del usuario
    def MyToolsClick(self, column):
        selected=self.MyToolsBars.currentItem()
        if selected is not None:
            parent = self.MyToolsBars.currentItem().parent()               
            if parent is not None:
                self.rename_btn.setEnabled(False)
                self.delete_btn.setEnabled(True)    
            else:
                self.rename_btn.setEnabled(True)
                self.delete_btn.setEnabled(True)
     
        return
    
    # Creamos una nueva ToolBar         
    def NewToolBar(self):
        flags = Qt.WindowSystemMenuHint | Qt.WindowTitleHint
        text, ok = QInputDialog.getText(self, 'ToolBar Name', 'Enter new Toolbar name.', flags=flags)
        if text=="":
            self.iface.messageBar().pushMessage("Error: ", "Enter Toolbar name.", level=QgsMessageBar.CRITICAL, duration=3) 
            return   
        if ok:
            new_toolbar = QtGui.QTreeWidgetItem()
            new_toolbar.setText(0, text)
            self.MyToolsBars.invisibleRootItem().addChild(new_toolbar)
            self.MyToolsBars.setEnabled(True)
            self.hasChanged = True
        return
 
    # Renombramos solo el nombre de la ToolBar     
    def RenameToolBar(self):
        flags = Qt.WindowSystemMenuHint | Qt.WindowTitleHint
        text, ok = QInputDialog.getText(self, 'ToolBar Name', 'Enter new Toolbar name.', flags=flags)
        if text=="":
            self.iface.messageBar().pushMessage("Error: ", "Enter Toolbar name.", level=QgsMessageBar.CRITICAL, duration=3) 
            return     
        if ok:
            item = self.MyToolsBars.currentItem()
            text_old= item.text(self.MyToolsBars.currentColumn())
 
            #Renombramos la barra de herramientas en el iface
            toolbars = self.iface.mainWindow().findChildren(QToolBar)
            for toolbar in toolbars:
                if toolbar.windowTitle() == text_old:
                    toolbar.setWindowTitle(text) 
                    
            item.setText(self.MyToolsBars.currentColumn(), text)
            self.hasChanged = True
        return
 
    # Borramos TODA la toolbar o la herramienta seleccionada    
    def DeleteToolBar(self):
        text= self.MyToolsBars.currentItem().text(0)
        reply = QtGui.QMessageBox.question(self, "Delete ToolBar", "Sure you want to delete '" + text + "' ?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            root = self.MyToolsBars.invisibleRootItem()
            for item in self.MyToolsBars.selectedItems():
                (item.parent() or root).removeChild(item)

            if self.rename_btn.isEnabled():
                self.DelToolBarIface(text) #Borramos la barra de herramientas
                self.PopulateQgisTools()#Recargamos la lista de herramientas.
                
            num_chils = root.childCount()
            if num_chils == 0:
                self.MyToolsBars.setEnabled(False)
                self.rename_btn.setEnabled(False)
                self.delete_btn.setEnabled(False)
                self.hasChanged = True

        return
 
    
    #Borramos la herramienta
    def DelToolBarIface(self,value):
        toolbars = self.iface.mainWindow().findChildren(QToolBar)
        for toolbar in toolbars:
            if toolbar.windowTitle() == value:
                self.iface.mainWindow().removeToolBar( toolbar)
                self.iface.mainWindow().update()
                toolbar.setParent(None)
        return

        
    # Creamos la barra de herramientas.
    def CreateToolBar(self, item):
        self.DelToolBarIface(item.text(0))      
        self.bar = self.iface.mainWindow().addToolBar(item.text(0))
        return  
        
 
    # Metodo para obtener la accion del boton y anadirla a la barra nueva
    def obtainAction(self, value):
        toolbars = self.iface.mainWindow().findChildren(QToolBar)
        for toolbar in toolbars:
            Buttons = toolbar.findChildren(QToolButton)
            for Button in Buttons:
                if Button.text() == value:
                    action = Button.defaultAction()
                    return action
        return  
    
    
    #####################################################################################
    ################################    Save and Read    ################################
    #####################################################################################
    
    # Guardamos el modelo con nuestras herramientas
    def SaveTools(self):
        try:
            if os.path.isfile(self.filepath):
                QFile.remove(self.file) 
                      
            self.file.open(QtCore.QIODevice.WriteOnly)
            datastream = QtCore.QDataStream(self.file)
            count=self.MyToolsBars.topLevelItemCount()
            datastream.writeUInt32(count)
             
            for i in range(0, count):
                item=self.MyToolsBars.topLevelItem(i) 
                item.write(datastream)
                self.bar=None
                self.CreateToolBar(item)
                self.save_item(item, datastream )
 
            self.hasChanged = False
            self.iface.messageBar().pushMessage("Info: ", "Save correctly.", level=QgsMessageBar.INFO, duration=3)   
            self.PopulateQgisTools()
            self.file.close()
                                               
        except:
            self.iface.messageBar().pushMessage("Error: ", "Error save tools ", level=QgsMessageBar.CRITICAL, duration=3) 
        return
    
    def save_item(self, item, datastream ):
        
        count = item.childCount()
        datastream.writeUInt32(count)
        for i in range(0, count):
            child =  item.child(i)
            child.write(datastream)
            self.bar.addAction(self.obtainAction(child.text(0)))  
            self.save_item(child, datastream )
            
 
    # Obtenemos la lista de herramientas del usuario
    def listMyToolBars(self):
        self.file.open(QtCore.QIODevice.ReadOnly)         
        datastream = QtCore.QDataStream(self.file)
        num_childs = datastream.readUInt32()
        for i in range(0, num_childs):
            self.MyToolsBars.setEnabled(True)
            item=QtGui.QTreeWidgetItem()
            item.read(datastream)
            self.MyToolsBars.insertTopLevelItem(i, item)
            self.restore_item(datastream, item)
        self.file.close()
 
 
    def restore_item(self, datastream, item):
        num_childs = datastream.readUInt32()
        for i in range(0, num_childs):
            child=QtGui.QTreeWidgetItem()
            child.read(datastream)
            item.addChild(child) 
            self.restore_item(datastream, child)
    
    #####################################################################################
    ################################         End         ################################
    #####################################################################################
    
        
    # Evento cerrar dialogo
    def closeEvent(self, evt):
        if self.hasChanged:
            ret = QMessageBox.question(self, self.tr('Save'),
                    self.tr('There are unsaved changes in the model. Save changes?'),
                    QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Yes)
            if ret == QMessageBox.Yes:
                self.SaveTools()
                evt.accept()    
            if ret == QMessageBox.No:
                evt.accept()
            if ret == QMessageBox.Cancel:
                evt.ignore()
        else:
            evt.accept()
