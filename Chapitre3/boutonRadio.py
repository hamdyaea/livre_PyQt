from PyQt6.QtWidgets import QApplication, QMainWindow, QRadioButton, QHBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
         
        radio_button_1 = QRadioButton("Option 1")
        radio_button_2 = QRadioButton("Option 2")
         
        hbox = QHBoxLayout()
        hbox.addWidget(radio_button_1)
        hbox.addWidget(radio_button_2)
         
        widget = QWidget()
        widget.setLayout(hbox)
        self.setCentralWidget(widget)
         
        radio_button_1.setChecked(True)
        radio_button_1.toggled.connect(self.radio_button_toggled)
        radio_button_2.toggled.connect(self.radio_button_toggled)

    def radio_button_toggled(self):
        if self.sender().isChecked():
            print(f"{self.sender().text()} is checked!")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
