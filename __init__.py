# -*- coding: utf-8 -*-
import os
import site
import sys


try:
    sys.path.append("C:/eclipse/plugins/org.python.pydev_4.2.0.201507041133/pysrc")
    #sys.path.append("C:/eclipse/plugins/org.python.pydev_3.6.0.201406232321/pysrc")
except:
    None
    
def classFactory(iface):
    from CustomToolbar import CustomToolbar
    return CustomToolbar(iface)
