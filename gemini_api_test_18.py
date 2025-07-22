import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

genai.configure(api_key="AIzaSyCQ5GP9zHHwflUVrSb8I5xwBOJeQrF1vBE")

text_model = genai.GenerativeModel("gemini-2.5-flash")
vision_model = genai.GenerativeModel("gemini-2.5-flash")

# --------- 앱 UI ---------
st.set_page_config(page_title="Gemini AI 멀티툴", layout="centered")
st.title("🤖 Gemini AI 멀티툴 (챗봇 + 이미지 분석기)")

tab1, tab2 = st.tabs(["💬 텍스트 챗봇", "🖼️ 이미지 분석"])

# --------- 텍스트 챗봇 탭 ---------
with tab1:
    st.header("💬 Gemini Pro 텍스트 챗봇")

    if "chat" not in st.session_state:
        st.session_state.chat = text_model.start_chat(history=[])

    prompt = st.text_input("질문을 입력하세요:")

    if st.button("보내기", key="send_chat"):
        if prompt.strip():
            response = st.session_state.chat.send_message(prompt)
            st.markdown(f"**You:** {prompt}")
            st.markdown(f"**Gemini:** {response.text}")

            # 다운로드 기능 추가
            st.download_button(
                label="💾 대화 저장 (TXT)",
                data=f"사용자 질문: {prompt}\nGemini 응답: {response.text}",
                file_name="chat_result.txt",
                mime="text/plain"
            )

    st.markdown("---")
    st.subheader("📜 대화 기록")

    for msg in st.session_state.chat.history:
        role = msg.role.capitalize()
        content = msg.parts[0].text
        st.markdown(f"**{role}:** {content}")

# --------- 이미지 분석기 탭 ---------
with tab2:
    st.header("🖼️ Gemini Vision 이미지 분석기")

    uploaded_image = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="업로드한 이미지", use_column_width=True)

        vision_prompt = st.text_input("이미지에 대해 알고 싶은 내용을 입력하세요", value="이 이미지에 무엇이 보이나요?")

        if st.button("분석하기", key="analyze_image"):
            with st.spinner("분석 중..."):
                response = vision_model.generate_content([vision_prompt, image])
                st.subheader("🔎 Gemini의 응답:")
                st.write(response.text)

                # 다운로드 기능 추가
                result = f"[질문]: {vision_prompt}\n\n[분석 결과]:\n{response.text}"
                st.download_button(
                    label="💾 결과 저장 (TXT)",
                    data=result,
                    file_name="image_analysis.txt",
                    mime="text/plain"
                )
