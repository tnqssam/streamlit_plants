import streamlit as st

st.title("🌿 나에게 어울리는 식물은?")
st.write("🪴 아래 질문에 답해보세요! 당신에게 딱 맞는 식물을 찾아드릴게요 💡")

# 입력 질문
name = st.text_input("👤 당신의 이름은 무엇인가요?")

personality = st.selectbox("🧠 당신의 성격은 어떤가요?", [
    "보기를 선택하세요",
    "🕊️ 차분하고 조용해요",
    "🏃 활발하고 활동적이에요",
    "📋 꼼꼼한 편이에요",
    "🔍 새롭고 신기한 걸 좋아해요"
])

location = st.selectbox("🏠 식물을 어디에 두고 싶나요?", [
    "보기를 선택하세요",
    "🛋️ 실내(책상, 방 안 등)",
    "🌤️ 실외(베란다, 마당 등)"
])

sunlight = st.selectbox("☀️ 햇빛은 얼마나 들어오나요?", [
    "보기를 선택하세요",
    "🌞 햇빛이 잘 들어요",
    "⛅ 반쯤 햇빛이 들어요(반그늘)",
    "🌑 햇빛이 거의 안 들어요(그늘)"
])

watering = st.selectbox("💧 물은 얼마나 자주 줄 수 있나요?", [
    "보기를 선택하세요",
    "🌊 매일 줄 수 있어요",
    "🌦️ 일주일에 2~3번 줄 수 있어요",
    "💤 자주 못 줄 수도 있어요"
])

size = st.selectbox("📏 키우고 싶은 식물의 크기는?", [
    "보기를 선택하세요",
    "🌱 작고 귀여운 식물",
    "🌿 중간 크기의 식물",
    "🌳 조금 큰 식물도 괜찮아요"
])

mood = st.selectbox("🎨 어떤 분위기의 식물을 원하나요?", [
    "보기를 선택하세요",
    "🌸 귀엽고 예쁜 식물",
    "🧼 심플하고 깔끔한 식물",
    "🌀 신기하고 독특한 식물"
])

plant_type = st.multiselect("🌼 식물의 종류 중 어떤 걸 좋아하나요? (최대 2개)", [
    "🌸 꽃이 피는 식물",
    "🍓 열매가 열리는 식물",
    "🍃 잎이 예쁜 식물",
    "🌵 모양이 독특한 식물",
    "🌺 향기가 나는 식물"
], max_selections=2)

colors = st.multiselect("🎨 좋아하는 색깔은 무엇인가요? (최대 2개)", [
    "🔴 빨강", "🟠 주황", "🟡 노랑", "🟢 초록",
    "🔵 파랑", "🟣 보라", "💗 분홍", "⚪ 흰색", "⚫ 검정", "🌈 기타"
], max_selections=2)

# 추천 로직
def recommend_plant():
    if "🌸 꽃이 피는 식물" in plant_type and "🍓 열매가 열리는 식물" in plant_type:
        return "🍓 딸기 화분"
    if "🌵 모양이 독특한 식물" in plant_type or personality == "🔍 새롭고 신기한 걸 좋아해요":
        return "🌵 선인장"
    if "🍃 잎이 예쁜 식물" in plant_type and sunlight == "🌑 햇빛이 거의 안 들어요(그늘)":
        return "🌿 스파트필름"
    if watering == "💤 자주 못 줄 수도 있어요":
        return "🪴 다육이"
    if "🌺 향기가 나는 식물" in plant_type:
        return "🌼 라벤더"
    if size == "🌱 작고 귀여운 식물" and mood == "🌸 귀엽고 예쁜 식물":
        return "🌼 미니 해바라기"
    if mood == "🧼 심플하고 깔끔한 식물":
        return "🪴 산세베리아"
    return "🌿 몬스테라"

# 결과 출력 버튼
if st.button("🌼 식물 추천받기"):
    if not name:
        st.warning("이름을 입력해주세요!")
    elif (personality.startswith("보기를 선택하세요") or location.startswith("보기를 선택하세요") or sunlight.startswith("보기를 선택하세요") or
          watering.startswith("보기를 선택하세요") or size.startswith("보기를 선택하세요") or mood.startswith("보기를 선택하세요")):
        st.warning("모든 항목을 선택해주세요!")
    elif len(plant_type) == 0 or len(colors) == 0:
        st.warning("식물의 종류와 색깔을 1개 이상 선택해주세요!")
    else:
        recommendation = recommend_plant()
        st.success(f"✨ {name}님께 어울리는 식물은 👉 **{recommendation}** 입니다!")
