import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(page_title="이차함수의 그래프 기본형(y=ax²) 분석하기", page_icon="📈")
st.title("📈 이차함수의 그래프 기본형 (y = a·x²) 분석하기")

st.write("""
이 앱은 **이차함수의 기본형 y = a·x²** 그래프를 탐구하며  
계수 `a`의 크기와 부호가 그래프의 **모양과 방향**에 어떤 영향을 주는지 관찰할 수 있도록 도와줍니다.
""")

# a값 슬라이더
a = st.slider("계수 a 값을 조절하세요", -5.0, 5.0, 1.0, 0.1)

# x, y 계산
x = np.linspace(-5, 5, 400)
y = a * (x ** 2)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label=f"y = {a:.1f}x²", linewidth=2)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"y = {a:.1f}x² 그래프")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# 그래프 해석 출력
st.subheader("그래프 분석 결과")

if a > 0:
    st.markdown(f"✅ **a = {a:.1f} > 0** → 그래프는 **아래로 볼록 (∪ 모양)** 입니다.")
elif a < 0:
    st.markdown(f"✅ **a = {a:.1f} < 0** → 그래프는 **위로 볼록 (∩ 모양)** 입니다.")
else:
    st.markdown("✅ **a = 0** → 이때 y = 0으로, **직선** 형태입니다.")

# 폭(넓이) 분석
abs_a = abs(a)
if abs_a < 1:
    st.markdown("📉 **|a| < 1** → 그래프의 폭이 **넓어집니다.** (완만한 곡선)")
elif abs_a == 1:
    st.markdown("⚖️ **|a| = 1** → 기본 폭의 그래프입니다.")
else:
    st.markdown("📈 **|a| > 1** → 그래프의 폭이 **좁아집니다.** (가파른 곡선)")

# 요약 문장
st.markdown("""
---
### 🧠 귀납적 관찰 포인트
- `a`가 **양수**면 그래프는 **아래로 볼록(∪)**  
- `a`가 **음수**면 그래프는 **위로 볼록(∩)**  
- `|a|`가 **커질수록 좁아지고**, **작아질수록 넓어진다.**
""")
