from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Click me!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)
     
    def button_clicked(self):
        print("Button was clicked!")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
