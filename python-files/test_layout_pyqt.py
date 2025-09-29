# import sys for command line arguments if needed
# import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
## from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout = QGridLayout()
        ## color stuff
        # layout.addWidget(Color("red"), 0, 3)
        # layout.addWidget(Color("green"), 1, 1)
        # layout.addWidget(Color("orange"), 2, 2)
        # layout.addWidget(Color("blue"), 3, 0)
        # self.setFixedSize(QSize(400, 300))
        # self.setMinimumSize(1800, 600)
        # self.setMaximumSize(1800, 600)

        layout.addWidget(QPushButton("1"), 0, 0)
        layout.addWidget(QPushButton("2"), 0, 1)
        layout.addWidget(QPushButton("3"), 0, 2)
        layout.addWidget(QPushButton("4"), 1, 0)
        layout.addWidget(QPushButton("5"), 1, 1)
        layout.addWidget(QPushButton("6"), 1, 2)
        layout.addWidget(QPushButton("7"), 2, 0)
        layout.addWidget(QPushButton("8"), 2, 1)
        layout.addWidget(QPushButton("9"), 2, 2)
        layout.addWidget(QPushButton("+"), 3, 0)
        layout.addWidget(QPushButton("0"), 3, 1)
        layout.addWidget(QPushButton("="), 3, 2)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

# app = QApplication(sys.argv)
# if no commandline arguments are needed:
app = QApplication([])
window = MainWindow()
window.show()
# Start the event loop.
app.exec()
