# -*- coding: utf-8 -*- 
from qgis.core import Qgis as QGis
from qgis.core import QgsApplication
from qgis.utils import loadPlugin, startPlugin, available_plugins, \
    isPluginLoaded

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QToolBar, QWidgetAction, QAction

try:
    from processing.gui.AlgorithmDialog import AlgorithmDialog
    from pydevd import *
except ImportError:
    None


def ActivatePlugins():
    ''' Loading the plugins (we avoid errors).'''
    for plugin in available_plugins:
        if not isPluginLoaded(plugin) and plugin != 'CustomToolBar':
            try:
                loadPlugin(plugin)
                startPlugin(plugin)
            except Exception:
                pass
    return


# Method to obtain the action of the button and add it to the new bar
def obtainAction(value, iface):
    # Qgis toolbars
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

    # Menus
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

    # Processing.
    try:
        for alg in QgsApplication.processingRegistry().algorithms():
            if value == alg.displayName():
                action = QAction(QIcon(alg.icon()),
                                 alg.displayName(),
                                 iface.mainWindow())
                action.triggered.connect(lambda: executeAlgorithm(alg.name(),
                                                                  iface))
                return action
        return
    except Exception:
        iface.messageBar().pushMessage("Error: ",
                                       "Error loading Processing Toolbox.",
                                       level=QGis.Critical, duration=3)
        return


# TODO : QGIS CRASH
def executeAlgorithm(value, iface):
    for alg in QgsApplication.processingRegistry().algorithms():
        if value == alg.name():
            try:
                dlg = AlgorithmDialog(alg)
            except Exception:
                iface.messageBar().pushMessage("Info: ", "Error loading Processing Algorithm.", level=QGis.Info, duration=3)  
                return
            dlg.exec_()
    return


# Remove ToolBar
def DelToolBarIface(value, iface):
    toolbars = iface.mainWindow().findChildren(QToolBar)
    for toolbar in toolbars:
        if toolbar.windowTitle() == value:
            visible = toolbar.isVisible()
            iface.mainWindow().removeToolBar(toolbar)
            iface.mainWindow().update()
            toolbar.setParent(None)
            return visible

    return True
