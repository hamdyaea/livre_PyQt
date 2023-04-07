from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        button = QPushButton("Show message", self)
        button.move(50, 50)
        button.clicked.connect(self.show_message)

    def show_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("My message box")
        msg.setText("This is my message.")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msg.exec()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()                      
