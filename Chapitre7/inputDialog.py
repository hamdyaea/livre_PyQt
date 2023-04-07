from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QInputDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        button = QPushButton("Get username", self)
        button.move(50, 50)
        button.clicked.connect(self.get_username)

        self.username_edit = QLineEdit(self)
        self.username_edit.move(50, 100)

        self.show()

    def get_username(self):
        username, ok = QInputDialog.getText(self, "Get username", "Enter your username:")
        if ok and username:
            self.username_edit.setText(username)

app = QApplication([])
window = MainWindow()
app.exec()
