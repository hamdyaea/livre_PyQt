from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        label = QLabel("Hello, world!")
        self.setCentralWidget(label)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
