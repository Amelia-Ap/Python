from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

app = QApplication([])

window = QWidget()
window.setWindowTitle("QGridLayout Example")

layout = QGridLayout()

layout.addWidget(QPushButton("Button 1"), 0, 0)
layout.addWidget(QPushButton("Button 2"), 0, 1)
layout.addWidget(QPushButton("Button 3"), 1, 0)
layout.addWidget(QPushButton("Button 4"), 1, 1)

window.setLayout(layout)
window.show()

app.exec()