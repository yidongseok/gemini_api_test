import google.generativeai as genai
import gradio as gr

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_code(prompt):
    full_prompt = f"다음 요청에 맞는 코드를 생성해줘:\n\n{prompt}"
    
    response = model.generate_content(full_prompt)
    return response.text

gr.Interface(
    fn=generate_code,
    inputs=gr.Textbox(lines=5, label="코드 요청 또는 질문을 입력하세요", placeholder="코드 생성 요청을 입력하세요..."),
    outputs="text",
    title="💻 Gemini 코드 생성 도우미",
    description="프로그래밍 요청을 입력하면 Gemini가 코드를 생성해줍니다."
).launch()
