import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        toolbar = self.addToolBar('Barre d\'outils')
        exit_action = QAction('Quitter', self)
        exit_action.triggered.connect(self.close)
        toolbar.addAction(exit_action)
         
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
