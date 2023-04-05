import streamlit as st
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI 

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
SERPAPI_API_KEY = st.secrets["SERPAPI_API_KEY"]


user_input = st.text_input("Enter Your Question :")

@st.cache_data(persist=True)
def serp(user_input):
    llm = OpenAI(temperature=0)
    tool_names = ["serpapi"]
    tools = load_tools(tool_names)
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

    result = agent.run(user_input)
    return result
  

if user_input:
    answer = serp(user_input)
    st.write(answer)
else:
  st.error("Enter your input")
