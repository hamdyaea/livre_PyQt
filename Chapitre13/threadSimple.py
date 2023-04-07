import sys
import time
from PyQt6.QtCore import QThread, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel


class MonThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        # Tâche effectuée dans le thread
        for i in range(1, 11):
            print(f"Compteur : {i}")
            time.sleep(1)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mon programme multithreading")

        # Layouts
        main_layout = QVBoxLayout(self)
        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        # Bouton pour lancer le thread
        start_button = QPushButton("Lancer le thread", self)
        start_button.clicked.connect(self.lancer_thread)
        button_layout.addWidget(start_button)

        # Étiquette pour afficher le statut du thread
        self.status_label = QLabel("Thread inactif", self)
        main_layout.addWidget(self.status_label)

        # Thread
        self.mon_thread = MonThread()
        self.mon_thread.finished.connect(self.thread_termine)

    def lancer_thread(self):
        if not self.mon_thread.isRunning():
            self.mon_thread.start()
            self.status_label.setText("Thread en cours...")
            self.status_label.setStyleSheet("color: green; font-weight: bold;")

    def thread_termine(self):
        self.status_label.setText("Thread terminé")
        self.status_label.setStyleSheet("color: red; font-weight: bold;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())                                                                                                                                                                                                              
                                                                                                                                                                                                                                       
                                         
