from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton                                                                                                                                              
                                                                                                                                                                                                                                              
class MainWindow(QMainWindow):                                                                                                                                                                                                                
    def __init__(self):                                                                                                                                                                                                                       
        super().__init__()                                                                                                                                                                                                                    
        self.setWindowTitle("My App")                                                                                                                                                                                                         
                                                                                                                                                                                                                                              
        label = QLabel("Hello, world!")                                                                                                                                                                                                       
        button = QPushButton("Click me!")                                                                                                                                                                                                     
                                                                                                                                                                                                                                              
        layout = QVBoxLayout()                                                                                                                                                                                                                
        layout.addWidget(label)                                                                                                                                                                                                               
        layout.addWidget(button)                                                                                                                                                                                                              
                                                                                                                                                                                                                                              
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
