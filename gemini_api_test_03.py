import google.generativeai as genai

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")

# 챗봇 초기화
model = genai.GenerativeModel('gemini-2.5-flash')
chat = model.start_chat(history=[])

# 사용자 입력 반복
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)
