import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")
model = genai.GenerativeModel("gemini-2.5-flash")

# 세션 상태로 대화 유지
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("💬 Gemini Pro 텍스트 챗봇")

# 사용자 입력 받기
prompt = st.text_input("질문을 입력하세요:")

if st.button("보내기") and prompt.strip():
    response = st.session_state.chat.send_message(prompt)
    st.markdown(f"**You:** {prompt}")
    st.markdown(f"**Gemini:** {response.text}")

# 대화 내역 표시
st.markdown("---")
st.subheader("📜 대화 기록")

for msg in st.session_state.chat.history:
    role = msg.role.capitalize()
    content = msg.parts[0].text
    st.markdown(f"**{role}:** {content}")
