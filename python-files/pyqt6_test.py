# import sys for command line arguments if needed
# import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        layout.addWidget(Color("red"), 0, 3)
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        self.setFixedSize(QSize(400, 300))
        # self.setMinimumSize(100, 600)
        # self.setMaximumSize(1800, 600)
        # Set the central widget of the Window.
        self.setCentralWidget(button)

# app = QApplication(sys.argv)
# if no commandline arguments are needed:
app = QApplication([])

window = MainWindow()
window.show()

# Start the event loop.
app.exec()
