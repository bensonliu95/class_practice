'''
以下为预置代码（创建窗口，添加窗口标题和背景图）
[10,300],[453,350],[76,260],[129,320],[520,160],[190,190],[209,322],[259,180],[356,159],[456,222],[513,346],[333,268],[153,159],[268,357],[550,263]

'''

from VipCode import *
import random

class UI_Gold(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(600,400)
        self.setWindowTitle("黄金矿工")
        self.setBackground("bg1.png")
        self.listXY=[[10,300],[453,350],[76,260],[129,320],[520,160],[190,190],[209,322],
        [259,180],[356,159],[456,222],[513,346],[333,268],[153,159],[268,357],[550,263]]
        random.shuffle(self.listXY)
        #定義存放礦石列表
        self.namelist=[]
        for x in range(0,len(self.listXY),3):
            self.addmineral(self.listXY[x][0],self.listXY[x][1],50,"stone.png",5)
            self.addmineral(self.listXY[x+1][0],self.listXY[x+1][1],20,"diamond.png",60)
            self.addmineral(self.listXY[x+2][0],self.listXY[x+2][1],30,"gold.png",30)
        self.elder=PyQt5_Qlabel(self,278,12,70,70)
        self.elder.setBackground("init.png")
        self.hook=PyQt5_Qlabel(self,290,88,20,15)
        self.hook.setBackground("hook.png")
        #添加繩子靜止時X,Y軸的變化範圍
        self.finalX=0
        self.finalY=0
        #添加點擊按鈕
        self.downButton=PyQt5_QPushButton(self,0,0,600,400)
        #設置背景顏色為透明
        self.downButton.setBackgroundColor("transparent")
        #添加點擊事件
        self.downButton.clicked.connect(self.downButtonClicked)
        #添加標記位
        self.isdo=0
        self.distanceX=0
        self.distanceY=0
        self.elderGif=PyQt5_QMovie("action.gif")
        self.elderGif.setScaledSize(self.elder.size())
        self.elder.setMovie(self.elderGif)
        self.beginLabel=PyQt5_Qlabel(self,0,0,600,400)
        self.beginLabel.setBackground("begin.png")
        self.beginButton=PyQt5_QPushButton(self,120,20,180,180)
        self.beginButton.setBackgroundColor("transparent")
        #按鈕點擊事件
        self.beginButton.clicked.connect(self.beginButtonClicked)
        self.score=0
        self.scorelabel=PyQt5_Qlabel(self,30,10,100,15)
        self.scorelabel.setText("分數:%d"% self.score)
        #時間變量
        self.finalTime=60
        #添加Label
        self.finalTimeLabel=PyQt5_Qlabel(self,30,40,100,15)
        #設置文本
        self.finalTimeLabel.setText("倒計時%d"%self.finalTime)
        #添加計時器組件
        self.Timer=QTimer()
        #綁定超時事件
        self.Timer.timeout.connect(self.timeOut)

    def timeOut(self):
        self.finalTime-=1
        self.finalTimeLabel.setText("倒計時%d"%self.finalTime)

    def beginButtonClicked(self):
        self.beginLabel.setVisible(False)
        self.beginButton.setVisible(False)
        self.Timer.start(1000)

    #繪製繩子事件
    def paintEvent(self,QPaintEvent):
        #取出畫筆
        qp=QPainter(self)
        #設置畫筆屬性
        qp.setPen(QPen(QColor("green"),3))
        #判斷開關是否打開
        if self.isdo==1:
            #print("延長線段,檢測碰撞")
            #self.isdo=0
            #華延長擺線
            qp.drawLine(300,60,300+self.finalX+self.distanceX,60+self.finalY+self.distanceY)
            #檢測擺線是否撈到東西 終點坐標X    終點坐標Y    鑽石標記     金子標記,石頭標記
            judge(self,300+self.finalX+self.distanceX,60+self.finalY+self.distanceY,60,30,5,20,30,50)
            #獲取檢測結果
            flag1,flag2=YesOrNo(self)
            #判斷是否撈到並上岸
            if flag1==1 and flag2==0:
                print("釣到礦石,還沒上岸")
                #隱藏鈎子
                self.hook.setVisible(False)
                #改變圖片
                change_img(self,30,60,5)
                #礦石隨繩子往上走
                self.namelist[self.index][0].move(300 - (getBorder()/2+3)+self.finalX+self.distanceX,60+self.finalY+self.distanceY)
            if flag1==1 and flag2==1:
                print("釣到礦石,已經上岸")
                #播放音效
                playAudio("success.mp3")
                #停止播放
                self.elderGif.stop()
                #讓分數進行增加
                self.score=self.score+self.namelist[self.index][1]
                self.scorelabel.setText("分數:%d"% self.score)
                #隱藏釣上來的礦石
                self.namelist[self.index][0].setVisible(False)
                #從坐標列表中刪除已經釣上去的礦石
                del self.listXY[self.index]
                #從礦石列表中刪除調上去的礦石坐標
                del self.namelist[self.index] 
                
            
        #鉤子處於搖擺狀態
        else:
            #繪製繩子
            qp.drawLine(300,60,300+self.finalX,60+self.finalY)
            self.hook.setVisible(True)
            self.hook.move(290+self.finalX,58+self.finalY)
            rock(dialog,30)
        refresh(dialog,3)

    def addmineral(self,x,y,size,img,reward):
        self.name=PyQt5_Qlabel(self,x,y,size,size)
        self.name.setBackground(img)
        self.namelist.append([self.name,reward])

    #按鈕點擊事件
    def downButtonClicked(self):
        print("畫繩子,檢測碰撞")
        self.isdo=1
        self.elder.setBackground("")
        self.elderGif.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Gold()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()