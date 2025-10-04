from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget, QGridLayout, QLabel, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication([])

window = MainWindow()
window.show()

# Start the event loop.
app.exec()
