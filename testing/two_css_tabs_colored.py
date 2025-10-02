from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget, QGridLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

app = QApplication([])

tab_widget = QTabWidget()
tab_widget.setTabPosition(QTabWidget.TabPosition.North)

# Create two tabs
tab1 = QWidget()
tab2 = QWidget()
# Remove this placeholder and the comment.
# The correct way is to add tabs with desired names using tab_widget.addTab(tab, "Tab Name") after setting up the tab content.
tab_widget.setWindowTitle("My Two Colored CSS Tabs")
# Add some content
tab1_layout = QGridLayout()
tab1_layout.addWidget(QLabel("This is Tab 1"))
tab1.setLayout(tab1_layout)

tab1_layout.addWidget(QPushButton("1"), 0, 0)
tab1_layout.addWidget(QPushButton("2"), 0, 1)     
tab1_layout.addWidget(QPushButton("3"), 0, 2)
tab1_layout.addWidget(QPushButton("4"), 1, 0)
tab1_layout.addWidget(QPushButton("5"), 1, 1)
tab1_layout.addWidget(QPushButton("6"), 1, 2)
tab1_layout.addWidget(QPushButton("7"), 2, 0)
tab1_layout.addWidget(QPushButton("8"), 2, 1)
tab1_layout.addWidget(QPushButton("9"), 2, 2)
tab1_layout.addWidget(QPushButton("+"), 3, 0)
tab1_layout.addWidget(QPushButton("0"), 3, 1)
tab1_layout.addWidget(QPushButton("="), 3, 2)

tab2_layout = QGridLayout()
tab2_layout.addWidget(QLabel("This is Tab 2"))
tab2.setLayout(tab2_layout)

tab2_layout.addWidget(QPushButton("1"), 0, 0)
tab2_layout.addWidget(QPushButton("2"), 0, 1)     
tab2_layout.addWidget(QPushButton("3"), 0, 2)
tab2_layout.addWidget(QPushButton("4"), 0, 3)
tab2_layout.addWidget(QPushButton("5"), 1, 0)
tab2_layout.addWidget(QPushButton("6"), 1, 1)
tab2_layout.addWidget(QPushButton("7"), 1, 2)
tab2_layout.addWidget(QPushButton("8"), 1, 3)
tab2_layout.addWidget(QPushButton("9"), 2, 0)
tab2_layout.addWidget(QPushButton("a"), 2, 1)
tab2_layout.addWidget(QPushButton("b"), 2, 2)
tab2_layout.addWidget(QPushButton("c"), 2, 3)
tab2_layout.addWidget(QPushButton("d"), 3, 0)
tab2_layout.addWidget(QPushButton("e"), 3, 1)
tab2_layout.addWidget(QPushButton("f"), 3, 2)
tab2_layout.addWidget(QPushButton("0"), 3, 3)
tab2_layout.addWidget(QPushButton("+"), 4, 0)
tab2_layout.addWidget(QPushButton("-"), 4, 1)
tab2_layout.addWidget(QPushButton("*"), 4, 2)
tab2_layout.addWidget(QPushButton("="), 4, 3)

tab_widget.addTab(tab1, "Decimal")
tab_widget.addTab(tab2, "Hexadecimal")


# Set the background color of the whole tab widget (not just the pages)
tab_widget.setStyleSheet("""
QTabWidget::pane {
    background: #87ceeb; /* Light blue */
    border: 1px solid #444;
}
QTabBar::tab {
    background: #000;
    color: #333;
    padding: 8px;
    border: 1px solid #888;
    border-bottom: none;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}
QTabBar::tab:selected {
    background: #fff;
    color: #000;
}
QTabBar::tab:hover {
    background: #999;
}
QPushButton {
    background-color: #aa00cc; /*  */
}
""")

tab_widget.resize(400, 200)
tab_widget.show()
app.exec()