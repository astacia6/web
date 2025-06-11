import streamlit as st
import folium
from streamlit_folium import st_folium
import requests

# 페이지 설정
st.set_page_config(page_title="🇪🇸 스페인 여행 가이드 (Fun Edition)", layout="wide")

# --- 사이드바 ---
st.sidebar.title("여행지 선택")
cities = ["전체 보기", "바르셀로나", "마드리드", "세비야", "그라나다"]
choice = st.sidebar.selectbox("여행지를 골라보세요!", cities)

st.sidebar.markdown("---")
if st.sidebar.button("🎯 스페인 퀴즈 풀기!"):
    st.sidebar.success("문제: 스페인의 수도는 마드리드일까요? 🤔")

# --- Lottie 애니메이션 로딩 함수 ---
@st.cache_data
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return {}

from streamlit_lottie import st_lottie
lottie_map = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json")

# --- 여행지 데이터 ---
travel_destinations = {
    "바르셀로나": {
        "loc": (41.3851, 2.1734),
        "img": "https://source.unsplash.com/featured/?barcelona",
        "desc": [
            "🎨 **사그라다 파밀리아**: 가우디의 걸작 성당",
            "🏰 **고딕 지구**: 중세 분위기의 골목 산책",
            "🛍️ **람블라스 거리**: 활기 넘치는 쇼핑 거리"
        ]
    },
    "마드리드": {
        "loc": (40.4168, -3.7038),
        "img": "https://source.unsplash.com/featured/?madrid",
        "desc": [
            "🖼️ **프라도 미술관**: 고전 예술의 성지",
            "🏰 **왕궁**: 유럽 최대 규모의 궁전",
            "🌳 **레티로 공원**: 현지인과 함께 여유를"
        ]
    },
    "세비야": {
        "loc": (37.3886, -5.9823),
        "img": "https://source.unsplash.com/featured/?seville",
        "desc": [
            "⛪ **세비야 대성당**: 거대한 고딕 양식 성당",
            "🏰 **알카사르 궁전**: 중세 이슬람-기독교 혼합양식",
            "💃 **플라멩코 공연**: 열정의 무대!"
        ]
    },
    "그라나다": {
        "loc": (37.1773, -3.5986),
        "img": "https://source.unsplash.com/featured/?granada",
        "desc": [
            "🌺 **알람브라 궁전**: 이슬람 예술의 결정체",
            "🏘️ **알바이신 지구**: 고즈넉한 언덕마을 산책",
            "🎶 **사크로몬테**: 동굴 속 집시 공연"
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
            tooltip=city,
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)
    return m

# --- 본문 콘텐츠 ---
st.title("🎉 스페인 여행 가이드 (Fun Edition)")
st.caption("도시를 선택하면 사진, 설명, 지도, 퀴즈까지 즐길 수 있어요!")

# 애니메이션 표시
with st.container():
    st_lottie(lottie_map, height=200, key="map_anim")

# 전체 보기
if choice == "전체 보기":
    st.subheader("📍 여행지 지도 보기")
    st_folium(make_map(travel_destinations.keys()), width=1000, height=500)

    st.subheader("🏙️ 여행지 카드 보기")
    for city, data in travel_destinations.items():
        st.image(data["img"], caption=f"{city}의 풍경", use_column_width=True)
        for line in data["desc"]:
            st.write(f"- {line}")
        st.markdown("---")

else:
    # 도시 개별 보기
    data = travel_destinations[choice]
    tabs = st.tabs(["ℹ️ 정보", "🖼️ 사진", "🗺️ 지도", "❓ 퀴즈"])

    with tabs[0]:
        st.header(f"{choice} 여행지 정보")
        for d in data["desc"]:
            st.markdown(f"- {d}")

    with tabs[1]:
        st.image(data["img"], caption=f"{choice}의 풍경", use_column_width=True)

    with tabs[2]:
        st.subheader(f"{choice} 위치 지도")
        st_folium(make_map([choice]), width=900, height=500)

    with tabs[3]:
        st.subheader(f"{choice} 관련 퀴즈 🎯")
        q = st.radio("📌 사그라다 파밀리아는 어느 도시에 있나요?", 
                     ["세비야", "그라나다", "바르셀로나", "마드리드"])
        if st.button("정답 확인"):
            if q == "바르셀로나":
                st.success("🎉 정답입니다! 바르셀로나는 가우디의 도시예요.")
            else:
                st.error("🙅‍♂️ 오답입니다. 다시 생각해보세요!")

# 푸터
st.markdown("---")
st.caption("🧳 본 앱은 스트림릿 + 폴리움 + Lottie로 제작되었습니다.")
