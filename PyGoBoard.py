#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
---------------------------------
-----------PyGoBoard-------------
---------------------------------
Version 0.21
By Pablo Soifer -Draculinio-
stackpointerex@gmail.com

"""

import wx
import os

from principal import *

#-------------------------------------------------
#---------------------MAIN------------------------
#-------------------------------------------------

if __name__ == '__main__':
    app = wx.App()
    #principalD.Principal(None, 'PyGoBoard')
    Principal(None, 'PyGoBoard')
    app.MainLoop()