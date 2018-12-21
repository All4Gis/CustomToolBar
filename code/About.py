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
from qgis.gui import QgsMessageBar
import subprocess
import sys

from PyQt5.QtWidgets import QDialog

from CustomToolBar.gui.About import Ui_About

try:
    from pydevd import *
except ImportError:
    None


class AboutDialog(QDialog, Ui_About):

    def __init__(self, iface):
        QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.video = os.path.dirname(__file__) + '//example//ExampleUse.mp4'

    # Video de ejemplo
    def ShowVideo(self):
        if os.path.exists(self.video):

            if sys.platform.startswith('dar'):
                subprocess.call(['open', self.video])
            elif sys.platform.startswith('lin'):
                subprocess.call(['xdg-open', self.video])
            elif sys.platform.startswith('win'):
                os.startfile(self.video)
            else:
                pass

        else:
            self.iface.messageBar().pushMessage("Error: ", "Could not open video file: " + self.video, level=QgsMessageBar.CRITICAL, duration=3) 
            return
