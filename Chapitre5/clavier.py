from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

    def keyPressEvent(self, event):
        print("Key pressed: ", event.key())

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
