from langchain_community.llms.llamacpp import LlamaCpp
from pathlib import Path
MODEL_PATH = "models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

class LLMLoad:
    def __init__(self):
        if not Path(MODEL_PATH).exists():
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
        self.llm = LlamaCpp(model_path=MODEL_PATH,
                            n_ctx=2048,
                            n_threads=4,
                            n_gpu_layers=-1,
                            temperature=0.7,
                            top_p=0.9, 
                            verbose=False,
                            streaming=False)

    def invoke(self, prompt: str) -> str:
        return self.llm(prompt)