import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🖼️ Gemini Vision 이미지 분석기")

# 이미지 업로드
uploaded_image = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="업로드한 이미지", use_column_width=True)

    # 설명 프롬프트 입력
    prompt = st.text_input("이미지에 대해 알고 싶은 내용을 입력하세요", value="이 이미지에 무엇이 보이나요?")

    if st.button("분석하기"):
        with st.spinner("분석 중..."):
            response = model.generate_content([prompt, image])
            st.subheader("🔎 Gemini의 응답:")
            st.write(response.text)
