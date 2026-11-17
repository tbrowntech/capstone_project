from PySide6.QtWidgets import QHBoxLayout

button_row = QHBoxLayout()
button_row.addStretch()
for button in (enter_button, restart_button):
    button_row.addWidget(button)
button_row.addStretch()

layout.addLayout(button_row)