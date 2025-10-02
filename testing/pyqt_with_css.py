from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget, QGridLayout, QLabel, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

# app = QApplication(sys.argv)
# if no commandline arguments are needed:
app = QApplication([])

window = MainWindow()
window.show()

# Start the event loop.
app.exec()
