# -*- coding: utf-8 -*-
import sys

try:
    sys.path.append(
        "D:\eclipse\plugins\org.python.pydev.core_7.0.3.201811082356\pysrc")
    from pydevd import *
except ImportError:
    None


def classFactory(iface):
    from .CustomToolbar import CustomToolbar
    return CustomToolbar(iface)
