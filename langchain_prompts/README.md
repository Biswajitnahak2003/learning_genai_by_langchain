# 🧠 LangChain Prompt Engineering Projects

Welcome to the **LangChain Prompt Engineering** project repository!  
This collection showcases multiple GenAI mini-projects using LangChain to build, test, and optimize LLM prompts for various use cases.

---

## 📁 Project Structure

langchain_prompts/
│
├── prompt_static.py # Simple static prompt example
├── prompt_dynamic.py # Dynamic prompt template using PromptTemplate
├── chatbot_static.py # Static chatbot using LangChain prompt for conversation with history stored
├── chat_prompt_templte.py # Custom ChatPromptTemplate for dynamic chatbot
├── message_placeholder.py # Handles message from history
├── prompt_generator.py # Template to reuse saved in a json file 
├── chat_history.txt # history content stored from conversation
├── template.json # (in parent directory) JSON template for dynamic prompts
└── README.md # You're reading it :)


---

## 🚀 What's Implemented

###  `prompt_static.py`
- Demonstrates a basic static prompt

###  `prompt_dynamic.py`
- Builds prompts from external template file (`template.json`)
- Accepts dynamic user inputs (e.g., topic, tone, format)

###  `chat_prompt_templte.py`
- Builds a dynamic chatbot based on pre-defined prompt logic
- Organizes messages with placeholders and roles

### ✅ `chatbot_static.py`
- Builds a static chatbot based on pre-defined prompt logic
- Supports integration with history and memory

### ✅ `message_placeholder.py`
- Manages placeholder variables like `{input}`, `{history}`
- Keeps context tracking clean and modular

---

## 📦 Dependencies

Make sure your virtual environment is activated and install the following:

```bash
pip install langchain langchain-google-genai python-dotenv

📚 References

    LangChain Docs

    OpenAI API

    Prompt Engineering Guide

👨‍💻 Author

by Biswajit Nahak
Feel free to contribute or fork this repo!


