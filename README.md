# local-llm-chatbot

As a part of learning LLMs in my LLM journey, a "HELLO WORLD" project, a minimal, open-source chatbot using [Mistral-7B-Instruct v0.2 GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)

---

## Tech Stack

| Layer      | Model      |
|---------------|--------------|
| LLM inference        | llama-cpp-python       |
| LLM orchestration        | LangChain       |
| Model        | [Mistral-7B-Instruct v0.2 GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)       |
| Environment        | `venv`, Python 3.12+       |
| Interface        | CLI (interactive prompt)       |
| Platform       | CPU + GPU switch      |

---

## Setup instructions

### 1. Clone the repo

```bash
git clone https://github.com/ShadowCoder151/local-llm-chatbot
cd local-llm-chatbot
```

### 2. Setup virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # or .\.venv\Scripts\activate on Windows
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Download the model
Model download link: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF

Place it in models folder
```bash
models/Mistral-7B-Instruct-v0.2.Q4_K_M.gguf
```

### 4. Run the chatbot:
```bash
python app.py
```

---

## Sample Output
```cmd
Enter the question:What is a neutron?
Answer: Neutrons are subatomic particles that have no charge and are identical to each other in terms of mass, which is approximately 1.67 x 10^-24 grams. Neutrons are fundamental constituents of the nucleus of an atom, along with protons. The number of neutrons in the nucleus of an atom determines the isotope of the element. For example, an atom of carbon-12 has 6 neutrons, while an atom of carbon-13 has 7. Neutrons are stable in the nucleus of most light and medium-mass elements, but they can be unstable in heavier nuclei and undergo a process called beta decay, transforming into a proton, an electron, and an antineutrino.
```

Note: You can customize the system prompt in prompts.py (What role should the chatbot play? in the code)
