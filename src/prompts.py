from langchain.prompts import PromptTemplate

SYSTEM_PROMPT = "Act as a helpful companion who answers any doubts only 60 words."

chat_prompt = PromptTemplate(input_variables=["system_prompt", "history", "user_input"],
                             template="""
    [INST]<<SYS>>{system_prompt}<</SYS>> 
    {history}
    User: {user_input} [/INST]
    """.strip())

# def HistoryString(memory_buffer: list):
#     hist = ""
#     for turn in memory_buffer:
#         if turn["role"] == "user":
#             hist += f"User: {turn['content']}\n"
#         elif turn["role"] == "assistant":
#             hist += f"{turn['content']}\n"
    
#     return hist.strip()
