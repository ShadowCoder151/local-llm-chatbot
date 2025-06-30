from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

from src.prompts import SYSTEM_PROMPT

def MemoryInit(chain):
    final_chain = RunnableWithMessageHistory(chain,
    lambda session_id: InMemoryChatMessageHistory(),
    input_messages_key="user_input",
    history_messages_key="history")

    # memory.chat_memory.add_message(SystemMessage(content=SYSTEM_PROMPT))

    return final_chain