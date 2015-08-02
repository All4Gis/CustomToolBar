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
from qgis.utils import loadPlugin, startPlugin 


try:
    from processing.core.Processing import Processing
    from processing.gui.AlgorithmDialog import AlgorithmDialog
    from processing.gui.MessageDialog import MessageDialog
    import sys
    from pydevd import *
except:
    None
    

class CustomToolbar:

    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'CustomToolbar_{}.qm'.format(locale))
 
        self.userhome = os.path.expanduser('~')
        self.filepath = self.userhome + '\.CustomToolBars'
        self.file = QFile(self.filepath)
 
        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
                
        # Activamos las herramientas creadas.
        try:
            loadPlugin('processing')
            startPlugin('processing')
        except:
            self.iface.messageBar().pushMessage("Error: ", "Error loading Processing Toolbox.", level=QgsMessageBar.CRITICAL, duration=3)
            None 
            
        try:
            self.MyToolBars()
        except:
            self.iface.messageBar().pushMessage("Error: ", "Error loading tools ", level=QgsMessageBar.CRITICAL, duration=3)
            None 

    def initGui(self):
        self.action = QAction(QIcon(":/img/images/icon.png"), u"Custom ToolBar", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Custom ToolBar", self.action)
       
        self.actionAbout = QAction(QIcon(":/img/images/info.png"), u"About", self.iface.mainWindow())
        self.iface.addPluginToMenu(u"&Custom ToolBar", self.actionAbout)
        self.actionAbout.triggered.connect(self.About)


    def unload(self):
        self.iface.removePluginMenu(u"&Custom ToolBar", self.action)
        self.iface.removePluginMenu(u"&Custom ToolBar", self.actionAbout)
        self.iface.removeToolBarIcon(self.action)

    def About(self):
        self.About = AboutDialog(self.iface)
        self.About.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint) 
        self.About.exec_()
        return
    
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
            self.DelToolBarIface(item.text(0))
            self.bar = self.iface.mainWindow().addToolBar(item.text(0))
            self.restore_item(datastream, item)
            
        self.file.close()
        return 

    def restore_item(self, datastream, item):
        num_childs = datastream.readUInt32()
        for i in range(0, num_childs):
            child = QtGui.QTreeWidgetItem()
            child.read(datastream)
            self.bar.addAction(self.obtainAction(child.text(0)))  
            self.restore_item(datastream, child)
        
    # Metodo para obtener la accion del boton y anadirla a la barra nueva
    def obtainAction(self, value):
        # Barras de herramientas de Qgis
        toolbars = self.iface.mainWindow().findChildren(QToolBar)
        for toolbar in toolbars:
            actions = toolbar.actions() 
            for action in actions:
                if isinstance(action, QWidgetAction):
                    a = action.defaultWidget().actions()
                    for b in a:
                        if b.iconText() == value:
                            return b
                else:
                    if action.iconText() == value:
                        return action
         
        # Obtencion de la herramienta en el listado de geoprocesos.
        try:
            for providerName in Processing.algs.keys():
                provider = Processing.algs[providerName]               
                algs = provider.values()
                for alg in algs:
                    if value == alg.name:
                        action = QAction(QIcon(alg.getIcon()), alg.name, self.iface.mainWindow())
                        action.triggered.connect(lambda:self.executeAlgorithm(alg.name))
                        return action  
            return  
        except:
            self.iface.messageBar().pushMessage("Error: ", "Error loading Processing Toolbox.", level=QgsMessageBar.CRITICAL, duration=3)  
            return

    def executeAlgorithm(self, value):
        
        for providerName in Processing.algs.keys():
            provider = Processing.algs[providerName]               
            algs = provider.values()
            for alg in algs:
                if value == alg.name:
                    try:
                        alg = Processing.getAlgorithm(alg.commandLineName())
                        message = alg.checkBeforeOpeningParametersDialog()
                    except:
                        self.iface.messageBar().pushMessage("Error: ", "Error loading Processing Algorithm.", level=QgsMessageBar.CRITICAL, duration=3)  
                        return
                    if message:
                        dlg = MessageDialog()
                        dlg.setTitle(self.tr('Missing dependency'))
                        dlg.setMessage(self.tr('<h3>Missing dependency. This algorithm cannot '
                                        'be run :-( </h3>\n%s') % message)
                        dlg.exec_()
                        return
                    alg = alg.getCopy()
                    dlg = alg.getCustomParametersDialog()
                    if not dlg:
                        try:
                            dlg = AlgorithmDialog(alg)
                        except:
                            self.iface.messageBar().pushMessage("Info: ", "Error loading Processing Algorithm.", level=QgsMessageBar.INFO, duration=3)  
                            return
                    canvas = self.iface.mapCanvas()
                    prevMapTool = canvas.mapTool()
                    dlg.show()
                    dlg.exec_()
                    if canvas.mapTool() != prevMapTool:
                        try:
                            canvas.mapTool().reset()
                        except:
                            pass
                        canvas.setMapTool(prevMapTool)
        return
    # Borramos la herramienta
    def DelToolBarIface(self, value):
        toolbars = self.iface.mainWindow().findChildren(QToolBar)
        for toolbar in toolbars:
            if toolbar.windowTitle() == value:
                self.iface.mainWindow().removeToolBar(toolbar)
                self.iface.mainWindow().update()
                toolbar.setParent(None)
        return
