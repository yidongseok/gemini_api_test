import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")

model = genai.GenerativeModel("gemini-1.5-flash")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    
st.title("🧠 Gemini 텍스트 챗봇")

user_input = st.text_input("질문을 입력하세요:", key="input")

if st.button("보내기") and user_input:
    response = st.session_state.chat.send_message(user_input)
    st.markdown(f"**You : ** {user_input}")
    st.markdown(f"**Gemini : ** {response.text}")

st.markdown("---")
st.subheader("🕘 이전 대화")
for msg in st.session_state.chat.history:
    st.markdown(f"**{msg.role.capitalize()} : ** {msg.parts[0].text}")
