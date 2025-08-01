# 🚀 Learning GenAI using LangChain

This is my personal learning journey through GenAI tools and frameworks — primarily focused on LangChain, Google Gemini, and Hugging Face.  
It contains code for working with prompts (static & dynamic), chat models, embedding models, and more.

learning_genai_by_langchain/

├── langchain_models/                            # Base venv + general LangChain model testing
│   ├── chatmodels/                              # Chat model examples (OpenAI, Gemini, HuggingFace, etc.)
│   └── embeddingmodels/                         # Embedding model examples (OpenAI, Gemini, HuggingFace, etc.)

├── langchain_prompts/                           # Prompt engineering and chatbot demos
│   ├── prompt_static.py                         # Static prompt example using basic PromptTemplate
│   ├── prompt_dynamic.py                        # Dynamic prompt using variables and JSON template
│   ├── chatbot_static.py                        # Simple static chatbot with LangChain
│   ├── chat_prompt_templte.py                   # Custom ChatPromptTemplate class example
│   ├── message_placeholder.py                   # MessagePlaceholder demo (chat formatting support)
│   ├── prompt_generator.py                      # Generates prompts dynamically from template.json
│   ├── chat_history.txt                         # Sample I/O from chatbot testing
│   ├── template.json                            # JSON-based prompt structure used in dynamic prompt
│   └── README.md                                 # Documentation for all prompt-related files

├── structured_output/                           # Structured output parsing demos
│   ├── structured_openai_jsonschema.py          # Using OpenAI's native structured output (tool_choice / response_format)
│   ├── structured_jsonparser.py                 # JSONOutputParser example for general models
│   ├── structured_stringparser.py               # StringOutputParser for basic use-cases
│   ├── structured_pydanticparser.py             # PydanticOutputParser to parse outputs into models
│   ├── schema_definitions.py                    # Shared Pydantic models or JSON schema definitions
│   └── README.md                                 # Full explanation of structured output strategies

├── test.py                                      # General test file for quick experimentation

├── .env                                         # API keys for OpenAI, Gemini, etc. (not committed)

├── .gitignore                                   # Git ignore file for venv, .env, etc.

├── requirements.txt                             # All required Python packages

└── README.md                                    # Main project documentation


## ⚙️ Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/your-username/learning_genai_by_langchain.git
cd learning_genai_by_langchain
```

### 🐍 2. Create & Activate Virtual Environment

```bash
python -m venv langchain-env
.\langchain-env\Scripts\activate    # On Windows
# source langchain-env/bin/activate  # On Linux/Mac
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 4. Setup `.env` file

Create a `.env` file in the root folder with the following:

```env
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACE_ACESS_TOKEN=your_HF_acess_token
```

---

## 🧑‍💻 Author

**Biswajit Nahak**  
> Final-year student | B.Tech ETC @IIIT BBSR

---

## 📜 License

This repository is for learning and educational purposes only.
