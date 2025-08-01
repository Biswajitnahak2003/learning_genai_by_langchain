# 📦 LangChain Structured Output with Google Gemini

This module explores structured output parsing in LangChain using Google Gemini (`gemini-1.5-flash`).  
It demonstrates how to extract and validate structured data from natural language responses.

---

## 📁 Files Overview

### ✅ `using_pydantic.py`
Uses `pydantic.BaseModel` to define a structured schema for extracting product review info such as:
- Key themes
- Summary
- Sentiment
- Pros & Cons
- Reviewer name

**Method**: `llm.with_structured_output(Review)`  
Use case: product reviews / feedback summarization.

---

### ✅ `schema.json` + `main_json_schema.py`
Defines a user profile schema using a JSON Schema file:
```json
{
  "name": "John Doe",
  "email": "john.doe@email.com",
  "is_premium_member": true
}
