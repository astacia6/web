import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="스페인 여행 가이드", layout="wide")

# 헤더
st.title("🇪🇸 스페인 여행지 가이드")
st.markdown("""
스페인은 유럽 남서부에 위치한 아름다운 나라로, 고유한 문화, 역사적인 도시, 매혹적인 자연경관으로 가득합니다. 아래에서 주요 여행지를 소개하고, 지도를 통해 위치도 확인해보세요!
""")

# 여행지 정보 정의
travel_destinations = [
    {
        "name": "바르셀로나",
        "location": (41.3851, 2.1734),
        "description": """
- **사그라다 파밀리아 성당**: 가우디가 설계한 미완성 성당.
- **고딕 지구**: 중세 분위기가 물씬 나는 역사 지구.
- **람블라스 거리**: 산책과 쇼핑을 즐길 수 있는 명소.
"""
    },
    {
        "name": "마드리드",
        "location": (40.4168, -3.7038),
        "description": """
- **프라도 미술관**: 세계적인 고전 예술 작품들이 전시됨.
- **왕궁(Palacio Real)**: 웅장한 건축과 궁전 내부 관람.
- **레티로 공원**: 시민들이 사랑하는 도심 속 휴식처.
"""
    },
    {
        "name": "세비야",
        "location": (37.3886, -5.9823),
        "description": """
- **세비야 대성당**: 스페인 최대의 고딕 성당.
- **알카사르 궁전**: 이슬람과 기독교 양식이 공존하는 궁전.
- **플라멩코 공연**: 플라멩코의 본고장에서 감상 가능.
"""
    },
    {
        "name": "그라나다",
        "location": (37.1773, -3.5986),
        "description": """
- **알람브라 궁전**: 이슬람 건축의 정수.
- **알바이신 지구**: 하얀 골목길과 언덕 풍경.
- **사크로몬테 동굴**: 집시 전통 문화 체험.
"""
    },
]

# 지도 만들기
m = folium.Map(location=[40.0, -3.7], zoom_start=6)

# 각 도시 마커 추가
for place in travel_destinations:
    folium.Marker(
        location=place["location"],
        popup=folium.Popup(f"<b>{place['name']}</b><br>{place['description']}", max_width=300),
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력
st.subheader("📍 스페인 여행지 지도")
st_data = st_folium(m, width=1000, height=600)

# 각 도시 설명 출력
st.subheader("📝 여행지 설명")
for place in travel_destinations:
    st.markdown(f"### {place['name']}")
    st.markdown(place["description"])
