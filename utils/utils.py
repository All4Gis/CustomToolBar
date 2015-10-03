# -*- coding: utf-8 -*- 
import os.path

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtGui import QToolBar, QToolButton, QWidgetAction
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

# Creamos las toolbar al iniciar Qgis  

def MyToolBars(iface):
 
    userhome = os.path.expanduser('~')
    filepath = userhome + '\.CustomToolBars'
    file = QFile(filepath)

    file.open(QtCore.QIODevice.ReadOnly)         
    datastream = QtCore.QDataStream(file)
    num_childs = datastream.readUInt32()  
    for i in range(0, num_childs):
        item = QtGui.QTreeWidgetItem()
        item.read(datastream)
        bar = None
        DelToolBarIface(item.text(0), iface)
        bar = iface.mainWindow().addToolBar(item.text(0))
        restore_item(datastream, item, bar, iface)
        
    file.close()
    return 

def restore_item(datastream, item, bar, iface):
    num_childs = datastream.readUInt32()
    for i in range(0, num_childs):
        child = QtGui.QTreeWidgetItem()
        child.read(datastream)
        bar.addAction(obtainAction(child.text(0), iface))  
        restore_item(datastream, child, bar, iface)
    
# Metodo para obtener la accion del boton y anadirla a la barra nueva
def obtainAction(value, iface):
    # Barras de herramientas de Qgis
    toolbars = iface.mainWindow().findChildren(QToolBar)
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

    # Acciones de los menus
    menubar = iface.mainWindow().menuBar()
 
    for action in menubar.actions():
        if action.menu():
            for action in action.menu().actions():
                if action.menu():
                    for actions in action.menu().actions():
                        if actions.iconText() == value:
                            return actions  
                else:  
                    if action.iconText() == value:
                        return action 
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
                    action = QAction(QIcon(alg.getIcon()), alg.name, iface.mainWindow())
                    action.triggered.connect(lambda:executeAlgorithm(alg.name, iface))
                    return action  
        return  
    except:
        iface.messageBar().pushMessage("Error: ", "Error loading Processing Toolbox.", level=QgsMessageBar.CRITICAL, duration=3)  
        return

def executeAlgorithm(value, iface):
    
    for providerName in Processing.algs.keys():
        provider = Processing.algs[providerName]               
        algs = provider.values()
        for alg in algs:
            if value == alg.name:
                try:
                    alg = Processing.getAlgorithm(alg.commandLineName())
                    message = alg.checkBeforeOpeningParametersDialog()
                except:
                    iface.messageBar().pushMessage("Error: ", "Error loading Processing Algorithm.", level=QgsMessageBar.CRITICAL, duration=3)  
                    return
                if message:
                    dlg = MessageDialog()
                    dlg.setTitle(tr('Missing dependency'))
                    dlg.setMessage(tr('<h3>Missing dependency. This algorithm cannot '
                                    'be run :-( </h3>\n%s') % message)
                    dlg.exec_()
                    return
                alg = alg.getCopy()
                dlg = alg.getCustomParametersDialog()
                if not dlg:
                    try:
                        dlg = AlgorithmDialog(alg)
                    except:
                        iface.messageBar().pushMessage("Info: ", "Error loading Processing Algorithm.", level=QgsMessageBar.INFO, duration=3)  
                        return
                canvas = iface.mapCanvas()
                prevMapTool = canvas.mapTool()
                dlg.exec_()
                if canvas.mapTool() != prevMapTool:
                    try:
                        canvas.mapTool().reset()
                    except:
                        pass
                    canvas.setMapTool(prevMapTool)
    return



# Borramos la herramienta
def DelToolBarIface(value, iface):
    toolbars = iface.mainWindow().findChildren(QToolBar)
    for toolbar in toolbars:
        if toolbar.windowTitle() == value:
            iface.mainWindow().removeToolBar(toolbar)
            iface.mainWindow().update()
            toolbar.setParent(None)
    return
