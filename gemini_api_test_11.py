import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")
model = genai.GenerativeModel("gemini-1.5-flash")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("💬 Gemini 웹 챗봇")

prompt = st.text_input("질문을 입력하세요:")

if st.button("보내기"):
    if prompt.strip():
        response = st.session_state.chat.send_message(prompt)
        st.write(f"**Gemini:** {response.text}")
