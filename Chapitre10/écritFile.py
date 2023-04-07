from PyQt6.QtWidgets import QApplication, QFileDialog

app = QApplication([])
filename, _ = QFileDialog.getSaveFileName(None, "Enregistrer un fichier", "", "Fichiers texte (*.txt)")

if filename:
    with open(filename, 'w') as f:
        f.write("Hello, World!")
