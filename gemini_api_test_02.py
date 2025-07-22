import google.generativeai as genai
from PIL import Image
import io

# API 키 설정
genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")

# 이미지 열기
image_path = "example.png"
image = Image.open(image_path)

# 모델 초기화
model = genai.GenerativeModel('gemini-2.5-flash')

# 텍스트 + 이미지 입력
prompt = "이 이미지에 무엇이 보이나요?"
response = model.generate_content([prompt, image])

# 출력
print(response.text)
