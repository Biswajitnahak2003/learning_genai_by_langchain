# 🚀 Learning GenAI using LangChain

This is my personal learning journey through GenAI tools and frameworks — primarily focused on LangChain, Google Gemini, and Hugging Face.  
It contains code for working with prompts (static & dynamic), chat models, embedding models, and more.

📦 learning_genai_by_langchain/
│
├── langchain_models/                    # Base venv + general LangChain model testing
│   ├── chatmodels/                      # Chat models (Gemini, Hugging Face, etc.)
│   └── embeddingmodels/                 # Embedding models (Gemini, Hugging Face, etc.)
│
├── langchain_prompts/                  # Prompt engineering and chatbot prompts
│   ├── prompt_static.py                # Simple static prompt example
│   ├── prompt_dynamic.py               # Dynamic prompt template using variables
│   ├── chatbot_static.py               # Static chatbot using LangChain prompt
│   ├── chat_prompt_templte.py          # Custom ChatPromptTemplate class
│   ├── message_placeholder.py          # Handles message placeholders
│   ├── prompt_generator.py             # Generates prompts from templates
│   ├── chat_history.txt                # Sample input/output from chatbot
│   ├── template.json                   # JSON template for dynamic prompts (if used)
│   └── README.md                       # You're reading it :)
│
├── test.py                             # General test script
├── .env                                # For storing API keys (e.g., OpenAI, Gemini)
├── .gitignore                          # Files/folders to ignore in version control
├── requirements.txt                    # Python dependencies (LangChain, etc.)
└── README.md                           # Project overview and usage instructions


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
