from VipCode import *

class UI_Gif(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):

        self.setFixedSize(700, 500)
        self.setBackground("mainBg2.png")
        self.label = PyQt5_Qlabel(self, 200, 140, 300, 300)
        self.playGif("initial.gif")
  
    # 播放的gif
    def playGif(self, gif_name):
        # 确定要播放的gif
        self.gif = PyQt5_QMovie(gif_name)
        # 给gif设置大小
        self.gif.setScaledSize(self.label.size())
        # 确定label播放哪个gif
        self.label.setMovie(self.gif)
        # 播放gif
        self.gif.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Gif()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()
