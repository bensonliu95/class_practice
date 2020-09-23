from VipCode import *

class UI_Second(PyQt5_QDialog):
    def showDialog(self):
        self.show()

    def setupUI(self):


    def playGif(self,gif_name):
        # 确定要播放的gif
        self.gif = PyQt5_QMovie(gif_name)
        # 给gif设置大小
        self.gif.setScaledSize(self.label.size())
        # 确定label播放哪个gif 
        self.label.setMovie(self.gif)
        # 播放gif
        self.gif.start()



