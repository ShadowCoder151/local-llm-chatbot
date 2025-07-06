# ui/widgets.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel, QScrollArea
from PyQt6.QtCore import pyqtSignal

class QuestionBox(QWidget):
    submitted = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Type your question here...")
        self.submit_btn = QPushButton("Send")
        self.submit_btn.clicked.connect(self.send_input)

        layout.addWidget(self.input_box)
        layout.addWidget(self.submit_btn)
        self.setLayout(layout)

    def send_input(self):
        text = self.input_box.toPlainText().strip()
        if text:
            self.submitted.emit(text)
            self.input_box.clear()

class ResponseBox(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.response_area = QLabel()
        self.response_area.setWordWrap(True)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.response_area)

        layout.addWidget(scroll)
        self.setLayout(layout)

    def display_response(self, text):
        self.response_area.setText(text)
