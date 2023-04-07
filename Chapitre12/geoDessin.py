from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen, QColor


class DrawingArea(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Dessin')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircle(qp)
        qp.end()

    def drawCircle(self, qp):
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor('#FF5733'))
        qp.setPen(pen)
        qp.drawEllipse(100, 100, 100, 100)


if __name__ == '__main__':
    app = QApplication([])
    window = DrawingArea()
    window.show()
    app.exec()

