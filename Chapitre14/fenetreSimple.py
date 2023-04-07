from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView

app = QApplication([])
window = QMainWindow()

# Create a QWebEngineView widget
web_view = QWebEngineView()
web_view.setUrl(QUrl("https://www.google.com"))

# Add the QWebEngineView widget to the main window layout
window.setCentralWidget(web_view)

window.show()
app.exec()
