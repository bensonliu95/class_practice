from VipCode import * 

class UI(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(400,300)

    def paintEvent(self,QPaintEvent):
        qp=QPainter(self)
        qp.setPen(QPen(QColor("red"),5))
        qp.drawLine(200,100,200,200)
        qp.drawLine(150,150,250,150)
        qp.drawLine(120,200,280,200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()