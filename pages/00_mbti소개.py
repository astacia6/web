import streamlit as st

# --- MBTI 유형 및 설명 데이터 ---
mbti_info = {
    "INTJ": {
        "그룹": "분석가",
        "설명": "전략가형 - 창의적이며 전략적인 사색가로, 모든 일에 계획이 있습니다."
    },
    "INTP": {
        "그룹": "분석가",
        "설명": "논리술사형 - 지적인 호기심이 많고 논리적인 사색가입니다."
    },
    "ENTJ": {
        "그룹": "분석가",
        "설명": "통솔자형 - 대담하고 상상력이 풍부한 지도자, 강한 의지와 결단력이 있습니다."
    },
    "ENTP": {
        "그룹": "분석가",
        "설명": "변론가형 - 기민하고 창의적인 사색가로, 지적인 도전을 즐깁니다."
    },
    "INFJ": {
        "그룹": "외교관",
        "설명": "옹호자형 - 조용하고 신비로우며, 통찰력 있는 이상주의자입니다."
    },
    "INFP": {
        "그룹": "외교관",
        "설명": "중재자형 - 부드럽고 친절한 성격의 이상주의자로, 내면의 가치를 중시합니다."
    },
    "ENFJ": {
        "그룹": "외교관",
        "설명": "선도자형 - 타인을 이끄는 카리스마 있고 감정이 풍부한 지도자입니다."
    },
    "ENFP": {
        "그룹": "외교관",
        "설명": "활동가형 - 열정적이고 창의적인 자유로운 영혼의 사람입니다."
    },
    # 필요에 따라 나머지 유형 추가 가능
}

# --- Streamlit 앱 구성 ---
st.set_page_config(page_title="MBTI 소개", page_icon="🧠")

st.title("🧠 MBTI 성격 유형 소개")
st.markdown("MBTI는 성격을 **16가지 유형**으로 나누는 대표적인 심리유형 이론입니다. 아래에서 당신의 유형을 선택해보세요.")

# 사이드바에서 그룹 선택
group_filter = st.sidebar.selectbox("성격 그룹 필터", ["전체", "분석가", "외교관"])

# MBTI 선택 드롭다운
filtered_mbti = [mbti for mbti, data in mbti_info.items() if group_filter == "전체" or data["그룹"] == group_filter]
selected_mbti = st.selectbox("MBTI 유형을 선택하세요", filtered_mbti)

# 선택한 MBTI 정보 출력
if selected_mbti:
    info = mbti_info[selected_mbti]
    st.subheader(f"🔍 {selected_mbti} - {info['그룹']}")
    st.write(info["설명"])
