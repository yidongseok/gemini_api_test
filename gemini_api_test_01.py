import google.generativeai as genai

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")
model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content("안녕하세요, Gemini!")
print(response.text)
