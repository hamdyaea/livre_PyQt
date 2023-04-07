from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QPen, QColor
import sys

class DrawingArea(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Dessin')
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor('#FF5733'))
        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)
        qp.drawLine(20, 80, 250, 80)
        qp.drawLine(20, 120, 250, 120)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrawingArea()
    window.show()
    sys.exit(app.exec())

