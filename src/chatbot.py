from llama_cpp import Llama

llm = Llama(model_path="models\\mistral-7b-instruct-v0.2.Q4_K_M.gguf",
            n_ctx=2048,
            n_threads=8,
            verbose=False)

system_prompt = "Act as a helpful and concise professor who is an expert in Physics."

# One time q/a

user_input = input("Enter the question:")

prompt = f"""
<s>[INST]<<SYS>>{system_prompt}<</SYS>> {user_input} [/INST]
"""

response = llm(prompt, max_tokens=256)

output = response["choices"][0]["text"].strip()

print(f"Answer: {output}")
