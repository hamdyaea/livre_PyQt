import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QStyleFactory

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Définir le titre de la fenêtre
        self.setWindowTitle("Application avec style Fusion")

        # Créer un widget central
        central_widget = QWidget()

        # Créer un layout vertical pour le widget central
        layout = QVBoxLayout(central_widget)

        # Créer un label pour afficher du texte
        label = QLabel("Hello, World!")

        # Modifier la police du texte
        font = QFont()
        font.setPointSize(24)
        label.setFont(font)

        # Ajouter le label au layout
        layout.addWidget(label)

        # Définir le widget central de la fenêtre
        self.setCentralWidget(central_widget)

        # Définir le style Fusion
        QApplication.setStyle(QStyleFactory.create("Fusion"))

        # Modifier la palette de couleurs pour le style Fusion
# Il faut utiliser : https://htmlcolorcodes.com pour les couleurs
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(10,20,30))
        palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(20,20,23))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(20,50,234))
        palette.setColor(QPalette.ColorRole.Text, QColor(110,232,12))
        palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(100,23,233))
        palette.setColor(QPalette.ColorRole.BrightText, QColor(10,40,222))
        palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(222,12,123))
        QApplication.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
