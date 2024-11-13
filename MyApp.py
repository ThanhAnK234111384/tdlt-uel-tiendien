from PyQt6.QtWidgets import QApplication, QMainWindow
from Tiendien.MainWindowEx import MainWindow

app = QApplication([])
mainWindow = MainWindow()
mainWindow.show()
app.exec()
