import streamlit as st
import random

# 최근 회차 당첨번호 (예시)
RECENT_WIN = set([3, 13, 15, 24, 33, 37])
RECENT_BONUS = 2

# 번호별 색상 지정
def get_color(num):
    if 1 <= num <= 10:
        return "#FBC400"   # 노랑
    elif 11 <= num <= 20:
        return "#69C8F2"   # 파랑
    elif 21 <= num <= 30:
        return "#FF7272"   # 빨강
    elif 31 <= num <= 40:
        return "#AAAAAA"   # 회색
    else:
        return "#B0D840"   # 초록

# 동그라미 스타일로 숫자 표시
def render_ball(num):
    color = get_color(num)
    return f"""
    <div style="
        display:inline-block;
        background:{color};
        color:white;
        border-radius:50%;
        width:45px;
        height:45px;
        text-align:center;
        line-height:45px;
        margin:4px;
        font-weight:bold;
        font-size:18px;">
        {num}
    </div>
    """

# Streamlit 설정
st.set_page_config(page_title="🎱 로또 번호 추첨기", page_icon="🎱")
st.title("🎱 대한민국 로또 번호 추첨기")

st.write("""
1부터 45까지 중 **6개의 번호를 무작위로 추천**해주는 앱입니다.  
몇 세트를 생성할지 직접 입력하고 **생성 버튼을 누르면 폭죽🎆이 터집니다!**
""")

# 세트 개수 직접 입력 (1~10)
num_sets = st.number_input("몇 세트를 생성할까요? (1~10)", min_value=1, max_value=10, value=1, step=1)

# 버튼 클릭 시 번호 생성
if st.button("🎰 번호 생성하기"):
    all_sets = []
    for i in range(num_sets):
        nums = random.sample(range(1, 46), 6)
        nums.sort()
        all_sets.append(nums)

    # 🎉 폭죽 애니메이션
    st.balloons()

    st.subheader("🎯 생성된 번호")
    for idx, nums in enumerate(all_sets, start=1):
        st.markdown(f"**세트 {idx}:**", unsafe_allow_html=True)
        html = "".join([render_ball(n) for n in nums])
        st.markdown(html, unsafe_allow_html=True)

    # 최근 당첨번호 표시
    st.subheader("📅 최근 당첨번호와 비교")
    st.markdown("**최근 당첨번호:**", unsafe_allow_html=True)
    recent_html = "".join([render_ball(n) for n in sorted(RECENT_WIN)]) \
                  + f"<span style='margin-left:10px; font-size:18px;'>보너스 ➕</span>" \
                  + render_ball(RECENT_BONUS)
    st.markdown(recent_html, unsafe_allow_html=True)

    st.markdown("---")
    # 비교 결과 출력
    for idx, nums in enumerate(all_sets, start=1):
        user_set = set(nums)
        matched = len(user_set & RECENT_WIN)
        bonus_matched = (RECENT_BONUS in user_set)
        result_text = f"세트 {idx}: 🎯 {matched}개 일치"
        if bonus_matched:
            result_text += " + 보너스 포함!"
        st.write(result_text)

st.markdown("""
---
### 💡 참고사항  
- 번호는 완전 무작위로 생성되며, 실제 당첨과는 무관합니다.  
- 로또는 **1~45 중 6개 숫자**를 맞히면 1등이에요!  
- 행운을 빕니다 🍀
""")
