import streamlit as st 
from streamlit_extras.add_vertical_space import add_vertical_space


# Step 1: Create sidebar content
with st.sidebar:
    st.title('LLM chat App')
    st.markdown('''
    # About
    This app is an LLM powered chat bot built using:
    - [streamlit] (https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
                
    ''')
    add_vertical_space(5)
    st.write('Learn this lesson from prompt engineer youtubu tutorial')