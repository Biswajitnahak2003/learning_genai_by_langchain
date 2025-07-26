from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(
    page_title = "multiprompt ai assistant",
    page_icon = "✨",
    layout = "wide"
)

st.title("The AI summarizer")
st.write("tell what you want to summarize.i will take care of the rest!!")

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

## template
template = """
explain the topic "{topic}"
with the explaination style of "{style}"
within the length of "{length}"words.
"""

prompt_template = PromptTemplate.from_template(template)

user_input = st.text_input("Enter the topic you want to understand:")
style = st.selectbox("Select the style of explanation:", ["simple", "detailed", "technical"])
length = st.selectbox("Select the length of the explanation:", ["short", "medium", "long"])

prompt = prompt_template.format(
    topic=user_input,
    style=style,
    length=length
)

if st.button("Summarize"):
    result = llm.invoke(prompt)
    st.write(result)

