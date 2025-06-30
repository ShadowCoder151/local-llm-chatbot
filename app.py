from src.model_load import LLMLoad
from src.prompts import chat_prompt, SYSTEM_PROMPT
from src.memory import MemoryInit
# from langchain.chains.llm import LLMChain


def main():
    print("Welcome to the chatbot.")

    # LLM invoke (no control over prompt)
    llm = LLMLoad()

    # LLM Chain
    chain = chat_prompt | llm

    # Memory Load + Final conversational chain
    memory_chain = MemoryInit(chain)


        
    # Loop based CLI
    while True:
        user_input = input("Enter the question:")
        if user_input.lower() == "exit":
            print("Exiting chat")
            exit(0)

        try:
            output = memory_chain.invoke({"user_input": user_input, "system_prompt" : SYSTEM_PROMPT}, config={"configurable": {"session_id": "chat1"}})
            print(f"Answer: {output.strip()}")
        except Exception as e:
            print(f"Error in answering your question {e}")
        print('-' * 40)

if __name__ == "__main__":
    main()
