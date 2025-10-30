import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="이차함수 그래프 학습기", layout="centered")

st.title("📈 이차함수의 그래프 표준형 학습기")
st.markdown("""
이 앱은 **이차함수의 그래프 표준형**  
\\[
y = a(x - p)^2 + q
\\]
의 형태와 그래프의 변화를 시각적으로 학습하기 위한 도구입니다.
""")

# --- 단계 1: p 변화 관찰 ---
st.header("1️⃣ p의 변화에 따른 그래프 이동")

st.markdown("""
표준형 \\( y = a(x - p)^2 \\) 에서 **p 값이 변하면 그래프가 x축 방향으로 평행이동**합니다.  
즉, **y = ax²**의 그래프를 **x축 방향으로 p만큼 이동**한 형태입니다.
""")

a = st.slider("a 값 선택", -3.0, 3.0, 1.0, 0.1)
p = st.slider("p 값 선택 (x축 이동)", -5.0, 5.0, 0.0, 0.1)

x = np.linspace(-10, 10, 400)
y = a * (x - p) ** 2

fig1, ax1 = plt.subplots()
ax1.plot(x, a * x ** 2, '--', label='y = ax² (기준)')
ax1.plot(x, y, label=f'y = a(x - {p})²')
ax1.set_ylim(-10, 50)
ax1.legend()
ax1.grid(True)
st.pyplot(fig1)

st.markdown("> 👉 **p > 0이면 오른쪽으로, p < 0이면 왼쪽으로** 이동합니다.")


# --- 단계 2: q 변화 관찰 ---
st.header("2️⃣ q의 변화에 따른 그래프 이동")

st.markdown("""
표준형 \\( y = a(x - p)^2 + q \\) 에서 **q 값이 변하면 그래프가 y축 방향으로 평행이동**합니다.  
즉, **y = a(x - p)²** 그래프를 **위 또는 아래로 q만큼 이동**합니다.
""")

q = st.slider("q 값 선택 (y축 이동)", -10.0, 10.0, 0.0, 0.1)

y2 = a * (x - p) ** 2 + q

fig2, ax2 = plt.subplots()
ax2.plot(x, a * (x - p) ** 2, '--', label=f'y = a(x - {p})² (기준)')
ax2.plot(x, y2, label=f'y = a(x - {p})² + {q}')
ax2.set_ylim(-10, 50)
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)

st.markdown("> 👉 **q > 0이면 위로, q < 0이면 아래로** 이동합니다.")


# --- 단계 3: p, q 동시에 조절 ---
st.header("3️⃣ p, q를 동시에 조절하며 그래프의 변화 관찰")

st.markdown("""
이제 p와 q를 함께 조절하면서 이차함수의 그래프가  
어떻게 **x축과 y축 방향으로 동시에 평행이동**하는지 확인해 보세요.
""")

p2 = st.slider("p 값 (x축 이동)", -5.0, 5.0, 0.0, 0.1, key="p2")
q2 = st.slider("q 값 (y축 이동)", -10.0, 10.0, 0.0, 0.1, key="q2")

y3 = a * (x - p2) ** 2 + q2

fig3, ax3 = plt.subplots()
ax3.plot(x, a * x ** 2, '--', label='y = ax² (기준)')
ax3.plot(x, y3, label=f'y = a(x - {p2})² + {q2}')
ax3.set_ylim(-10, 50)
ax3.legend()
ax3.grid(True)
st.pyplot(fig3)

st.markdown("> ✅ **꼭지점은 (p, q)** 이며, 이 점을 기준으로 그래프가 이동합니다.")


# --- 단계 4: 퀴즈 ---
st.header("🧠 개념 확인 퀴즈")

st.markdown("마지막으로, 간단한 문제로 개념을 점검해 봅시다!")

quiz_q = st.radio(
    "문제 1️⃣: y = (x - 3)² + 2 의 꼭지점은 어디일까요?",
    ["(3, 2)", "(-3, 2)", "(3, -2)", "(-3, -2)"]
)

if st.button("정답 확인", key="quiz1"):
    if quiz_q == "(3, 2)":
        st.success("🎉 정답입니다! 꼭지점은 (p, q) = (3, 2) 입니다.")
    else:
        st.error("❌ 오답입니다. 꼭지점은 (p, q) = (3, 2) 입니다.")

st.markdown("---")
st.markdown("💡 만든이: ChatGPT + 당신의 아이디어로 완성된 이차함수 학습 앱입니다.")
