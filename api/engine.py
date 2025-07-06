from api.model_load import LLMLoad
from api.prompts import build_prompt
from api.memory import memory
from api.prompts import SYSTEM_PROMPT

llm = LLMLoad()

# Main callable from route
def run_chain(user_input: str, system_prompt=SYSTEM_PROMPT) -> str:
    prompt = build_prompt(user_input, memory, system_prompt)
    output = llm.invoke(prompt)
    memory.save_context({"input": user_input}, {"output": output})
    return output
