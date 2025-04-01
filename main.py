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

# 식물 데이터 (설명만 포함, 2개 예시)
plant_db = [
    {
        "name": "해바라기",
        "description": "노란색 꽃잎이 활짝 피는, 햇빛을 좋아하는 밝은 식물이에요!",
        "sunlight": "햇빛", "water": "많음", "size": "큼",
        "type": ["꽃이 피는 식물"], "mood": "활기참", "personality": ["활발"], "colors": ["노랑"]
    },
    {
        "name": "무궁화",
        "description": "우리나라를 대표하는 꽃으로 다양한 색의 꽃이 여름 내내 피어요.",
        "sunlight": "햇빛", "water": "중간", "size": "중간",
        "type": ["꽃이 피는 식물"], "mood": "예쁨", "personality": ["꼼꼼"], "colors": ["분홍", "흰색"]
    },
    {
        "name": "봉선화",
        "description": "손톱 물들이는 재미가 있는, 어린이에게 친숙한 꽃이에요.",
        "sunlight": "햇빛", "water": "중간", "size": "작음",
        "type": ["꽃이 피는 식물"], "mood": "귀여움", "personality": ["차분"], "colors": ["주황", "빨강"]
    },
    {
        "name": "민들레",
        "description": "씨앗이 날아가는 모습이 재밌는 봄철 들꽃이에요.",
        "sunlight": "햇빛", "water": "중간", "size": "작음",
        "type": ["꽃이 피는 식물"], "mood": "자연스러움", "personality": ["신기한 걸 좋아해요"], "colors": ["노랑"]
    },
    {
        "name": "애플민트",
        "description": "달콤한 향기가 나는 허브로, 잎은 연초록색이에요.",
        "sunlight": "햇빛", "water": "중간", "size": "작음",
        "type": ["향기 나는 식물"], "mood": "상큼", "personality": ["활발"], "colors": ["초록"]
    },
    {
        "name": "산세베리아",
        "description": "공기 정화 능력이 뛰어나고 그늘에서도 잘 자라며 물을 자주 주지 않아도 되는 식물입니다.",
        "sunlight": "그늘", "water": "적음", "size": "중간",
        "type": ["공기 정화"], "mood": "심플", "personality": ["차분"]
    },
    {
        "name": "몬스테라",
        "description": "크고 독특한 잎이 매력적인 관엽식물로 반그늘에서 잘 자라며 실내 장식에 좋습니다.",
        "sunlight": "반그늘", "water": "중간", "size": "조금 큼",
        "type": ["잎이 예쁜 식물"], "mood": "자연스러움", "personality": ["활발"]
    },
    {
        "name": "스투키",
        "description": "관리가 편하고 공기 정화에 효과적인 실내식물입니다.",
        "sunlight": "그늘", "water": "적음", "size": "작음",
        "type": ["공기 정화"], "mood": "심플", "personality": ["차분"]
    },
    {
        "name": "해바라기",
        "description": "햇빛을 좋아하고 밝은 분위기를 주는 대표적인 꽃입니다.",
        "sunlight": "햇빛", "water": "많음", "size": "큼",
        "type": ["꽃이 피는 식물"], "mood": "활기참", "personality": ["활발"]
    },
    {
        "name": "칼랑코에",
        "description": "작고 귀여운 꽃이 피는 실내 화분용 식물입니다.",
        "sunlight": "햇빛", "water": "중간", "size": "작음",
        "type": ["꽃이 피는 식물"], "mood": "귀여움", "personality": ["꼼꼼"]
    },
    {
        "name": "딸기 화분",
        "description": "작은 열매가 열리는 재미있는 화분용 식물입니다.",
        "sunlight": "햇빛", "water": "매일", "size": "작음",
        "type": ["열매가 열리는 식물"], "mood": "귀여움", "personality": ["활발"]
    },
    {
        "name": "라벤더",
        "description": "향기가 좋고 보랏빛 꽃이 피는 허브식물입니다.",
        "sunlight": "햇빛", "water": "중간", "size": "중간",
        "type": ["향기 나는 식물"], "mood": "예쁨", "personality": ["꼼꼼"]
    },
    {
        "name": "제라늄",
        "description": "다양한 색깔의 꽃이 피며 향도 좋은 다용도 식물입니다.",
        "sunlight": "햇빛", "water": "중간", "size": "중간",
        "type": ["꽃이 피는 식물", "향기 나는 식물"], "mood": "예쁨", "personality": ["꼼꼼"]
    },
    {
        "name": "아이비",
        "description": "덩굴성으로 잘 자라며 공기 정화 기능도 뛰어난 식물입니다.",
        "sunlight": "반그늘", "water": "중간", "size": "중간",
        "type": ["잎이 예쁜 식물"], "mood": "자연스러움", "personality": ["차분"]
    },
    {
        "name": "페퍼민트",
        "description": "상큼한 향기가 나는 허브로 간단한 요리에도 사용할 수 있습니다.",
        "sunlight": "햇빛", "water": "중간", "size": "작음",
        "type": ["향기 나는 식물"], "mood": "상큼", "personality": ["활발"]
    },
    {
        "name": "로즈마리",
        "description": "요리와 방향제로 활용 가능한 향기로운 허브식물입니다.",
        "sunlight": "햇빛", "water": "중간", "size": "중간",
        "type": ["향기 나는 식물"], "mood": "깔끔", "personality": ["계획적"]
    },
    {
        "name": "파키라",
        "description": "재물운을 가져온다고 알려진 실내 인테리어용 나무입니다.",
        "sunlight": "햇빛", "water": "중간", "size": "큼",
        "type": ["잎이 예쁜 식물"], "mood": "화려함", "personality": ["활발"]
    },
    {
        "name": "호야",
        "description": "잎에 광택이 있으며 별 모양의 꽃이 피는 독특한 식물입니다.",
        "sunlight": "반그늘", "water": "중간", "size": "중간",
        "type": ["꽃이 피는 식물", "모양이 독특한 식물"], "mood": "신기함", "personality": ["신기한 걸 좋아해요"]
    },
    {
        "name": "필레아",
        "description": "둥글고 귀여운 잎이 특징이며 책상 위에 두기 좋은 소형 식물입니다.",
        "sunlight": "반그늘", "water": "중간", "size": "작음",
        "type": ["잎이 예쁜 식물"], "mood": "귀여움", "personality": ["차분"]
    },
    {
        "name": "마리모",
        "description": "물 속에서 자라는 초록색 이끼 공 모양 식물로 관리가 간편합니다.",
        "sunlight": "그늘", "water": "적음", "size": "작음",
        "type": ["모양이 독특한 식물"], "mood": "귀여움", "personality": ["조용"]
    },
    {
        "name": "무늬산호수",
        "description": "잎에 하얀 무늬가 있는 실내식물로 밝은 느낌을 줘요.",
        "sunlight": "반그늘", "water": "중간", "size": "중간",
        "type": ["잎이 예쁜 식물"], "mood": "심플", "personality": ["꼼꼼"], "colors": ["초록", "흰색"]
    },
    {
        "name": "금전수",
        "description": "두꺼운 잎이 특징인 행운의 상징 식물이에요.",
        "sunlight": "반그늘", "water": "적음", "size": "중간",
        "type": ["공기 정화"], "mood": "깔끔", "personality": ["차분"], "colors": ["초록"]
    },
    {
        "name": "크루시아",
        "description": "둥글고 도톰한 잎이 귀엽고 관리도 쉬운 식물이에요.",
        "sunlight": "반그늘", "water": "중간", "size": "작음",
        "type": ["잎이 예쁜 식물"], "mood": "귀여움", "personality": ["차분"], "colors": ["초록"]
    },
    {
        "name": "천냥금",
        "description": "작은 빨간 열매가 열리는 행운 식물이에요.",
        "sunlight": "반그늘", "water": "중간", "size": "작음",
        "type": ["열매가 열리는 식물"], "mood": "귀여움", "personality": ["꼼꼼"], "colors": ["빨강"]
    },
    {
        "name": "홍콩야자",
        "description": "넓은 잎이 매력적이며 공기 정화에도 좋아요.",
        "sunlight": "반그늘", "water": "중간", "size": "조금 큼",
        "type": ["잎이 예쁜 식물", "공기 정화"], "mood": "자연스러움", "personality": ["차분"], "colors": ["초록"]
    },
    {
        "name": "아레카야자",
        "description": "열대 분위기를 주는 실내 정화용 식물이에요.",
        "sunlight": "햇빛", "water": "많음", "size": "큼",
        "type": ["공기 정화"], "mood": "자연스러움", "personality": ["활발"], "colors": ["초록"]
    },
    {
        "name": "데리고니아",
        "description": "둥글고 밝은 초록색 잎이 사랑스러운 식물이에요.",
        "sunlight": "반그늘", "water": "중간", "size": "작음",
        "type": ["잎이 예쁜 식물"], "mood": "귀여움", "personality": ["차분"], "colors": ["초록"]
    },
    {
        "name": "아글라오네마",
        "description": "다양한 무늬가 있는 잎으로 시선을 끄는 식물이에요.",
        "sunlight": "그늘", "water": "중간", "size": "중간",
        "type": ["잎이 예쁜 식물"], "mood": "독특함", "personality": ["신기한 걸 좋아해요"], "colors": ["분홍", "초록"]
    },
    {
        "name": "금잔화",
        "description": "노란색의 작고 둥근 꽃이 귀여운 식물이에요.",
        "sunlight": "햇빛", "water": "중간", "size": "작음",
        "type": ["꽃이 피는 식물"], "mood": "귀여움", "personality": ["활발"], "colors": ["노랑"]
    },
    {
        "name": "염좌",
        "description": "잎이 도톰한 다육식물로 '돈나무'라고도 불려요.",
        "sunlight": "햇빛", "water": "적음", "size": "작음",
        "type": ["공기 정화"], "mood": "심플", "personality": ["차분"], "colors": ["초록"]
    }
]
]

