from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = QLabel("Click me!")
        label.mousePressEvent = self.on_label_mouse_press
        self.setCentralWidget(label)

    def on_label_mouse_press(self, event):
        print("Label clicked at ({}, {})".format(event.x(), event.y()))

app = QApplication([])
window = MainWindow()
window.show()
app.exec()

