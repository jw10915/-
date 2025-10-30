import streamlit as st
import random

# 최근 회차 당첨번호 (예시)
RECENT_WIN = set([3, 13, 15, 24, 33, 37])
RECENT_BONUS = 2

# 번호 구간별 색상 지정 (로또 공 느낌)
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

# 동그라미 HTML 렌더링 함수
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

st.set_page_config(page_title="로또 번호 추천기", page_icon="🎱")
st.title("🎱 로또 번호 추천 및 당첨번호 비교 앱")

st.write("""
이 앱은 대한민국 로또 1부터 45까지 중 6개의 숫자를 무작위로 추천해줍니다.  
또한 최근 당첨번호와 비교해서 얼마나 맞았는지 확인할 수 있어요.
""")

# 사용자 입력: 몇 세트를 생성할지
num_sets = st.number_input("몇 세트를 생성하시겠어요?", min_value=1, max_value=100, value=1, step=1)

if st.button("번호 생성하기"):
    all_sets = []
    for i in range(num_sets):
        nums = random.sample(range(1, 46), 6)
        nums.sort()
        all_sets.append(nums)

    st.subheader("생성된 번호")
    for idx, nums in enumerate(all_sets, start=1):
        st.markdown(f"**세트 {idx}:**", unsafe_allow_html=True)
        html = "".join([render_ball(n) for n in nums])
        st.markdown(html, unsafe_allow_html=True)

    st.subheader("최근 당첨번호와 비교")
    st.markdown("**최근 당첨번호:**", unsafe_allow_html=True)
    recent_html = "".join([render_ball(n) for n in sorted(RECENT_WIN)]) \
                  + f"<span style='margin-left:10px; font-size:18px;'>보너스 ➕</span>" \
                  + render_ball(RECENT_BONUS)
    st.markdown(recent_html, unsafe_allow_html=True)

    st.markdown("---")
    for idx, nums in enumerate(all_sets, start=1):
        user_set = set(nums)
        matched = len(user_set & RECENT_WIN)
        bonus_matched = (RECENT_BONUS in user_set)
        result_text = f"세트 {idx}: {matched}개 일치"
        if bonus_matched:
            result_text += " + 보너스 포함!"
        st.write(result_text)

st.markdown("""
---
### 참고사항  
- 번호는 **완전 무작위 생성**되며 실제 당첨을 보장하지 않습니다.  
- 추천번호와 당첨번호 비교는 **참고용** 입니다.  
- 즐겁게 이용하세요!
""")
