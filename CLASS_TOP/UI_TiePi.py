from VipCode import *   # 从工具箱中拿到所有的东西

# 创建窗口类
class UI_TiePi(PyQt5_QDialog):

    #================代码书写位置======================
    # 显示窗口的函数/方法  self  表示当前窗口   class2
    def showDialog(self):
        # 让窗口显示
        self.show()

    # 美化窗口方法
    def setupUI(self):
        # 设置窗口大小,尺寸不可以拖动改变
        self.setFixedSize(960, 600)
        # 设置窗口标题
        self.setWindowTitle("Hello Top!!!")
        # 设置窗口背景
        self.setBackground("mainBg.png")
        # 添加标签组件  前两个表示坐标 后两个 表示尺寸（宽，高）
        self.label = PyQt5_Qlabel(self, 370, 180, 350, 350)
        # 设置label背景
        # self.label.setBackground("main_lion.gif")

        # 播放gif
        self.playGif("main_lion.gif")
        # 播放动画
        self.playAudio("main_lion.wav")
               
        # 添加汉堡按钮
        self.hamburger = PyQt5_QPushButton(self, 60, 388, 57, 57)
        # 设置按钮背景
        self.hamburger.setBackground("main_hamburger_normal.png")
        # 设置按压背景
        self.hamburger.setPressedBackground("main_hamburger_pressed.png")
        # 添加按钮点击事件
        self.hamburger.clicked.connect(self.hamburgerClicked)
        # 添加果汁按钮
        self.juice = PyQt5_QPushButton(self, 60, 460, 57, 57)
        # 设置按钮背景
        self.juice.setBackground("main_juice_normal.png")
        # 设置按压背景
        self.juice.setPressedBackground("main_juice_pressed.png")
        # 添加按钮点击事件
        self.juice.clicked.connect(self.juiceClicked)
        # 添加组控件
        self.allGroup = PyQt5_QGroupBox(self, 814, 156, 60, 367)
        # 设置背景颜色
        self.allGroup.setBackground("action_group.png")
        # 眩晕按钮
        self.halo = PyQt5_QPushButton(self.allGroup, 9, 5, 42, 42)
        # 设置背景
        self.halo.setBackground("main_halo_normal.png")
        # 设置按压背景
        self.halo.setPressedBackground("main_halo_normal.png")
        # 按钮点击事件
        self.halo.clicked.connect(self.haloClicked)
        # 生气按钮
        self.anger = PyQt5_QPushButton(self.allGroup, 9, 56, 42, 42)
        # 设置背景
        self.anger.setBackground("main_anger_normal.png")
        # 设置按压背景
        self.anger.setPressedBackground("main_anger_normal.png")
        # 按钮点击事件
        self.anger.clicked.connect(self.angerClicked)
        # 哭泣按钮
        self.cry = PyQt5_QPushButton(self.allGroup, 9, 107, 42, 42)
        # 设置背景
        self.cry.setBackground("main_cry_normal.png")
        # 设置按压背景
        self.cry.setPressedBackground("main_cry_normal.png")
        # 按钮点击事件
        self.cry.clicked.connect(self.cryClicked)
        # 眼镜按钮
        self.glasses = PyQt5_QPushButton(self.allGroup, 9, 158, 42, 42)
        # 设置背景
        self.glasses.setBackground("main_glasses_normal.png")
        # 设置按压背景
        self.glasses.setPressedBackground("main_glasses_normal.png")
        # 按钮点击事件
        self.glasses.clicked.connect(self.glassesClicked)
        # 拳击按钮
        self.boxing = PyQt5_QPushButton(self.allGroup, 9, 209, 42, 42)
        # 设置背景
        self.boxing.setBackground("main_boxing_normal.png")
        # 设置按压背景
        self.boxing.setPressedBackground("main_boxing_normal.png")
        # 按钮点击事件
        self.boxing.clicked.connect(self.boxingClicked)
        # 消失按钮
        self.disappear = PyQt5_QPushButton(self.allGroup, 9, 260, 42, 42)
        # 设置背景
        self.disappear.setBackground("main_disappear_normal.png")
        # 设置按压背景
        self.disappear.setPressedBackground("main_disappear_normal.png")
        # 按钮点击事件
        self.disappear.clicked.connect(self.disappearClicked)
        # 显示隐藏按钮
        self.all = PyQt5_QPushButton(self, 815, 465, 58, 58)
        # 设置按钮背景
        self.all.setBackground("main_all_normal.png")
        # 设置按压背景
        self.all.setPressedBackground("main_all_pressed.png")
        # 点击事件
        self.all.clicked.connect(self.allClicked)
        # 进入主界面设置组控件默认隐藏
        self.allGroup.setVisible(False)
        # 答题按钮
        self.answer = PyQt5_QPushButton(self, 60, 316, 57, 57)
        # 设置按钮背景
        self.answer.setBackground("main_answer_normal.png")
        # 设置按压背景
        self.answer.setPressedBackground("main_answer_pressed.png")
        # 点击事件
        self.answer.clicked.connect(self.answerClicked)
        # 添加系统托盘
        self.tray = PyQt5_QSystemTrayIcon(self)
        # 设置托盘图标
        self.tray._setIcon("icon.png")
        # 添加显示菜单
        self.menuShow = self.tray.addMenu("显示")
        # 绑定右键菜单的事件
        self.menuShow.triggered.connect(self.trayShow)
        # 添加退出的菜单
        self.menuExit = self.tray.addMenu("退出")
        # 绑定右键菜单的事件
        self.menuExit.triggered.connect(self.trayExit)
        # 添加透明窗口
        self.framelessBox = PyQt5_FramelessBox()
        # 设置组件置顶
        self.framelessBox.setWindowsTop(True)
        # 设置组件透明
        self.framelessBox.setWindowsTransparent(True)
        # 添加一个label到framelessBox
        self.frameLabel = PyQt5_Qlabel(self.framelessBox, 0, 0, 340, 340)
        # 设置背景，测试透明属性
        # self.frameLabel.setBackground("icon.png")
        # 播放透明窗口中的gif
        self.playframeGif("frame_fly.gif")
        # 1.为framelessBox添加动画
        self.anim = PyQt5_Animation(self.framelessBox)
        # 2.设置动画时长  单位是毫秒
        self.anim.setDuration(4000)
        # 5.获取窗口宽度
        self.width = getDesktopWidth()
        # 6.窗口高度
        self.height = getDesktopHeight()
        # 3.设置动画终点  修改 去右下角  前两个值终点坐标，后两个终点label大小
        self.anim.setEndValues(self.width-340, self.height-340, 140, 140)
        # 设置动画的模式
        self.anim.setMode(Mode.InOut)
        # 连接动画改变事件
        self.anim.valueChanged.connect(self.animChange)
        # 动画结束
        self.anim.animFinished.connect(self.animFinish)
        # 1添加结束动画
        self.closeAnim = PyQt5_Animation(self.framelessBox)
        # 2设置时长
        self.closeAnim.setDuration(4000)
        # 3.设置终点
        self.closeAnim.setEndValues(self.width/2-170, self.height/2-170, 340, 340)
        # 4 连接动画改变事件
        self.closeAnim.valueChanged.connect(self.animChange)
        # 5.closeAnim结束事件
        self.closeAnim.animFinished.connect(self.closeAnimFinish)
        # 添加鼠标移入事件
        self.frameLabel.entered.connect(self.frameEnter)
        # 创建变量记录anim的状态  False  没结束
        self.isAnimFinished = False
        # 鼠标移出事件
        self.frameLabel.leaved.connect(self.frameLeave)
    
    # 鼠标移出睡觉
    def frameLeave(self):
        # 判断anim是否结束
        if self.isAnimFinished:
            # 播放睡觉的gif
            self.playframeGif("frame_sleep.gif")
    # 鼠标移入
    def frameEnter(self):
        # 判断anim是否结束
        if self.isAnimFinished:
            # 播放玩球的gif
            self.playframeGif("frame_play.gif")
    
    # closeAnim结束，显示主界面
    def closeAnimFinish(self):
        # 1.关闭透明窗口
        self.framelessBox.close()
        # 2.显示主界面
        self.show()        

    # 动画结束事件
    def animFinish(self):
        # isAnimFinished值变化  表示结束
        self.isAnimFinished = True
        # 切换gif  小狮子从气球上下来
        self.playframeGif("frame_down.gif")
        # 获取gif帧数
        self.flyCount = self.frameGif.frameCount()
        # 连接帧数改变事件
        self.frameGif.frameChanged.connect(self.changeGif)
    
    # 帧数改变事件
    def changeGif(self):
        # 帧数自减一
        self.flyCount -= 1
        # 如果帧数为0
        if self.flyCount == 0:
            # 结束下来的gif
            self.frameGif.stop()
            # 切换睡觉的gif
            self.playframeGif("frame_sleep.gif")
    
    # 动画改变事件
    def animChange(self):
        # 把label大小匹配透明窗口大小
        self.frameLabel.setSize(self.framelessBox.size())
        # 将gif大小匹配label
        self.frameGif.setScaledSize(self.frameLabel.size())

    #播放gif
    def playframeGif(self,gif_name):
        # 1.创建gif
        self.frameGif = PyQt5_QMovie(gif_name)
        # 2.尺寸
        self.frameGif.setScaledSize(self.frameLabel.size())
        # 3.用label加载gif
        self.frameLabel.setMovie(self.frameGif)
        # 4.播放gifelf.frameLabel.setMovie(self.frameGif)
        # 4.播放gif
        self.frameGif.start()
    
    # 程序退出
    def trayExit(self):
        # 让程序退出   窗口 - 应用
        QApplication.exit() 
    
    # 窗口显示菜单事件
    def trayShow(self):
        # 关闭透明窗口
        # self.framelessBox.close()
        # 窗口显示
        # self.show()   注释快捷键   ctrl + /
        # 切换坐气球的gif
        self.playframeGif("frame_fly.gif")
        # 4播放closeAnim
        self.closeAnim.start()
    
    # 更改程序自带的关闭方法  关闭窗口
    def closeEvent(self, event):
        # 输出一句话验证该方法是否被调用
        print("点击了关闭窗口")
        # 隐藏窗口
        self.hide()
        # 显示透明窗口
        self.framelessBox.show()
        # 4.播放动画
        self.anim.start()
        # 改变默认的退出方法
        event.ignore()
    
    # 答题按钮点击事件
    def answerClicked(self):
        # 创建窗口类对象
        dialog = UI_Answer()
        # 美化窗口
        dialog.setupUI()
        # 窗口显示
        dialog.showDialog()
        # 窗口持续运行
        dialog.exec_()
 
    # 显示隐藏按钮
    def allClicked(self):
        # 如果组控件可见
        if self.allGroup.isVisible():
            # 组控件隐藏  False 表示隐藏   True   显示
            self.allGroup.setVisible(False)
        else:
            # 组控件显示  False 表示隐藏   True   显示
            self.allGroup.setVisible(True)  #setVisible() 设置组控件 显示/隐藏

    # 消失按钮点击事件
    def disappearClicked(self):
        # 播放动画
        self.playGif("disappear.gif")
        # 播放音效
        self.playAudio("disappear.wav")
    
    # 拳击按钮点击事件
    def boxingClicked(self):
        # 播放动画
        self.playGif("boxing.gif")
        # 播放音效
        self.playAudio("boxing.wav")

    # 眼镜按钮点击事件
    def glassesClicked(self):
        # 播放动画
        self.playGif("glasses.gif")
        # 播放音效
        self.playAudio("glasses.wav")

    # 哭泣按钮点击事件
    def cryClicked(self):
        # 播放动画
        self.playGif("cry.gif")
        # 播放音效
        self.playAudio("cry.wav")

    # 生气按钮点击事件
    def angerClicked(self):
        # 播放动画
        self.playGif("anger.gif")
        # 播放音效
        self.playAudio("anger.wav")
        
    # 眩晕按钮点击事件
    def haloClicked(self):
        # 播放动画
        self.playGif("halo.gif")
        # 播放音效
        self.playAudio("halo.wav")

    # 果汁按钮点击事件
    def juiceClicked(self):
        # 播放动画
        self.playGif("juice.gif")
        # 播放音效
        self.playAudio("juice.wav")
    
    # 播放gif动画
    def playGif(self,gif_name):
        # 1 确定要播放的gif文件
        self.gif = PyQt5_QMovie(gif_name)
        # 2 设置播放的gif的大小  保持跟相框尺寸一致
        self.gif.setScaledSize(self.label.size())
        # 3 使用label加载gif
        self.label.setMovie(self.gif)
        # 4 播放gif
        self.gif.start()
        # 获取动画帧数
        self.frameCount = self.gif.frameCount()
        # 连接帧数改变事件
        self.gif.frameChanged.connect(self.returnGif)
    
    # 帧数改变事件
    def returnGif(self):
        # 每运行一帧，帧数减一
        self.frameCount -= 1
        # 如果帧数为0
        if  self.frameCount == 0:
            # 停止播放gif
            self.gif.stop()
            # 播放主界面的动画
            # 1 确定要播放的gif文件
            self.gif = PyQt5_QMovie("main_lion.gif")
            # 2 设置播放的gif的大小  保持跟相框尺寸一致
            self.gif.setScaledSize(self.label.size())
            # 3 使用label加载gif
            self.label.setMovie(self.gif)
            # 4 播放gif
            self.gif.start()

    # 播放音效
    def playAudio(self,audio_name):
        # 1 添加播放器
        self.media = PyQt5_QMediaPlayer()
        # 2 确定要播放的音效文件
        self.media.prepare_audio(audio_name)
        # 3 播放音效
        self.media.play()

    # 汉堡按钮点击事件
    def hamburgerClicked(self):
        # 提示按钮被点击了
         #QMessageBox.information(self, "你好啊", "game over")
        # 播放动画
        self.playGif("hamburger.gif")
        # 播放音效
        self.playAudio("hamburger.wav")    

# 程序主入口
if __name__ == '__main__':
    # 通过QApplication创建应用
    app = QApplication(sys.argv)

    #================代码书写位置======================
    # 创建窗口类对象
    dialog = UI_TiePi()
    # 调用美化窗口的方法
    dialog.setupUI()
    # 调用显示窗口的方法
    dialog.showDialog()
    #================================================
    # 让应用持续保持运行
    app.exec_()