import sys
import time
from PyQt6.QtCore import Qt, QObject, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        for i in range(1, 101):
            time.sleep(0.1)
            self.progress.emit(i)
        self.finished.emit()

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Création du layout vertical pour la fenêtre
        layout = QVBoxLayout()

        # Ajout d'un label pour afficher la progression
        self.label = QLabel('0%')
        layout.addWidget(self.label)

        # Ajout d'un bouton pour démarrer le thread
        self.button = QPushButton('Démarrer')
        self.button.clicked.connect(self.start_thread)
        layout.addWidget(self.button)

        # Configuration du layout pour la fenêtre
        self.setLayout(layout)

        # Initialisation du worker et du thread
        self.worker = Worker()
        self.thread = QThread()

        # Configuration du worker pour s'exécuter dans le thread
        self.worker.moveToThread(self.thread)
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.thread.quit)

        # Configuration du thread pour exécuter le worker
        self.thread.started.connect(self.worker.run)
        self.thread.finished.connect(self.thread.deleteLater)

    def start_thread(self):
        self.button.setDisabled(True) # désactiver le bouton pour éviter le démarrage multiple du thread
        self.thread.start()

    def update_progress(self, value):
        self.label.setText(f'{value}%')
        if value == 100:
            self.button.setEnabled(True) # réactiver le bouton une fois le thread terminé

app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec())
