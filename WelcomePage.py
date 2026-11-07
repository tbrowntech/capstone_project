import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

welcomeMsg = "Welcome to the AI Agent Analyzer."
promptMsg = "Please enter your prompt (max 200 characters)"

def introMessage():
    message.setText(welcomeMsg)
    
def getPrompt():
    prompt = text_box.text()
    message.setText(prompt)

def restart():
    text_box.clear()
    introMessage()

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("AI Agent Analyzer")
window.resize(500, 500)

message = QLabel("")
message.setAlignment(Qt.AlignCenter)
message.setWordWrap(True)

text_box = QLineEdit()
text_box.setMaxLength(200)
text_box.setPlaceholderText(promptMsg)

enter_button = QPushButton("Enter")
enter_button.clicked.connect(getPrompt)

restart_button = QPushButton("Restart")
restart_button.clicked.connect(restart)

layout = QVBoxLayout(window)
layout.addWidget(message)
layout.addWidget(text_box)

# Give all buttons the same width
for button in (enter_button, restart_button):
    button.setFixedWidth(125)
    layout.addWidget(button, alignment=Qt.AlignHCenter)

introMessage()

window.show()
sys.exit(app.exec())