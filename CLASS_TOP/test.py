from VipCode import *

class UI_Test(PyQt5_QDialog):
    
    def setupUI(self):
        self.setFixedSize(300,300)
        self.a = PyQt5_QPushButton(self,0,0,0,0)

        # 测试pygame
        self.pygameTest = PyQt5_QPushButton(self,30,120,100,60)
        self.pygameTest.setText("PyGame")
        self.pygameTest.clicked.connect(self.pygameTestClicked)

        # 测试requests
        self.requestsTest = PyQt5_QPushButton(self,160,120,100,60)
        self.requestsTest.setText("requests")
        self.requestsTest.clicked.connect(self.requestsClicked)

    def requestsClicked(self):
        self.s = getQuestion(1)
        print(self.s)
        if self.s["wenti"] == "由于网络问题未找到所需内容，请检查您的网络":
            QMessageBox.warning(self, "提示信息", "测试失败。")
        else:
            QMessageBox.warning(self, "提示信息", "测试成功。")

    def pygameTestClicked(self):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load('RESOURCE/audio/test.wav')
            pygame.mixer.music.play()
            QMessageBox.warning(self, "提示信息", "测试成功。")
        except:
            QMessageBox.warning(self, "提示信息", "测试失败。")

if __name__ == '__main__':
    # 创建应用
    app = QApplication(sys.argv)
    # 创建窗口
    dialog = UI_Test()
    # 设置窗口的属性
    dialog.setupUI()
    dialog.show()
    # 保持应用运行
    app.exec_()
