import streamlit as st
import folium
from streamlit_folium import st_folium
import requests

st.set_page_config(page_title="🇪🇸 스페인 여행 가이드 (Fun Edition)", layout="wide")

# --- 사이드바 ---
st.sidebar.title("여행지 선택")
cities = ["전체 보기", "바르셀로나", "마드리드", "세비야", "그라나다"]
choice = st.sidebar.selectbox("도가니 중 하나를 골라보세요!", cities)

st.sidebar.markdown("---")
if st.sidebar.button("스페인 퀴즈!"):
    st.sidebar.success("스페인 국기는 🇪🇸? 아니면 🇪🇺?")
    # 실제 퀴즈 로직은 여기다 추가 가능

# --- Lottie 애니메이션 (지도 배경 장식용) ---
@st.experimental_memo
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return {}

lottie_map = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_tfb3estd.json")

# --- 여행지 데이터 ---
travel_destinations = {
    "바르셀로나": {
        "loc": (41.3851, 2.1734),
        "img": "https://source.unsplash.com/featured/?barcelona",
        "desc": [
            "🎨 **사그라다 파밀리아**: 가우디의 걸작, 매년 수백만 명 방문",
            "🏰 **고딕 지구**: 중세 골목길을 걸어보세요",
            "🛍️ **람블라스 거리**: 거리 공연과 시장이 활기차요"
        ]
    },
    "마드리드": {
        "loc": (40.4168, -3.7038),
        "img": "https://source.unsplash.com/featured/?madrid",
        "desc": [
            "🖼️ **프라도 미술관**: 고전 명화가 가득",
            "🏰 **왕궁(Palacio Real)**: 호화로운 왕실 건축",
            "🌳 **레티로 공원**: 보트 타기와 해먹 체험"
        ]
    },
    "세비야": {
        "loc": (37.3886, -5.9823),
        "img": "https://source.unsplash.com/featured/?seville",
        "desc": [
            "⛪ **세비야 대성당**: 히랄다 탑에서 전망 감상",
            "🏰 **알카사르 궁전**: 무데하르 양식의 걸작",
            "💃 **플라멩코 공연**: 열정적인 춤을 눈앞에서"
        ]
    },
    "그라나다": {
        "loc": (37.1773, -3.5986),
        "img": "https://source.unsplash.com/featured/?granada",
        "desc": [
            "🌺 **알람브라 궁전**: 서쪽 이슬람 예술의 정수",
            "🏘️ **알바이신 지구**: 매력적인 흰집 골목길",
            "🎶 **사크로몬테 동굴**: 집시 플라멩코를 체험"
        ]
    },
}

# --- 지도 생성 함수 ---
def make_map(filtered_cities):
    m = folium.Map(location=[40.0, -3.7], zoom_start=6)
    for city in filtered_cities:
        data = travel_destinations[city]
        folium.Marker(
            location=data["loc"],
            popup=f"<b>{city}</b>",
            tooltip=city
        ).add_to(m)
    return m

# --- 본문 ---
st.title("🎉 스페인 여행 가이드 (Fun Edition)")
st.caption("사이드바에서 도시를 선택하거나 퀴즈를 눌러보세요!")

# 애니메이션 오버레이
st_lottie = st.empty()
st_lottie_l = st_lottie.lottie_component(lottie_map, height=200)

# 전체 보기
if choice == "전체 보기":
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📍 지도")
        st_folium(make_map(travel_destinations.keys()), width=650, height=500)
    with col2:
        st.subheader("🏙️ 여행지 카드")
        for city, data in travel_destinations.items():
            st.image(data["img"], caption=city, use_column_width=True)
            for line in data["desc"]:
                st.write(f"- {line}")
            st.markdown("---")
else:
    # 개별 도시 상세 탭
    tabs = st.tabs(["정보", "사진", "지도", "퀴즈"])
    data = travel_destinations[choice]

    # 정보 탭
    with tabs[0]:
        st.header(choice)
        for d in data["desc"]:
            st.write(d)
        if st.button(f"{choice} 퀴즈 풀기"):
            st.info(f"{choice} 관련 간단 퀴즈를 준비 중입니다 😉")
    # 사진 탭
    with tabs[1]:
        st.image(data["img"], use_column_width=True, caption=f"{choice}의 풍경")
    # 지도 탭
    with tabs[2]:
        st_folium(make_map([choice]), width=800, height=500)
    # 퀴즈 탭
    with tabs[3]:
        st.markdown(f"### 🔍 {choice} 퀴즈")
        q1 = st.radio("사그라다 파밀리아가 위치한 도시는?", ["마드리드", "바르셀로나", "세비야"])
        if st.button("정답 확인"):
            if q1 == "바르셀로나":
                st.success("정답입니다! 🎉")
            else:
                st.error("아쉽지만 다시 시도해보세요.")

# 푸터
st.markdown("---")
st.markdown("💡 원하시는 기능(맛집 추천, 교통 정보 등)이 있으면 사이드바에 요청해주세요!")
