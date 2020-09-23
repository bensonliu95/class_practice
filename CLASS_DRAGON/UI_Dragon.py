from VipCode import *

class UI_Dragon(PyQt5_QDialog):
    def showDialog(self):
        self.show()
    def setupUI(self):
        self.setFixedSize(1000,600)
        # 设置窗口的背景
        self.setBackground("background.png")
# ---------------------------代码书写位置------------------------------
       

if __name__ == '__main__':
    # 创建应用
    app = QApplication(sys.argv)
    # 创建窗口
    dialog =UI_Dragon()
    # 设置窗口的属性
    dialog.setupUI()
    # 显示窗口
    dialog.showDialog()
    # 保持应用运行
    app.exec_()