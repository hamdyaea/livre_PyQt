from PyQt6.QtWidgets import QApplication, QFileDialog, QTableWidget, QTableWidgetItem
import csv

app = QApplication([])
filename, _ = QFileDialog.getOpenFileName(None, "Ouvrir un fichier", "", "Fichiers CSV (*.csv)")

if filename:
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

        table = QTableWidget()
        table.setRowCount(len(data))
        table.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, item in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(item))

        table.show()
        app.exec()
