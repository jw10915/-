import streamlit as st
import sympy as sp

# 페이지 기본 설정
st.set_page_config(page_title="유리식 학습 앱", layout="centered")

st.title("📘 유리식의 개념과 연산 학습")
st.write("---")

# 1️⃣ 유리식의 개념
st.header("1️⃣ 유리식의 개념")
st.markdown("""
- **유리식**은 **두 다항식의 나눗셈**으로 나타낼 수 있는 식을 말합니다.  
- 즉, $$ \\frac{P(x)}{Q(x)} $$ 의 꼴이며, 여기서  
  - P(x): 다항식 (분자)  
  - Q(x): 다항식 (분모, 단 Q(x) ≠ 0)  
- 유리식은 다항식이 아닌 **분모에 문자가 있는 식**을 포함합니다.
""")

# 예시
st.subheader("🧩 예시")
examples = [
    "1) \\( \\frac{x}{x+1} \\)",
    "2) \\( \\frac{2x^2 + 3x - 1}{x - 2} \\)",
    "3) \\( \\frac{3}{x} \\)",
    "4) \\( \\frac{x^2 + 1}{x^2 - 4} \\)"
]
for ex in examples:
    st.latex(ex)

st.write("---")

# 2️⃣ 유리식의 연산
st.header("2️⃣ 유리식의 연산")

st.markdown("""
유리식의 연산에는 **덧셈, 뺄셈, 곱셈, 나눗셈**이 있습니다.  
각 연산의 기본 원리를 먼저 이해하고, 예시를 계산해 봅시다.
""")

# 연산 선택
operation = st.selectbox("연산을 선택하세요", ["덧셈", "뺄셈", "곱셈", "나눗셈"])

# 공통 x 변수 설정
x = sp.Symbol('x')

if operation == "덧셈":
    st.subheader("➕ 유리식의 덧셈")
    st.markdown("""
    - 분모가 같을 때: 분자는 더하고 분모는 그대로 둔다.  
      $$ \\frac{a}{b} + \\frac{c}{b} = \\frac{a + c}{b} $$
    - 분모가 다를 때: 공통분모를 구해서 분자를 바꾼 뒤 더한다.  
      $$ \\frac{a}{b} + \\frac{c}{d} = \\frac{ad + bc}{bd} $$
    """)
    expr1 = (x + 1)/(x - 2)
    expr2 = (2*x)/(x + 3)
    st.latex(f"\\frac{{x+1}}{{x-2}} + \\frac{{2x}}{{x+3}}")
    st.write("🧮 계산 결과:")
    st.latex(sp.latex(sp.simplify(expr1 + expr2)))

elif operation == "뺄셈":
    st.subheader("➖ 유리식의 뺄셈")
    st.markdown("""
    - 분모가 같으면 분자끼리 뺀다.  
      $$ \\frac{a}{b} - \\frac{c}{b} = \\frac{a - c}{b} $$
    - 분모가 다르면 공통분모를 만들어 계산한다.  
      $$ \\frac{a}{b} - \\frac{c}{d} = \\frac{ad - bc}{bd} $$
    """)
    expr1 = (2*x)/(x+1)
    expr2 = (x-3)/(x-2)
    st.latex(f"\\frac{{2x}}{{x+1}} - \\frac{{x-3}}{{x-2}}")
    st.write("🧮 계산 결과:")
    st.latex(sp.latex(sp.simplify(expr1 - expr2)))

elif operation == "곱셈":
    st.subheader("✖️ 유리식의 곱셈")
    st.markdown("""
    - 분자끼리, 분모끼리 각각 곱한다.  
      $$ \\frac{a}{b} \\times \\frac{c}{d} = \\frac{ac}{bd} $$
    - 단, 약분이 가능한 경우 약분한다.
    """)
    expr1 = (x**2 - 1)/(x + 2)
    expr2 = (x + 2)/(x + 1)
    st.latex(f"\\frac{{x^2 - 1}}{{x + 2}} \\times \\frac{{x + 2}}{{x + 1}}")
    st.write("🧮 계산 결과:")
    st.latex(sp.latex(sp.simplify(expr1 * expr2)))

elif operation == "나눗셈":
    st.subheader("➗ 유리식의 나눗셈")
    st.markdown("""
    - 나눗셈은 **나누는 유리식을 뒤집어 곱셈으로 바꾼다.**  
      $$ \\frac{a}{b} \\div \\frac{c}{d} = \\frac{a}{b} \\times \\frac{d}{c} = \\frac{ad}{bc} $$
    """)
    expr1 = (x+3)/(x-1)
    expr2 = (x+1)/(x+2)
    st.latex(f"\\frac{{x+3}}{{x-1}} \\div \\frac{{x+1}}{{x+2}}")
    st.write("🧮 계산 결과:")
    st.latex(sp.latex(sp.simplify(expr1 / expr2)))

st.write("---")
st.success("💡 유리식의 계산에서는 항상 **분모가 0이 되는 값은 제외**해야 한다는 점을 기억하세요!")
