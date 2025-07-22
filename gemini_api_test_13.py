from flask import Flask
import gradio as gr
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")
model = genai.GenerativeModel("gemini-1.5-flash")

def chat_with_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

demo = gr.Interface(
    fn=chat_with_gemini,
    inputs=gr.Textbox(lines=2, label="입력"),
    outputs="text",
    title="Flask + Gradio Gemini 챗봇"
)

@app.route("/")

def home():
    return demo.launch(share=False, inline=True)

if __name__ == "__main__":
    app.run(debug=True)
