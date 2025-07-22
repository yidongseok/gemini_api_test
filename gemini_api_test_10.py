import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("💻 Gemini 코드 생성 도우미")

prompt = st.text_area("코드 생성 요청을 입력하세요 (예: '파이썬으로 이진 탐색 구현해줘')", height=200)

if st.button("코드 생성하기"):
    if prompt.strip() == "":
        st.warning("요청 내용을 입력해주세요.")
    else:
        with st.spinner("Gemini가 코드를 생성 중입니다..."):
            full_prompt = f"다음 요청에 맞는 코드를 생성해줘:\n\n{prompt}"
            response = model.generate_content(full_prompt)
            st.code(response.text, language="python")
