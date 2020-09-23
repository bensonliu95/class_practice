'''
预置代码：创建一个窗口并显示
 
'''
from VipCode import *
import random

class Anim_Dialog(PyQt5_FramelessBox):
    def showDialog(self):
        self.show()
        
    def setupUI(self):
        self.setFixedSize(750, 550)
        #添加label
        self.label=PyQt5_Qlabel(self,0,0,750,550)
        #設置背景
        self.label.setBackground("bg_canvas.png")
        #設置窗口透明
        self.setWindowsTransparent(True)
        #添加退出按鈕
        self.quit=PyQt5_QPushButton(self,215,0,305,140)
        #設置背景顏色為透明
        self.quit.setBackgroundColor("transparent")
        #添加點擊事件
        self.quit.clicked.connect(self.Quit)
        self.listXY=[[132,160], [319,160], [515,165], [100,250], [320,250], [520,250], [95,347], [320,352], [540,354]]
        self.hamsters=[]
        for x in range(9):
            self.addHamster(x)
        self.timer=QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeOut)
        #self.flag=-1
        #添加錘子
        self.hammer=PyQt5_Qlabel(self,132,160,122,122)
        #設置背景
        self.hammer.setBackground("hammer.png")
        #設置默認隱藏
        self.hammer.setVisible(False)
        #得分初始值
        self.score=0
        #時間初始值
        self.time=15
        #添加時間組件
        self.timelabel = PyQt5_Qlabel(self,280,160,100,20)
        #設置字體
        self.timelabel.setFont(QFont("手扎体-简",15))
        #設置文字顏色
        self.timelabel.setTextColor("red")
        #顯示文字
        self.timelabel.setText("時間:%d" % self.time)
        #添加得分
        self.scorelabel = PyQt5_Qlabel(self,380,160,100,20)
        #設置文字顏色
        self.scorelabel.setTextColor("blue")
        #設置字體
        self.scorelabel.setFont(QFont("手扎体-简",15))
        #設置文本
        self.scorelabel.setText("得分：%d" % self.score)


    def timeOut(self):
        while True:
            if self.hammer.isVisible():
                self.hammer.setVisible(False)
            index=random.randint(0,8)
            if self.hamsters[index][0].isVisible()==False:
                self.hamsters[index][0].setVisible(True)
                #self.hamsters[self.flag][0].setVisible(False)
                #self.flag=index
                break

        for i in self.hamsters:
            if i[0].isVisible():
                i[1]+=1
                if i[1]>3:
                    i[0].setVisible(False)
                    i[1]=0
                    i[0].setBackground("hamster.png")
                    i[0].setEnabled(True)
        #時間遞減一
        self.time -= 1
        #判斷時間是否為零
        if self.time <= 0:
            #關閉計時器
            self.timer.stop()
            #顯示得分
            QMessageBox.information(self,"得分","當前得分為%d" % self.score)
        self.timelabel.setText("時間:%d" % self.time)
        

    def Quit(self):
        QApplication.quit()

    def addHamster(self,x):
        #添加地鼠
        self.hamster=PyQt5_Qlabel(self,self.listXY[x][0],self.listXY[x][1],122,122)
        #設置背景
        self.hamster.setBackground("hamster.png")
        #地鼠放進大籠子
        self.hamsters.append([self.hamster,0])
        #默認隱藏地鼠
        self.hamster.setVisible(False)
        self.hamster.pressed.connect(lambda:self.hitHamster(x))

    def hitHamster(self,x):
        self.hamsters[x][0].setBackground("hit.png")
        self.hamsters[x][0].setEnabled(False)
        #錘子跟地鼠一起動
        self.hammer.move(self.listXY[x][0],self.listXY[x][1])
        #讓錘子顯示
        self.hammer.setVisible(True)
        #讓分數遞增一
        self.score += 1
        self.scorelabel.setText("得分：%d" % self.score)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog =Anim_Dialog()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()