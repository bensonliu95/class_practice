from VipCode import *
import random

class UI_Battle(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        # 设置窗口的大小，不可拖动更改窗口大小
        self.setFixedSize(640, 360)
        # 设置窗口的背景
        self.setBackground("battleBg.png")

        self.heros = ["不知火舞","东皇太一","兰陵王","关羽","后羿","周瑜","大乔","妲己","安琪拉","宫本武藏",
        "扁鹊","曹操","狄仁杰","白起","花木兰","蔡文姬","貂蝉","达摩","阿轲","黄忠"]
    
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Battle()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()
