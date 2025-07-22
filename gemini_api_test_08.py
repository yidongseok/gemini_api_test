import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🖼️ Gemini 이미지 분석기")

# 이미지 업로드
uploaded_image = st.file_uploader("이미지를 업로드하세요", type=["png", "jpg", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="업로드된 이미지", use_column_width=True)

    # 버튼 클릭 시 분석
    if st.button("분석하기"):
        response = model.generate_content(["이 이미지를 설명해줘.", image])
        st.subheader("📄 분석 결과:")
        st.write(response.text)

