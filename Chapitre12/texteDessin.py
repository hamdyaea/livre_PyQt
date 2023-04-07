import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen, QFont, QColor
from PyQt6.QtCore import Qt


class DrawingArea(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Dessin')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(qp)
        qp.end()

    def drawText(self, qp):
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor('#FF5733'))
        qp.setPen(pen)
        qp.setFont(QFont('Arial', 16))
        qp.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, "Hello PyQt6!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrawingArea()
    window.show()
    sys.exit(app.exec())
