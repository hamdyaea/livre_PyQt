from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        button = QPushButton("Open file", self)
        layout.addWidget(button)
        button.clicked.connect(self.open_file)

        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text files (*.txt)")
        if filename:
            with open(filename, "r") as file:
                content = file.read()
                self.text_edit.setPlainText(content)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
