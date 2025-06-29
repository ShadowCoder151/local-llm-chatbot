from langchain_community.llms.llamacpp import LlamaCpp
import os

def LLMLoad(model_path: str = "models\\mistral-7b-instruct-v0.2.Q4_K_M.gguf"):
    llm = LlamaCpp(model_path=model_path,
            n_ctx=2048,
            n_threads=8,
            n_gpu_layers=-1,
            temperature=0.7,
            top_p=0.9, 
            verbose=False,
            streaming=False)

    return llm