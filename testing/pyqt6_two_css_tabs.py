import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLabel, QPushButton, QTabWidget, QMainWindow
)

class TabOne(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        # label = QLabel("This is the first tab.")
        
        # for loop for the first 9 buttons in a grid layout
        for i in list(range(9)):
            layout.addWidget(QPushButton(str(i+1)), i//3, i%3)
        layout.addWidget(QPushButton("+"), 3, 0)
        layout.addWidget(QPushButton("0"), 3, 1)
        layout.addWidget(QPushButton("="), 3, 2)

        '''
        layout.addWidget(QPushButton("1"), 0, 0)
        layout.addWidget(QPushButton("2"), 0, 1)     
        layout.addWidget(QPushButton("3"), 0, 2)
        layout.addWidget(QPushButton("4"), 1, 0)
        layout.addWidget(QPushButton("5"), 1, 1)
        layout.addWidget(QPushButton("6"), 1, 2)
        layout.addWidget(QPushButton("7"), 2, 0)
        layout.addWidget(QPushButton("8"), 2, 1)
        layout.addWidget(QPushButton("9"), 2, 2)
        '''

        self.setStyleSheet("background-color: #30f7fa;")
        self.setAutoFillBackground(True)

class TabTwo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        label = QLabel("This is the second tab.")
        layout.addWidget(label)
        self.setLayout(layout)
        self.setStyleSheet("background-color: #7fe0b2;")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window with Two Tabs")
        tabs = QTabWidget()
        tabs.addTab(TabOne(), "First Tab")
        tabs.addTab(TabTwo(), "Second Tab")
        self.setCentralWidget(tabs)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())