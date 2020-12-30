#自定义可点击的label组件
#标签被点击时触发 self.function 事件

from PyQt5 import QtCore, QtGui, QtWidgets


class clickLabel(QtWidgets.QLabel):
    '''
    自定义可点击的label组件
    标签被点击时触发 self.function 事件
    '''

    def __init__(self,parent=None):
        super(clickLabel, self).__init__(parent)
        self.arg = ''

    def mousePressEvent(self, event):
        '''
        重写标签的被点击事件
        :param event:
        :return:
        '''
        try:
            if event.buttons() == QtCore.Qt.LeftButton:  # 左键按下
                if self.arg == '':
                    self.function()
                else:
                    self.function(self.arg)
        except Exception as e:
            print(e)