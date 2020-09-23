from VipCode import *
from class12_two import *


class UI_First(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
    


    # 播放音效
    def playAudio(self, audio_name):
        # 添加媒体音效播放器
        self.media = PyQt5_QMediaPlayer()
        # 确定所要播放的音效文件
        self.media.prepare_audio(audio_name)
        # 播放
        self.media.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    first = UI_First()
    first.setupUI()
    first.showDialog()
    app.exec_()
