import streamlit as st
import streamlit.components.v1 as components
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI

st.set_page_config(page_title="ChatGptWithGoogle", page_icon="🤖", layout="wide")


st.title("ChatGPT + Google")
user_input = st.text_input("Ask me anything: Hi, I am Google")

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
GOOGLE_CSE_ID = st.secrets["GOOGLE_CSE_ID"]

@st.cache(persist=True, allow_output_mutation=True)
def googlesearch(user_input):
    tool_names = ["google-search"]
    tools = load_tools(tool_names)
    llm = ChatOpenAI(temperature=0)
    agent_chain = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    template = f"""Question: {user_input}

    Answer: Let's think step by step."""

    result = agent_chain.run(template)
    return result

if user_input:
    result = googlesearch(user_input)
    st.success(result)
else:
    st.error("Enter your input")
    
st.markdown("Made with ❤️ by [Aenish Shrestha](https://twitter.com/aenish_shrestha).")

components.iframe("https://aenishshrestha.substack.com/embed",height=500)
