
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton


# This is basically css to style the UI
with open("d:/git/Python/testing/pyqt6-style/style.qss", "r") as f:
    stylesheet = f.read()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # self.setFixedSize(QSize(400, 300))

        layout = QGridLayout()

        # Set the central widget of the Window.
        for i in range(9):
            layout.addWidget(QPushButton(str(i+1)), i//3, i%3)
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()

window.setStyleSheet(stylesheet)

window.resize(350, 200)
window.show()
# Start the event loop.
app.exec()
