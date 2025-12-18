import streamlit as st
import sympy as sp

st.set_page_config(page_title="유리식", layout="centered")
st.title("📘 유리식")
st.write("---")

x = sp.Symbol('x')

# =====================
# 1. 유리식의 뜻
# =====================
st.header("1️⃣ 유리식의 뜻")

st.markdown("두 다항식의 나눗셈으로 나타낼 수 있는 식을 **유리식**이라고 한다.")

st.latex(r"\frac{P(x)}{Q(x)} \quad (Q(x) \neq 0)")

st.markdown("이때 분모에 문자가 포함되어 있으면 유리식에 해당한다.")

st.write("---")

# =====================
# 유리식의 예
# =====================
st.subheader("📌 유리식의 예")

st.markdown("다음 식들은 모두 유리식이다.")

st.latex(r"①\quad \frac{x}{x+1}")
st.latex(r"②\quad \frac{3}{x-2}")
st.latex(r"③\quad \frac{2x^2+1}{x^2-4}")

st.markdown("위 식들은 모두 분모가 0이 되지 않는 범위에서 정의된다.")

st.write("---")

# =====================
# 2. 유리식의 연산
# =====================
st.header("2️⃣ 유리식의 연산")

operation = st.selectbox(
    "학습할 연산을 선택하세요",
    ["덧셈", "뺄셈", "곱셈", "나눗셈"]
)

examples = {
    "덧셈": ((x + 1)/(x - 2), (2*x)/(x + 3)),
    "뺄셈": ((2*x)/(x + 1), (x - 3)/(x - 2)),
    "곱셈": ((x**2 - 1)/(x + 2), (x + 2)/(x + 1)),
    "나눗셈": ((x + 3)/(x - 1), (x + 1)/(x + 2)),
}

expr1, expr2 = examples[operation]

st.write("---")
st.subheader(f"📖 예제 | 유리식의 {operation}")

# =====================
# 덧셈
# =====================
if operation == "덧셈":
    st.markdown("다음 유리식을 계산하여라.")
    st.latex(sp.latex(expr1) + " + " + sp.latex(expr2))

    st.markdown("**풀이**")
    st.markdown(
        "① 분모가 서로 다르므로 **통분한다**. "
        "분모를 $(x-2)(x+3)$으로 맞춘다."
    )

    st.latex(r"\frac{(x+1)(x+3) + 2x(x-2)}{(x-2)(x+3)}")

    num = sp.expand((x+1)*(x+3) + 2*x*(x-2))
    st.latex(r"\frac{" + sp.latex(num) + r"}{(x-2)(x+3)}")

    st.latex(sp.latex(sp.simplify(expr1 + expr2)))

# =====================
# 뺄셈
# =====================
elif operation == "뺄셈":
    st.markdown("다음 유리식을 계산하여라.")
    st.latex(sp.latex(expr1) + " - " + sp.latex(expr2))

    st.markdown("**풀이**")
    st.markdown(
        "① 분모가 서로 다르므로 **통분한다**. "
        "분모를 $(x+1)(x-2)$로 맞춘다."
    )

    st.latex(r"\frac{2x(x-2) - (x-3)(x+1)}{(x+1)(x-2)}")

    num = sp.expand(2*x*(x-2) - (x-3)*(x+1))
    st.latex(r"\frac{" + sp.latex(num) + r"}{(x+1)(x-2)}")

    st.latex(sp.latex(sp.simplify(expr1 - expr2)))

# =====================
# 곱셈
# =====================
elif operation == "곱셈":
    st.markdown("다음 유리식을 계산하여라.")
    st.latex(sp.latex(expr1) + " \times " + sp.latex(expr2))

    st.markdown("**풀이**")
    st.markdown("① 분자끼리, 분모끼리 각각 곱한다.")

    st.latex(r"\frac{(x^2-1)(x+2)}{(x+2)(x+1)}")
    st.latex(r"\frac{(x-1)(x+1)(x+2)}{(x+2)(x+1)}")
    st.latex(r"x-1")

# =====================
# 나눗셈
# =====================
elif operation == "나눗셈":
    st.markdown("다음 유리식을 계산하여라.")
    st.latex(sp.latex(expr1) + " \div " + sp.latex(expr2))

    st.markdown("**풀이**")
    st.markdown("① 나누는 유리식을 뒤집어 곱셈으로 바꾼다.")

    st.latex(r"\frac{x+3}{x-1} \times \frac{x+2}{x+1}")
    st.latex(r"\frac{(x+3)(x+2)}{(x-1)(x+1)}")
    st.latex(sp.latex(sp.simplify(expr1 / expr2)))

st.write("---")
st.info("💡 분모가 0이 되는 값은 정의역에서 제외해야 한다.")
