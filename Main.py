# -*- coding: utf-8 -*-
'''
Created on 2013-6-15

@author: Anderson
'''
import sys
from PyQt4 import QtGui
from MainWindowRaw import Ui_MainWindow
from MyItem import MyItem

class   MyMainWindow(Ui_MainWindow):
    
    def __init__(self,parent=None):
        super(MyMainWindow, self).__init__()
        #QtGui.QMainWindow.__init__(self,parent)
        self.ui = Ui_MainWindow(self)
        self.ui.setupUi(self)
        
        self.Scene = QtGui.QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.Scene)
        self.setupItem()
        self.ui.pushButton_generate.clicked.connect(self.generate)
        self.ui.pushButton.clicked.connect(self.clear)
    
    def setupItem(self):
        self.itemList = []
        for i in range(0,8):
            for j in range(0,8):                
                tmpItem = MyItem(QtGui.QPixmap("empty.jpg"))
                tmpItem.setPos(j*25,i*25)
                tmpItem.setScale(0.5)
                self.Scene.addItem(tmpItem)
                self.itemList.append(tmpItem)
    
    def generate(self):
        str = "const int LED[8][8]={\n"
        for i in range(0,len(self.itemList)):
            tmpItem = self.itemList[i]
            flag = tmpItem.isEmpty
            if flag:
                str = str + "0,"
            else:
                str = str + "1,"
            if (i+1)%8 == 0:
                str = str + "\n"
        
        str = str + "};"
        
        self.ui.textEdit.setText(str)
    
    def copy(self):
        ''''''
    
    def clear(self):
        for i in range(0,len(self.itemList)):
            tmpItem = self.itemList[i]
            tmpItem.isEmpty = True
            tmpItem.setPixmap(QtGui.QPixmap("empty.jpg"))
                

app = QtGui.QApplication(sys.argv)
widget = MyMainWindow()
widget.show()
sys.exit(app.exec_())