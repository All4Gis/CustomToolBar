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

from PyQt5.QtCore import QFile, QDataStream, QIODevice, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QTreeWidgetItem

from CustomToolBar.About import AboutDialog
from CustomToolBar.CustomToolbarDialog import CustomToolbarDialog
from CustomToolBar.utils.utils import ActivatePlugins, DelToolBarIface, obtainAction

try:
    from pydevd import *
except ImportError:
    None


class CustomToolbar:

    def __init__(self, iface):
        self.iface = iface
        self.userhome = os.path.expanduser('~')
        self.filepath = self.userhome + '//.CustomToolBars'
        self.file = QFile(self.filepath)
        # Activamos los plugins para evitar que falle al activar las herramientas
        try:
            ActivatePlugins()
        except Exception:
            self.iface.messageBar().pushMessage("Error: ", " Error activate plugins", level=QGis.Critical, duration=3)
            None
        # We activate the user's tools
        try:
            self.MyToolBars()
        except Exception:
            self.iface.messageBar().pushMessage("Error: ", " Error loading Custom Toolbars", level=QGis.Critical, duration=3)
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
        self.About.exec_()

    def run(self):
        self.dlg = CustomToolbarDialog(self.iface)
        self.dlg.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)
        self.dlg.exec_()

    def MyToolBars(self):
        ''' Create user toolbars '''
        self.file.open(QIODevice.ReadOnly)
        datastream = QDataStream(self.file)
        num_childs = datastream.readUInt32()
        for _ in range(0, num_childs):
            item = QTreeWidgetItem()
            item.read(datastream)
            self.bar = None
            DelToolBarIface(item.text(0), self.iface)
            self.bar = self.iface.mainWindow().addToolBar(item.text(0))
            self.restore_item(datastream, item)

        self.file.close()
        return

    def restore_item(self, datastream, _):
        num_childs = datastream.readUInt32()
        for _ in range(0, num_childs):
            child = QTreeWidgetItem()
            child.read(datastream)
            self.bar.addAction(obtainAction(child.text(0), self.iface))
            self.restore_item(datastream, child)
