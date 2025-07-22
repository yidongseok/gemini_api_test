from flask import Flask
import gradio as gr
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")
model = genai.GenerativeModel("gemini-2.5-flash")

# 텍스트 생성 요청
prompt = "한국의 여름 날씨는 어떤 특징이 있나요?"
response = model.generate_content(prompt)

# 출력
print("📝 Gemini의 응답:")
print(response.text)
