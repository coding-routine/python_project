import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(page_title="나의 첫 Streamlit 앱", page_icon="🚀", layout="centered")

# 제목
st.title("🚀 나의 첫 Streamlit 앱")
st.write("안녕하세요! 이건 Streamlit Cloud에 배포할 수 있는 **샘플 앱**입니다.")

# 입력 위젯
name = st.text_input("이름을 입력해 보세요", "홍길동")
st.write(f"반갑습니다, **{name}**님!")

# 간단한 데이터프레임
st.header("📊 샘플 데이터")
df = pd.DataFrame({
    "이름": ["철수", "영희", "민수", "지영"],
    "점수": [85, 92, 78, 90]
})
st.dataframe(df)

# Matplotlib 차트
st.header("📈 랜덤 데이터 시각화")
arr = np.random.randn(50)
fig, ax = plt.subplots()
ax.hist(arr, bins=10, color="skyblue", edgecolor="black")
st.pyplot(fig)

# 버튼 이벤트
if st.button("클릭하면 메시지 보여주기"):
    st.success("버튼을 눌렀습니다! 🎉")

# 이미지 표시
st.image("https://picsum.photos/600/300", caption="랜덤 샘플 이미지")
