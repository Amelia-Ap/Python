import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel

def main():
    app = QApplication(sys.argv)

    # Main window
    window = QWidget()
    window.setWindowTitle("Interactive PyQt6 Example")
    window.resize(600, 600)

    # Layout
    layout = QGridLayout()
    layout.addWidget(QLabel("Welcome to the interactive PyQt6 application!"))

    # Label
    label = QLabel("Hello, PyQt6!")
    layout.addWidget(label)

    # Button
    button = QPushButton("Click me")
    layout.addWidget(button)

    # Define what happens when button is clicked
    def on_button_click():
        label.setText("Button clicked!")

    button.clicked.connect(on_button_click)

    # Apply layout and show window
    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
