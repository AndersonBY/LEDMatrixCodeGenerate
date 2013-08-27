# -*- coding: utf-8 -*-
'''
Created on 2013-6-16

@author: Anderson
'''
from PyQt4 import QtCore, QtGui

class MyItem(QtGui.QGraphicsPixmapItem):
    '''
    classdocs
    '''


    def __init__(self, pixmap, parent=None, scene=None):
        '''
        Constructor
        '''
        QtGui.QGraphicsPixmapItem.__init__(self, pixmap, parent=None, scene=None)
        self.isEmpty = True
        self.pixmapEmpty = QtGui.QPixmap("empty.jpg")
        self.pixmapFull  = QtGui.QPixmap("full.jpg")
    
    def mousePressEvent(self, event):
        super(MyItem, self).mousePressEvent(event)
        if self.isEmpty:
            self.setPixmap(self.pixmapFull)
            self.isEmpty = False
        else:
            self.setPixmap(self.pixmapEmpty)
            self.isEmpty = True
        