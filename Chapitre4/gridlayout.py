from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
         
        button_1 = QPushButton("Button 1")
        button_2 = QPushButton("Button 2")
        button_3 = QPushButton("Button 3")
        button_4 = QPushButton("Button 4")
         
        layout = QGridLayout()
        layout.addWidget(button_1, 0, 0)
        layout.addWidget(button_2, 0, 1)
        layout.addWidget(button_3, 1, 0)
        layout.addWidget(button_4, 1, 1)
         
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
