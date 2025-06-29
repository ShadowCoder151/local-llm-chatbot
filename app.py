from src.model_load import LLMLoad
from src.prompts import chat_prompt, SYSTEM_PROMPT, HistoryString

# LLM invoke (no control over prompt)
llm = LLMLoad()
response = llm.invoke("What is your name?")
print(response)

# Main prompt to be sent
history = [
    {"role": "user", "content": "What is your name?"},
    {"role": "assistant", "content": "My name is Max"},
    {"role": "user", "content": "What is all this?"},
    {"role": "assistant", "content": "This is rocket"}
]

formatted_prompt = chat_prompt.format(
    system_prompt=SYSTEM_PROMPT,
    history=HistoryString(history),
    user_input="Meaning of your name."
)

print(formatted_prompt)
