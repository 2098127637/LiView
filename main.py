import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
	QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication
import win32gui
class HandleOperation():
    def __init__(self):
        self.thisHandle = win32gui.FindWindow(None, 'LiView')
    def setWallpaper(self):
        #设置壁纸
        wallpaperHandle = win32gui.FindWindow('SysListView32', None)
        win32gui.SetParent(self.thisHandle,wallpaperHandle)#设置窗口到窗口层的下方覆盖原壁纸与图表
        #设置为父窗口

    def noticeColumn(self):
        #将通知栏嵌入窗口
        noticeColumnHandle = win32gui.FindWindow('SysPager',None)
        print(noticeColumnHandle)
        assert noticeColumnHandle != 0
        #win32gui.SetParent(self.thisHandle, noticeColumnHandle)  # 设置窗口到窗口层的下方覆盖原壁纸与图表
        # 设置为父窗口
        win32gui.SetParent(65784,self.thisHandle)
class AppLiView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('LiView')
        self.setWindowIcon(QIcon('img\\icon.jpg'))
        self.showFullScreen()
        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=AppLiView()
    sys.exit(app.exec_())
