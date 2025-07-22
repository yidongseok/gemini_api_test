from PIL import Image
import google.generativeai as genai

image = Image.open("example.png")

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")
model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(["이 이미지에 뭐가 있나요?", image])
print(response.text)
