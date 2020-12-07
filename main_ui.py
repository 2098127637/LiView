import requests


import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
	QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QCoreApplication

class AppLiView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300, 1017, 712)
        self.setWindowTitle('LiView')
        self.setWindowIcon(QIcon('img\\icon.jpg'))
        '''palette = QtGui.QPalette()
        self.autoFillBackground = True
        pix = QtGui.QPixmap("img//background.jpg")
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pix))
        self.setPalette(palette)'''
        '''
                滚动条
        '''
        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(250, 5000)  #######设置滚动条的尺寸
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topFiller)

        self.gridlayoutT = QGridLayout()
        self.scroll.setLayout(self.gridlayoutT)

        res = self.img()
        a=0
        x=0
        y=0
        for i in res:
            if a%5 == 0 and a!=0:
                y=y+1
                x=0
            exec('img%s = QImage.fromData(i.content)'%a)
            exec('self.Lab%s = QLabel(self)'%a)
            exec('self.Lab%s.setPixmap(QPixmap.fromImage(img%s))'%(a,a))
            exec('self.Lab%s.setScaledContents (True)  # 让图片自适应label大小'%a)
            exec('self.gridlayoutT.addWidget(self.Lab%s,%s,%s)'%(a,y,x))
            exec('self.Lab%s.setMaximumSize(189,272)'%a)
            exec('self.Lab%s.setMinimumSize(90,170)' % a)
            print(str(y) + ',' + str(x))
            x=x+1
            a=a+1


        #self.setLayout(self.scroll)

        '''exec('self.l10.resize(1600,1200)')'''


        '''self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        self.setLayout(self.vbox)'''

        self.gridlayoutB = QGridLayout()
        self.gridlayoutB.addWidget(self.scroll)
        self.setLayout(self.gridlayoutB)
        '''exec('self.grid_layout.addWidget(l10, 4, 1)')'''
        #exec('grid_layout.addWidget(, 2, 2)')


        self.show()

    def img(self):
        import requests
        s = requests.Session()
        req=[]
        '''req0 = requests.get('https://www.xuanshu.com/tupian/69/69551/69551s.jpg')
        req1 = requests.get('https://www.xuanshu.com/tupian/51/51518/51518s.jpg')
        req2 = requests.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req3 = requests.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req4 = requests.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req5 = requests.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req6 = requests.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req7 = requests.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req8 = requests.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req9 = requests.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req10 = requests.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req11= requests.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')'''

        req0 = s.get('https://www.xuanshu.com/tupian/69/69551/69551s.jpg')
        req1 = s.get('https://www.xuanshu.com/tupian/51/51518/51518s.jpg')
        req2 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req3 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req4 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req5 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req6 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req7 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req8 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req9 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req10 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req11 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req12 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req13 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req14 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req15 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req16 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req17 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req18 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req19 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req20 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req21 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req22 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req23 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req24 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req25 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req26 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')
        req27 = s.get('https://www.xuanshu.com/tupian/66/66137/66137s.jpg')


        for i in range(27):
            exec('req.append(req%s)'%i)
        return req



if __name__ == '__main__':
    app = QApplication(sys.argv)
    LiView = AppLiView()
    sys.exit(app.exec_())