# 추천 알고리즘

def match_score(plant):
    score = 0
    if plant["sunlight"] in sunlight:
        score += 1
    if plant["water"] in watering:
        score += 1
    if plant["size"] in size:
        score += 1
    if any(t in [pt[2:] for pt in plant_type] for t in plant["type"]):
        score += 1
    if plant["mood"] in mood:
        score += 1
    if personality.endswith(plant["personality"][0]):
        score += 1
    if "colors" in plant:
        if any(c in [color[2:] for color in colors] for c in plant["colors"]):
            score += 1
    return score

def recommend_plants():
    sorted_plants = sorted(plant_db, key=match_score, reverse=True)
    return sorted_plants[:2]

# 추천 결과 출력
if st.button("🌼 식물 추천받기"):
    if not name:
        st.warning("이름을 입력해주세요!")
    elif (personality.startswith("보기를 선택하세요") or location.startswith("보기를 선택하세요") or
          sunlight.startswith("보기를 선택하세요") or watering.startswith("보기를 선택하세요") or
          size.startswith("보기를 선택하세요") or mood.startswith("보기를 선택하세요")):
        st.warning("모든 항목을 선택해주세요!")
    elif len(plant_type) == 0 or len(colors) == 0:
        st.warning("식물의 종류와 색깔을 1개 이상 선택해주세요!")
    else:
        recommendations = recommend_plants()
        st.subheader(f"✨ {name}님께 어울리는 식물 추천 결과")
        cols = st.columns(2)
        for i, plant in enumerate(recommendations):
            with cols[i]:
                st.markdown(f"### 🌿 {plant['name']}")
                st.caption(plant['description'])
