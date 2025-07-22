import google.generativeai as genai
import gradio as gr

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")

model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_image(image):
    if image is None:
        return "이미지를 업로드 해 주세요"
    response = model.generate_content(["이 이미지를 설명해 줘.", image])
    return response.text

demo = gr.Interface(
    fn=analyze_image,
    inputs=gr.Image(type="pil", label="이미지 업로드"),
    outputs="text",
    title="📷 Gemini 이미지 분석기",
    description="업로드한 이미지를 분석하고 설명을 생성합니다."
)

demo.launch()
