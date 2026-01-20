import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
st.set_page_config(
    page_title="Chat UI",
    page_icon="💬",
    layout="centered"
)
llm = ChatGroq(
    temperature=0.9,
    model="llama-3.1-8b-instant"
)

st.markdown("""
<style>
.chat-container {
    max-width: 720px;
    margin: auto;
}
.user-msg {
    background-color: #DCF8C6;
    padding: 12px;
    border-radius: 10px;
    margin: 8px 0;
    text-align: right;
}
.bot-msg {
    background-color: #F1F0F0;
    padding: 12px;
    border-radius: 10px;
    margin: 8px 0;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

st.title("💬 Chat")
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Send a message...")

if user_input:
    # 1️⃣ Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # 2️⃣ Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # 3️⃣ Call LangChain HERE
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(user_input)
            answer = response.content
            st.markdown(answer)

    # 4️⃣ Save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
