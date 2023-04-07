from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        checkbox = QCheckBox("Check me!")
        checkbox.stateChanged.connect(self.checkbox_changed)
        self.setCentralWidget(checkbox)
     
    def checkbox_changed(self, state):
        if state == 2:
            print("Checkbox is checked!")
        else:
            print("Checkbox is unchecked!")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()

