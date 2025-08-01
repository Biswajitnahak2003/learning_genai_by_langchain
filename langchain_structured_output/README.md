# LangChain Structured Output with Gemini 1.5 Flash

This folder demonstrates how to **parse, validate, and extract structured outputs** from **Gemini 1.5 Flash** using [LangChain](https://www.langchain.com/).

You'll find multiple approaches for handling structured outputs:
- ✅ Using **Pydantic models**
- ✅ Using **JSON Schemas**
- ✅ Using **Output Parsers** like `JsonOutputParser` and `StrOutputParser` and more to be updated soon

---

## 📁 Folder Structure

langchain_structured_output/
├── using_pydantic.py # Validates Gemini output with a pydantic.BaseModel
├── schema.json # JSON Schema definition for a user profile
├── main_json_schema.py # Validates Gemini output using schema.json
├── str_op_parser.py # Uses StrOutputParser for direct string response
└── json_op_parser.py # Uses JsonOutputParser for dictionary-like parsing


---

##  Tech Stack

- **LLM**: Gemini 1.5 Flash (`google/gemini-pro`)
- **Framework**: LangChain
- **Validation**: Pydantic and JSON Schema
- **Prompt Handling**: `ChatPromptTemplate`, `Output Parsers`

---

## 📜 Scripts Overview

| Script | Description |
|--------|-------------|
| `using_pydantic.py` | Parses Gemini's output into a custom `Review` Pydantic model containing product, rating, and sentiment. |
| `schema.json` | Schema file describing fields like `name`, `email`, and `is_premium_user` for validating model responses. |
| `main_json_schema.py` | Loads `schema.json` and validates Gemini output using `.with_structured_output(schema=schema)`. |
| `str_op_parser.py` | Uses `StrOutputParser` to get plain text from the model with minimal formatting. |
| `json_op_parser.py` | Uses `JsonOutputParser` with a format instruction to get dictionary-formatted output. |

---

##  Sample Output

### `json_op_parser.py`

python
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
<class 'dict'>

using_pydantic.py

Review(product='Sony WH-1000XM4', rating=4.5, sentiment='positive')
<class '__main__.Review'>

📌 How to Run

Make sure you're using a virtual environment with langchain and google.generativeai installed:

pip install -r requirements.txt

Then run any script like:

python json_op_parser.py

📌 Notes

    These scripts assume your GOOGLE_API_KEY is set as an environment variable.

    You can modify the prompt templates to experiment with different schemas or model behaviors.

    All outputs are validated before printing — any mismatch will throw a validation error.

📌 Author

Biswajit Nahak

    Final-Year B.Tech ETC Student @ IIIT Bhubaneswar


