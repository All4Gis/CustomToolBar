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

from About import AboutDialog
from CustomToolbarDialog import CustomToolbarDialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtGui import QToolBar, QToolButton, QWidgetAction
import gui.generated.resources_rc
from qgis.core import *
from qgis.gui import QgsMessageBar
from utils.utils import *

try:
    import sys
    from pydevd import *
except:
    None
    

class CustomToolbar:

    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value("locale//userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'CustomToolbar_{}.qm'.format(locale))
        self.userhome = os.path.expanduser('~')
        self.filepath = self.plugin_dir + '//.CustomToolBars'
        self.file = QFile(self.filepath)
        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
         
        #Activamos los plugins para evitar que falle al activar las herramientas    
        try:   
            ActivatePlugins(self.iface)
        except:
            self.iface.messageBar().pushMessage("Error: ", "Error activate plugins ", level=QgsMessageBar.CRITICAL, duration=3)
            None 
        #Activamos las herramientas del usuario    
        try:
            self.MyToolBars()
        except:
            self.iface.messageBar().pushMessage("Error: ", "Error loading tools ", level=QgsMessageBar.CRITICAL, duration=3)
            None 

    def initGui(self):
        self.action = QAction(QIcon(":/img/images/icon.png"), u"Customize ToolBars", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Customize ToolBars", self.action)
       
        self.actionAbout = QAction(QIcon(":/img/images/info.png"), u"About", self.iface.mainWindow())
        self.iface.addPluginToMenu(u"&Customize ToolBars", self.actionAbout)
        self.actionAbout.triggered.connect(self.About)


    def unload(self):
        self.iface.removePluginMenu(u"&Customize ToolBars", self.action)
        self.iface.removePluginMenu(u"&Customize ToolBars", self.actionAbout)
        self.iface.removeToolBarIcon(self.action)

    def About(self):
        self.About = AboutDialog(self.iface)
        #self.About.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint) 
        self.About.exec_()
    
    def run(self):
        self.dlg = CustomToolbarDialog(self.iface)
        self.dlg.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint) 
        self.dlg.exec_()
    
      
    # Creamos las toolbar al iniciar Qgis  
    
    def MyToolBars(self):
 
        self.file.open(QtCore.QIODevice.ReadOnly)         
        datastream = QtCore.QDataStream(self.file)
        num_childs = datastream.readUInt32()  
        for i in range(0, num_childs):
            item = QtGui.QTreeWidgetItem()
            item.read(datastream)
            self.bar = None
            DelToolBarIface(item.text(0),self.iface)
            self.bar = self.iface.mainWindow().addToolBar(item.text(0))
            self.restore_item(datastream, item)
            
        self.file.close()
        return 

    def restore_item(self, datastream, item):
        num_childs = datastream.readUInt32()
        for i in range(0, num_childs):
            child = QtGui.QTreeWidgetItem()
            child.read(datastream)
            self.bar.addAction(obtainAction(child.text(0),self.iface))  
            self.restore_item(datastream, child)
 
