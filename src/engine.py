from src.model_load import LLMLoad
from src.prompts import chat_prompt
from src.memory import MemoryInit

class ChatEngine:
    def __init__(self, system_prompt:str):
        self.system_prompt = system_prompt
        # LLM invoke (no control over prompt)
        self.llm = LLMLoad()
        # LLM Chain
        chain = chat_prompt | self.llm
        # Memory Load + Final conversational chain
        self.memory_chain = MemoryInit(chain)

    def chat(self, user_input:str):
        output = self.memory_chain.invoke({"user_input": user_input, "system_prompt" : self.system_prompt}, config={"configurable": {"session_id": "chat1"}})
        return output.strip()