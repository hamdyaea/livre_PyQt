from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt

class ClickableLabel(QLabel):
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            print("Label clicked at ({}, {})".format(event.position().x(), event.position().y()))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = ClickableLabel("Click me!")
        self.setCentralWidget(label)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()

