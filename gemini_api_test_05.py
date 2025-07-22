import google.generativeai as genai
import gradio as gr

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

def chanbot(message, history):
    response = chat.send_message(message)
    return response.text

gr.ChatInterface(chanbot, title="Gemini Chatbot (Gradio)").launch()
