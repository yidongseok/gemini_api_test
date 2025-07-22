# 13. [2주차] 클라우드 배포 (Streamlit Cloud or Vercel), PDF 저장 기능 추가, 음성 입력 출력 기능, 채팅 이미지 결과 DB 저장
from fpdf import FPDF
import streamlit as st
import google.generativeai as genai

def generate_pdf(content, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True)
    pdf.set_font("Arial", size=12)

    for line in content.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True)

    pdf.output(filename)

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")
model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("안녕하세요, Gemini!")

if st.button("📄 PDF 저장"):
    content = f"질문: 안녕하세요, Gemini!\n\n답변: {response.text}"
    generate_pdf(content, "gemini_result.pdf")

    with open("gemini_result.pdf", "rb") as file:
        st.download_button("💾 PDF 다운로드", file, "result.pdf")
