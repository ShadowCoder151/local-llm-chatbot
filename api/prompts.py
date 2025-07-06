# api/prompts.py
from langchain.prompts import PromptTemplate

SYSTEM_PROMPT = "Act as a helpful companion who answers any doubts only 60 words."

def build_prompt(user_input: str, memory, system_prompt: str = SYSTEM_PROMPT) -> str:
    chat_prompt = PromptTemplate(
        input_variables=["system_prompt", "history", "user_input"],
        template="""
        [INST]<<SYS>>{system_prompt}<</SYS>>
        {history}
        User: {user_input} [/INST]
        """.strip()
    )

    history_messages = memory.chat_memory.messages
    history_str = ""
    for msg in history_messages:
        if msg.type == "human":
            history_str += f"User: {msg.content}\n"
        elif msg.type == "ai":
            history_str += f"{msg.content}\n"

    return chat_prompt.format(system_prompt=system_prompt.strip(),
                               history=history_str.strip(),
                               user_input=user_input.strip())


# def HistoryString(memory_buffer: list):
#     hist = ""
#     for turn in memory_buffer:
#         if turn["role"] == "user":
#             hist += f"User: {turn['content']}\n"
#         elif turn["role"] == "assistant":
#             hist += f"{turn['content']}\n"
    
#     return hist.strip()
