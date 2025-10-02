from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

app = QApplication([])

# Main window
window = QWidget()
window.setWindowTitle("PyQt6 with CSS Example")

# Layout
layout = QGridLayout()
layout.addWidget(QPushButton("1"), 0, 0)
layout.addWidget(QPushButton("2"), 0, 1)
layout.addWidget(QPushButton("3"), 0, 2)
layout.addWidget(QPushButton("4"), 1, 0)
layout.addWidget(QPushButton("5"), 1, 1)
layout.addWidget(QPushButton("6"), 1, 2)
layout.addWidget(QPushButton("7"), 2, 0)
layout.addWidget(QPushButton("8"), 2, 1)
layout.addWidget(QPushButton("9"), 2, 2)
layout.addWidget(QPushButton("9"), 2, 2)
layout.addWidget(QPushButton("+"), 3, 0)
layout.addWidget(QPushButton("0"), 3, 1)
layout.addWidget(QPushButton("="), 3, 2)
window.setLayout(layout)

# Apply CSS (Qt Style Sheet)
window.setStyleSheet("""
    QWidget {
        background-color: #2e3440;
    }

    QPushButton {
        background-color: #5e81ac;
        color: #eceff4;
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 16px;
    }
    QPushButton:hover {
        background-color: #81a1c1;
    }
""")

window.resize(300, 150)
window.show()
app.exec()