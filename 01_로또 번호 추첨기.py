import streamlit as st
import random

# 최근 회차 당첨번호 (예시로 최신 회차)
RECENT_WIN = set([3, 15, 27, 33, 34, 36])
RECENT_BONUS = 37

st.title("로또 번호 추천 및 당첨번호 비교 앱")

# 사용자 입력: 몇 세트 생성할지
num_sets = st.number_input("몇 세트를 생성하시겠어요?", min_value=1, max_value=100, value=1, step=1)

if st.button("생성"):
    all_sets = []
    for i in range(num_sets):
        # 1 ~ 45 중에서 중복 없이 6개 선택
        nums = random.sample(range(1, 46), 6)
        nums.sort()
        all_sets.append(nums)
    # 출력
    st.subheader("생성된 번호들")
    for idx, nums in enumerate(all_sets, start=1):
        st.write(f"세트 {idx}: {nums}")
    # 비교
    st.subheader("최근 당첨번호와 비교")
    st.write(f"최근 당첨번호: {sorted(RECENT_WIN)}  (보너스: {RECENT_BONUS})")
    for idx, nums in enumerate(all_sets, start=1):
        user_set = set(nums)
        matched = len(user_set & RECENT_WIN)
        bonus_matched = (RECENT_BONUS in user_set)
        st.write(f"세트 {idx}: {nums} → 맞은 번호 개수: {matched}" + (" + 보너스 포함!" if bonus_matched else ""))

# 추가 팁
st.markdown("""
---
### 사용 팁  
- 번호는 무작위로 생성됩니다. 아무런 당첨을 보장하지 않습니다.  
- 생성된 번호와 당첨번호 비교는 참고용입니다.  
- 즐거운 마음으로 사용하세요!  
""")
