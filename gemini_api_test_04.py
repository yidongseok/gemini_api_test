import google.generativeai as genai

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")

model = genai.GenerativeModel('gemini-2.5-flash')

# 버그가 있는 코드 입력
buggy_code = """
def calculate_area(radius):
    area = pi * r^2
    return area
"""

prompt = f"다음 코드에서 오류를 찾고 수정한 후 설명해주세요:\n{buggy_code}"

response = model.generate_content(prompt)

print(response.text)
