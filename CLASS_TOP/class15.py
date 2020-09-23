from VipCode import *
import random

class UI_Question(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        # 设置窗口的大小，不可拖动更改窗口大小
        self.setFixedSize(600, 400)
        # 设置窗口的背景
        self.setBackground("informationBg.png")
        # 初始化性别str
        self.sexStr="----"
        # 添加组
        self.allGroup = PyQt5_QGroupBox(self, 70, 70, 500, 250)
        self.allGroup.setBorderWidth(0)
       
        # 添加姓名label
        self.userNameLabel = PyQt5_Qlabel(self.allGroup, 10, 10, 50, 20)
        # 设置字体大小
        self.userNameLabel.setFontSize(15)
        # 设置文字
        self.userNameLabel.setText("姓名:")

        # 添加第一个编辑框
        self.userNameEdit = PyQt5_QLineEdit(self.allGroup, 60, 10, 80, 20)
        # 更改背景图片
        self.userNameEdit.setBackground("information.png")

        # 添加性别label
        self.sexLabel = PyQt5_Qlabel(self.allGroup, 180, 10, 50, 20)
        self.sexLabel.setFontSize(15)
        self.sexLabel.setText("性别:")
        
         # 添加兴趣label
        self.interestLabel = PyQt5_Qlabel(self.allGroup, 10, 50, 50, 20)
        self.interestLabel.setFontSize(15)
        self.interestLabel.setText("爱好:")

        self.informationLabel =PyQt5_Qlabel(self.allGroup, 10, 90, 100, 20 )
        self.informationLabel.setText("个人信息展示")

        self.information = PyQt5_Qlabel(self.allGroup, 10, 120, 370,100)
        self.information.setBackground("information.png")
        self.information.setFontSize(15)

        # 设置居左和顶部对齐
        self.information.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        # 设置文字左边距为50 上边距为40，右边距为50，没有下边距
        self.information.setContentsMargins(20, 20, 30, 0)

        self.defineButton = PyQt5_QPushButton(self, 240, 320, 120, 32)
        self.defineButton.setBackground("define_normal.png")
        self.defineButton.setPressedBackground("define_pressed.png")
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Question()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()
