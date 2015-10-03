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
import subprocess

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui.generated.About import Ui_About
from qgis.core import *
from qgis.gui import *
from qgis.gui import QgsMessageBar


try:
    import sys
    from pydevd import *
except:
    None
 
class AboutDialog(QtGui.QDialog, Ui_About):
    def __init__(self, iface):      
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__) 
        self.video = self.plugin_dir + '//example//ExampleUse.mp4'
    
    # Video de ejemplo
    def ShowVideo(self): 
        if os.path.exists(self.video):
             
            if sys.platform.startswith('dar'):
                subprocess.call(['open', self.video])
            elif sys.platform.startswith('lin'):
                subprocess.call(['xdg-open', self.video])
            elif sys.platform.startswith('win'):
                #subprocess.call([self.video])
                os.startfile(self.video)
            else:   
                pass
             
        else:
            self.iface.messageBar().pushMessage("Error: ", "Could not open video file: " + self.video, level=QgsMessageBar.CRITICAL, duration=3) 
            return
