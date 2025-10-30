import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 페이지 기본 설정
st.set_page_config(page_title="유리함수의 그래프 기본형(y=a/x) 분석하기", page_icon="📉")
st.title("📉 유리함수의 그래프 기본형 (y = a/x) 분석하기")

st.write("""
이 앱은 **유리함수의 기본형 y = a/x** 그래프를 탐구하며  
계수 `a`의 크기와 부호가 그래프의 **방향과 폭**에 어떤 영향을 주는지 관찰할 수 있도록 도와줍니다.
""")

# 슬라이더: a값 조절 (-100 ~ 100)
a = st.slider("계수 a 값을 조절하세요", -100.0, 100.0, 1.0, 0.1)

# x, y 계산
x = np.linspace(-10, 10, 400)
x = x[x != 0]  # 0은 정의되지 않으므로 제외
y = a / x

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label=f"y = {a:.1f}/x", linewidth=2, color="royalblue")
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"y = {a:.1f}/x 그래프")
ax.legend()
ax.grid(True)

# 축 범위 조절 (그래프가 튀어나가지 않도록)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

st.pyplot(fig)

# 분석 설명
st.subheader("그래프 분석 결과")

# 부호에 따른 사분면 및 모양
if a > 0:
    st.markdown(f"✅ **a = {a:.1f} > 0** → 그래프는 **제1사분면과 제3사분면**에 위치한 **반비례 모양**입니다.")
elif a < 0:
    st.markdown(f"✅ **a = {a:.1f} < 0** → 그래프는 **제2사분면과 제4사분면**에 위치한 **반비례 모양**입니다.")
else:
    st.markdown("✅ **a = 0** → 모든 x에서 y=0, 즉 x축과 일치하는 **직선 그래프**입니다.")

# 폭(넓이) 분석
abs_a = abs(a)
if abs_a < 1:
    st.markdown("📉 **|a| < 1** → 그래프의 폭이 **좁아집니다.** (원점 근처에서 완만)")
elif abs_a == 1:
    st.markdown("⚖️ **|a| = 1** → **기본 폭**의 그래프입니다.")
else:
    st.markdown("📈 **|a| > 1** → 그래프의 폭이 **넓어집니다.** (원점에 더 가까운 형태)")

# 학습 요약
st.markdown("""
---
### 🧠 귀납적 관찰 포인트
- `a`가 **양수**면 그래프는 **제1사분면과 제3사분면**에 그려진다.  
- `a`가 **음수**면 그래프는 **제2사분면과 제4사분면**에 그려진다.  
- `|a|`가 **커질수록 폭이 넓어지고**, **작아질수록 폭이 좁아진다.**
""")
