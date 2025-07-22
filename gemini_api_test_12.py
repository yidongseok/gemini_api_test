import gradio as gr
import google.generativeai as genai

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_code(prompt):
    response = model.generate_content(f"다음 요청에 맞는 코드를 생성해줘:\n{prompt}")
    return response.text

gr.Interface(
    fn=generate_code,
    inputs=gr.Textbox(lines=4, label="코드 요청"),
    outputs="text",
    title="🧑‍💻 Gemini 코드 생성기"

).launch()
