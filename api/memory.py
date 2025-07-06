from langchain.memory import ConversationBufferMemory
from langchain_core.chat_history import InMemoryChatMessageHistory

# Global memory object
memory = ConversationBufferMemory(
    memory_key="history",
    input_key="input",  
    chat_memory=InMemoryChatMessageHistory(return_messages=True)
)