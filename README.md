# 🚀 Learning GenAI using LangChain

This is my personal learning journey through GenAI tools and frameworks — primarily focused on [LangChain](https://www.langchain.com/), [Google Gemini](https://ai.google.dev/), and [Hugging Face](https://huggingface.co/).
It contains code for working with prompts, chat models, embedding models, and more.

---

## 📂 Project Structure

```
learning_genai_by_langchain/
├── langchain_models/         # Base venv + general LangChain testing
│   ├── chatmodels/           # Chat models(by opensource(gemini) and hf_acess_token or by downloading to local)
│   ├── embeddingmodels/      # Embedding models(by opensource(gemini) and hf_acess_token or by downloading to local)
├── langchain_prompts/        # Prompt
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
.\langchain-env\Scripts\activate
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 4. Setup `.env` file

Create a `.env` file in the root folder with the following :

```env
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACE_ACESS_TOKEN=your_HF_acess_token

---

## 🧑‍💻 Author

**Biswajit Nahak**  
> final-year student | Btech ETC @IIIT BBSR

---

## 📜 License

This repository is for learning and educational purposes only.
