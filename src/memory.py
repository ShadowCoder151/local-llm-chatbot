from langchain.memory import ConversationBufferMemory
from langchain.schema.messages import SystemMessage

from src.prompts import SYSTEM_PROMPT

def MemoryInit():
    memory = ConversationBufferMemory(
        memory_key="history",
        input_key="user_input",
        return_messages=True
    )

    memory.chat_memory.add_message(SystemMessage(SYSTEM_PROMPT))

    return memory