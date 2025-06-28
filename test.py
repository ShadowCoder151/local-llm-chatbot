from llama_cpp import Llama

llm = Llama(
    model_path="models\\mistral-7b-instruct-v0.2.Q4_K_M.gguf",  # Use a GGUF model file here
    n_gpu_layers=-1,                       # Offload all layers to GPU
    verbose=True                           # Enable detailed logs
)