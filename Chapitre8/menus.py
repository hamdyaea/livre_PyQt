import sys                                                                                                                                                                                                                                    
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar 
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        menubar = self.menuBar()
        file_menu = menubar.addMenu('Fichier')
        edit_menu = menubar.addMenu('Édition')
        exit_action = QAction('Quitter', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
         
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
