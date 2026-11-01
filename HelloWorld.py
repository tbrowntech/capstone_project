import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

def say_hello():
    message.setText("hello world")

def restart():
    message.setText("")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Hello World")
window.resize(200, 150)

enter_button = QPushButton("Enter")
enter_button.clicked.connect(say_hello)

message = QLabel("")
message.setAlignment(Qt.AlignCenter)

restart_button = QPushButton("Restart")
restart_button.clicked.connect(restart)

layout = QVBoxLayout(window)
layout.addWidget(enter_button)
layout.addWidget(message)
layout.addWidget(restart_button)

window.show()
sys.exit(app.exec())