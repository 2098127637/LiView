from PyQt5.QtWidgets import QApplication, QWidget
from the import Ui_MainWindow   #导入py文件中的类
#ss是ui转换后的py文件，Ui_Form是文件中的类名

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget



import sys

class win(Ui_MainWindow):  #继承类
    def __init__(self):
        super().__init__()
        self.resize(300,300)
        self.setupUi(self)   #执行类中的setupUi函数
        self.DynamicIncrease()



    def DynamicIncrease(self):
        for i in range(10):
            exec('self.groupBox_4%s = QtWidgets.QGroupBox(self.groupBox_2)' % i)
            exec('self.groupBox_4%s.setTitle("")' % i)
            exec('self.groupBox_4%s.setObjectName("groupBox_4%s")'%(i,i))
            exec('self.label_4%s = QtWidgets.QLabel(self.groupBox_4%s)' %(i,i))
            exec('self.label_4%s.setGeometry(QtCore.QRect(0, 0, 121, 171))' % i)
            exec('self.label_4%s.setText("")' % i)
            exec('self.label_4%s.setPixmap(QtGui.QPixmap("/img/66137s.jpg"))' % i)
            exec('self.label_4%s.setScaledContents(True)' % i)
            exec('self.label_4%s.setObjectName("label_4%s")' %(i,i))
            exec('self.label_6%s = QtWidgets.QLabel(self.groupBox_4%s)'%(i,i))
            exec('self.label_6%s.setGeometry(QtCore.QRect(130, 0, 121, 171))' % i)
            exec('self.label_6%s.setText("")' % i)
            exec('self.label_6%s.setPixmap(QtGui.QPixmap("/img/66137s.jpg"))' % i)
            exec('self.label_6%s.setScaledContents(True)' % i)
            exec('self.label_6%s.setObjectName("label_6%s")' %(i,i))
            exec('self.label_7%s = QtWidgets.QLabel(self.groupBox_4%s)' %(i,i))
            exec('self.label_7%s.setGeometry(QtCore.QRect(270, 0, 121, 171))' % i)
            exec('self.label_7%s.setText("")' % i)
            exec('self.label_7%s.setPixmap(QtGui.QPixmap("/img/66137s.jpg"))' % i)
            exec('self.label_7%s.setScaledContents(True)' % i)
            exec('self.label_7%s.setObjectName("label_7%s")' %(i,i))
            exec('self.label_8%s = QtWidgets.QLabel(self.groupBox_4%s)' %(i,i))
            exec('self.label_8%s.setGeometry(QtCore.QRect(400, 0, 121, 171))' % i)
            exec('self.label_8%s.setText("")' % i)
            exec('self.label_8%s.setPixmap(QtGui.QPixmap("/img/66137s.jpg"))' % i)
            exec('self.label_8%s.setScaledContents(True)' % i)
            exec('self.label_8%s.setObjectName("label_8%s")' %(i,i))
            exec('self.label_9%s = QtWidgets.QLabel(self.groupBox_4%s)' %(i,i))
            exec('self.label_9%s.setGeometry(QtCore.QRect(530, 0, 121, 171))' % i)
            exec('self.label_9%s.setText("")' % i)
            exec('self.label_9%s.setPixmap(QtGui.QPixmap("/img/66137s.jpg"))' % i)
            exec('self.label_9%s.setScaledContents(True)' % i)
            exec('self.label_9%s.setObjectName("label_9%s")' %(i,i))
            exec('self.label_10%s = QtWidgets.QLabel(self.groupBox_4%s)' %(i,i))
            exec('self.label_10%s.setGeometry(QtCore.QRect(660, 50, 71, 71))' % i)
            exec('self.label_10%s.setObjectName("label_10%s")' %(i,i))
            exec('self.verticalLayout.addWidget(self.groupBox_4%s)' % i)


if __name__=='__main__':
    app=QApplication(sys.argv)
    w=win()
    w.show()
    sys.exit(app.exec_())