from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QInputDialog
from PyQt6.QtCore import QThreadPool
from ui.widgets import QuestionBox, ResponseBox
from ui.worker import QueryWorker

class ChatUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Local LLM Chatbot")
        self.setMinimumSize(1000, 600)
        self.thread_pool = QThreadPool()  

        self.system_prompt = self.ask_system_prompt()

        central_widget = QWidget()
        layout = QHBoxLayout()

        self.question_box = QuestionBox()
        self.response_box = ResponseBox()

        self.question_box.submitted.connect(self.process_query)

        layout.addWidget(self.question_box, 1)
        layout.addWidget(self.response_box, 2)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def ask_system_prompt(self):
        prompt, ok = QInputDialog.getText(self, "System Prompt", "Set the assistant's behavior:")
        if ok and prompt.strip():
            return prompt.strip()
        else:
            return "Act as a helpful assistant."

    def process_query(self, user_input: str):
        worker = QueryWorker(user_input, self.system_prompt)
        worker.signals.finished.connect(self.response_box.display_response)
        worker.signals.error.connect(self.response_box.display_response)
        self.thread_pool.start(worker)
