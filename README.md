# 🚀 Learning GenAI using LangChain

This is my personal learning journey through GenAI tools and frameworks — primarily focused on LangChain, Google Gemini, and Hugging Face.  
It contains code for working with prompts (static & dynamic), chat models, embedding models, and more.

---

## 📂 Project Structure

```
learning_genai_by_langchain/
├── langchain_models/         # Base venv + general LangChain testing
│   ├── chatmodels/           # Chat models (Gemini, Hugging Face, etc.)
│   ├── embeddingmodels/      # Embedding models (Gemini, Hugging Face, etc.)
├── langchain_prompts/        # Prompt engineering (prompt_static.py, prompt_dynamic.py)
├── test.py                   # Test script
├── .env                      # For storing API keys
├── .gitignore                # Files/folders to ignore
├── requirements.txt          # Dependencies
```

---

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
