from llama_cpp import Llama

llm = Llama(model_path="models\\mistral-7b-instruct-v0.2.Q4_K_M.gguf",
            n_ctx=2048,
            n_threads=8,
            n_gpu_layers=-1,
            verbose=False)

system_prompt = "Act as a helpful companion."

chat_history = []

# Loop based CLI
while True:
    user_input = input("Enter the question:")
    if user_input.lower() == "exit":
        print("Exiting chat")
        exit(0)

    chat_history.append({"role" : "user", "content" : user_input})

    prompt = f"""
    <s>[INST]<<SYS>>{system_prompt}<</SYS>> {user_input} [/INST]
    """

    for turn in chat_history:
        prompt += f"{turn['content']}\n[/INST]"

    response = llm(prompt, max_tokens=256)
    output = response["choices"][0]["text"].strip()

    chat_history.append({"role" : "assistant", "content" : output})

    print(f"Answer: {output}")
    print('-' * 40)
