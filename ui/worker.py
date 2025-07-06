# ui/worker.py
from PyQt6.QtCore import QObject, pyqtSignal, QRunnable, QThreadPool
import httpx

class QuerySignals(QObject):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

class QueryWorker(QRunnable):
    def __init__(self, user_input: str, system_prompt: str):
        super().__init__()
        self.user_input = user_input
        self.system_prompt = system_prompt
        self.signals = QuerySignals()

    def run(self):
        try:
            payload = {
                "user_input": self.user_input,
                "system_prompt": self.system_prompt
            }
            with httpx.Client(timeout=60.0) as client:
                res = client.post("http://localhost:8000/chat/", json=payload)
                res.raise_for_status()
                output = res.json().get("response", "[No response received]")
                self.signals.finished.emit(output)
        except Exception as e:
            self.signals.error.emit(f"[Error] {str(e)}")
