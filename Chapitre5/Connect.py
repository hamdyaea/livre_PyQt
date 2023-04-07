from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton                                                                                                                                                                            
                                                                                                                                                                                                                                              
class MainWindow(QMainWindow):                                                                                                                                                                                                                
    def __init__(self):                                                                                                                                                                                                                       
        super().__init__()                                                                                                                                                                                                                    
        self.setWindowTitle("My App")                                                                                                                                                                                                         
                                                                                                                                                                                                                                              
        button = QPushButton("Click me!")                                                                                                                                                                                                     
        button.clicked.connect(self.on_button_click)                                                                                                                                                                                          
        self.setCentralWidget(button)                                                                                                                                                                                                         
                                                                                                                                                                                                                                              
    def on_button_click(self):                                                                                                                                                                                                                
        print("Button clicked!")                                                                                                                                                                                                              
                                                                                                                                                                                                                                              
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
