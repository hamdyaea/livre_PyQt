import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
  
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
  
        # Création de la QTableWidget
        self.table_widget = QTableWidget()
  
        # Définition du nombre de colonnes et de lignes
        self.table_widget.setRowCount(3)
        self.table_widget.setColumnCount(2)
  
        # Ajout des données
        item1 = QTableWidgetItem("Donnée 1")
        item2 = QTableWidgetItem("Donnée 2")
        item3 = QTableWidgetItem("Donnée 3")
        item4 = QTableWidgetItem("Donnée 4")
        item5 = QTableWidgetItem("Donnée 5")
        item6 = QTableWidgetItem("Donnée 6")
  
        self.table_widget.setItem(0, 0, item1)
        self.table_widget.setItem(0, 1, item2)
        self.table_widget.setItem(1, 0, item3)
        self.table_widget.setItem(1, 1, item4)
        self.table_widget.setItem(2, 0, item5)
        self.table_widget.setItem(2, 1, item6)
  
        # Mise en place de la fenêtre
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)
  
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
