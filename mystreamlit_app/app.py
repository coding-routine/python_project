import streamlit as st
from datetime import datetime, timedelta

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="코딩 클래스 | 문의·신청",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown(
    """
    <style>
      /* overall */
      .main .block-container {padding-top: 2rem; padding-bottom: 4rem;}
      .hero {background: linear-gradient(135deg,#f6f8ff 0%, #eef9ff 100%); padding: 40px 28px; border-radius: 24px; border: 1px solid #e9eef5;}
      .badge {display:inline-block; padding:6px 12px; border-radius:999px; background:#edf2ff; color:#34495e; font-weight:600; font-size:0.85rem; margin-bottom:8px;}
      .title {font-size: 2.2rem; font-weight: 800; margin: 6px 0 8px 0;}
      .subtitle {font-size: 1.05rem; color:#4b5563; margin-bottom: 0;}
      .pill {border:1px solid #eaeaea; padding:8px 12px; border-radius:999px; font-size:0.85rem; margin-right:8px; margin-top:8px; display:inline-block;}
      .card {border:1px solid #eaeaea; border-radius: 18px; padding: 18px; height:100%; background:#fff;}
      .card h4 {margin:0 0 6px 0;}
      .muted {color:#6b7280; font-size:0.9rem;}
      .price {font-weight:800; font-size:1.2rem;}
      .footer {color:#6b7280; font-size:0.9rem;}
      .faq h4 {margin-bottom: 6px;}
      .kicker {font-size:0.9rem; color:#6b7280; margin-top:2px;}
      .divider {height:1px; background:#efefef; margin: 12px 0 18px 0;}
      .highlight {background:#fffbe6; padding:2px 8px; border-radius:8px; border:1px dashed #f0e6a0;}
      .center {text-align:center;}
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Header / Hero
# -----------------------------
col_hero_left, col_hero_right = st.columns([1.1, 0.9])

with col_hero_left:
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    st.markdown('<div class="badge">초·중·고·성인 대상 1:1 · 소그룹</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">파이썬 · Pygame · Streamlit · SQL · IGCSE CS</div>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">실전 프로젝트 중심 코딩 수업 — 포트폴리오까지 완성합니다.</p>', unsafe_allow_html=True)
    st.write("")
    c1, c2, c3 = st.columns([0.22,0.22,0.56])
    with c1:
        st.link_button("📅 수업 일정 문의", "https://forms.gle/your-google-form", use_container_width=True)
    with c2:
        st.link_button("💬 카카오톡 상담", "https://pf.kakao.com/_yourchannel", use_container_width=True)
    with c3:
        st.link_button("📧 이메일 문의", "mailto:your@email.com?subject=코딩%20수업%20문의", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_hero_right:
    st.image(
        "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?q=80&w=1600&auto=format&fit=crop",
        caption="프로젝트 기반 학습: 게임·웹앱·데이터 분석",
        use_column_width=True,
    )

# -----------------------------
# Badges / Quick facts
# -----------------------------
st.markdown("#### 이런 학생에게 딱 맞아요")
fact_cols = st.columns(4)
facts = [
    ("👦", "초등 · 중등", "터틀/게임으로 재미있게 기초 탄탄"),
    ("🎮", "게임 제작", "Pygame으로 완성작 만들기"),
    ("📊", "데이터 분석", "Pandas·SQL·시각화로 분석력 up"),
    ("🎓", "IGCSE/입시", "Past paper 풀이·개념·실전 대비"),
]
for (emoji, title, desc), c in zip(facts, fact_cols):
    with c:
        st.markdown(f"<div class='card'><h4>{emoji} {title}</h4><p class='muted'>{desc}</p></div>", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# -----------------------------
# Curriculum Cards
# -----------------------------
st.markdown("### 커리큘럼(예시)")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class='card'>
      <h4>🐢 Turtle · 파이썬 기초 (8회)</h4>
      <div class='kicker'>변수·반복·조건·함수 + 도형·애니메이션</div>
      <ul>
        <li>기초 문법: 자료형, for/while, if</li>
        <li>도형/패턴/눈송이 애니메이션</li>
        <li>미니 프로젝트: 그림판, 대칭 드로잉</li>
      </ul>
      <div class='muted'>결과물: 캡처 이미지, 소스코드, 요약 리포트</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card'>
      <h4>🎮 Pygame 게임 제작 (8~12회)</h4>
      <div class='kicker'>이벤트·충돌·스프라이트·사운드</div>
      <ul>
        <li>Catch Me / Cookie Catch / 점프 액션</li>
        <li>난이도 조절, 점수/목숨, 스테이지</li>
        <li>최종 배포: 실행파일(.exe) 만들기</li>
      </ul>
      <div class='muted'>결과물: 플레이 영상, 배포 파일, 코드</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='card'>
      <h4>📈 데이터분석·SQL·Streamlit (8~12회)</h4>
      <div class='kicker'>Pandas·시각화·대시보드·웹앱</div>
      <ul>
        <li>CSV/JSON 다루기, EDA · 차트</li>
        <li>SQL(SELECT, JOIN, WINDOW, 집계)</li>
        <li>Streamlit 대시보드/폼/파일 업로드</li>
      </ul>
      <div class='muted'>결과물: 웹앱 링크/스크린샷, 리포트</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Portfolio (lightweight)
# -----------------------------
st.markdown("### 포트폴리오 샘플")
tab1, tab2, tab3 = st.tabs(["초·중등 게임", "데이터 분석", "IGCSE CS"])
with tab1:
    g1, g2, g3 = st.columns(3)
    g1.image("https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=1200&auto=format&fit=crop", caption="Catch Me")
    g2.image("https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=1200&auto=format&fit=crop", caption="Cookie Catch")
    g3.image("https://images.unsplash.com/photo-1538485399081-7191377e8241?q=80&w=1200&auto=format&fit=crop", caption="Jump Action")
with tab2:
    d1, d2, d3 = st.columns(3)
    d1.image("https://images.unsplash.com/photo-1551281044-8af4e6624178?q=80&w=1200&auto=format&fit=crop", caption="대시보드")
    d2.image("https://images.unsplash.com/photo-1551281044-4d9613d0d8df?q=80&w=1200&auto=format&fit=crop", caption="차트")
    d3.image("https://images.unsplash.com/photo-1450101215322-bf5cd27642fc?q=80&w=1200&auto=format&fit=crop", caption="EDA")
with tab3:
    st.write("Past Paper 정리, 이진/십진/16진 변환, 데이터 전송, 네트워크 등 이론+기출 대비 자료 제공")

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# -----------------------------
# Class Types & Pricing (example)
# -----------------------------
st.markdown("### 수업 형태 · 수강료 (예시)")
p1, p2, p3 = st.columns(3)
with p1:
    st.markdown("""
    <div class='card'>
      <h4>1:1 개인 수업</h4>
      <p class='muted'>맞춤 커리큘럼 · 속도/난이도 조절</p>
      <p class='price'>50분 × 8회 = <span class='highlight'>₩480,000</span></p>
      <ul>
        <li>개인 프로젝트 집중</li>
        <li>포트폴리오/대회 준비</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)
with p2:
    st.markdown("""
    <div class='card'>
      <h4>2~3인 소그룹</h4>
      <p class='muted'>팀 프로젝트 · 협업 툴 경험</p>
      <p class='price'>50분 × 8회 = <span class='highlight'>₩360,000 / 인</span></p>
      <ul>
        <li>또래 학습 동기 부여</li>
        <li>코드 리뷰 · 발표</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)
with p3:
    st.markdown("""
    <div class='card'>
      <h4>단기 부트캠프</h4>
      <p class='muted'>방학 집중 · 결과물 중심</p>
      <p class='price'>1~2주 집중반 · 커스텀 견적</p>
      <ul>
        <li>데이터분석/웹앱/게임 중 선택</li>
        <li>최종 발표/리포트 포함</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)

st.caption("※ 위 금액은 예시이며 레벨/목표/스케줄에 따라 달라질 수 있습니다.")

# -----------------------------
# Differentiators
# -----------------------------
st.markdown("### 왜 우리의 코딩 수업일까?")
d1, d2, d3, d4 = st.columns(4)
d1.metric("만족도", "4.9/5.0")
d2.metric("완성 프로젝트", "120+", "누적")
d3.metric("포트폴리오 제작", "100%")
d4.metric("재등록률", "90%")

st.markdown("""
- 실전 중심: **프로젝트 2~3개**를 완성해 포트폴리오에 담습니다.
- 기록과 피드백: 수업 후 **요약 리포트**와 다음 과제를 드립니다.
- 개별화: 학생 흥미(게임/데이터/웹) 맞춤 주제 선정.
- 진로/대회: 청소년 공모전/해커톤/IGCSE/내신 대비 지도.
""")

# -----------------------------
# Testimonials (placeholder)
# -----------------------------
st.markdown("### 수강 후기")
t1, t2 = st.columns(2)
with t1:
    st.markdown("""
    <div class='card'>
      <p>“아이 수준에 맞춰 차근차근 설명해 주셔서 스스로 코드를 고치고 개선하는 힘이 생겼어요.”</p>
      <p class='muted'>— 학부모 A</p>
    </div>
    """, unsafe_allow_html=True)
with t2:
    st.markdown("""
    <div class='card'>
      <p>“Pygame으로 만든 게임을 친구들에게 보여주며 자신감이 크게 올랐습니다!”</p>
      <p class='muted'>— 중1 학생 B</p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Schedule & Availability
# -----------------------------
st.markdown("### 진행 가능 시간")
today = datetime.now()
slots = [(today + timedelta(days=i)).strftime("%m/%d(%)") for i in range(1,6)]
colA, colB = st.columns([0.5,0.5])
with colA:
    st.write("평일: 16:00 ~ 21:00 (KST)")
    st.write("주말: 10:00 ~ 18:00 (KST)")
with colB:
    st.write("원격(Zoom/Google Meet) · 대면(협의)")
    st.write("결석 시 1회까지 보강 제공(사전 협의)")

# -----------------------------
# Inquiry / Enrollment Form
# -----------------------------
st.markdown("### 문의 · 신청")
with st.form(key="inquiry_form"):
    cols = st.columns(2)
    with cols[0]:
        name = st.text_input("이름 / 학생명")
        contact = st.text_input("연락처(이메일 또는 카카오톡 ID)")
        level = st.selectbox("학년/레벨", ["초등", "중등", "고등", "대학/성인", "기타"])
    with cols[1]:
        track = st.multiselect("관심 분야(복수 선택)", ["파이썬 기초", "Pygame 게임", "데이터 분석", "SQL", "Streamlit", "IGCSE CS"])
        mode = st.radio("수업 형태", ["1:1 개인", "2~3인 소그룹", "단기 부트캠프"])
        times = st.text_input("가능 시간대 (예: 토 10-12, 화/목 19시)")
    goal = st.text_area("목표/요청사항 (예: 공모전 준비, 포트폴리오, 기초 다지기 등)")
    agreed = st.checkbox("개인정보 수집·이용에 동의합니다 (상담 목적).")
    submitted = st.form_submit_button("제출하기")
    if submitted:
        if not (name and contact and agreed):
            st.warning("이름, 연락처 입력 및 동의가 필요합니다.")
        else:
            st.success("제출되었습니다! 24시간 내로 연락드릴게요. (실제 전송 기능은 배포 시 연결)")

# -----------------------------
# FAQ
# -----------------------------
st.markdown("### 자주 묻는 질문")
with st.expander("Q1. 완전 처음인데 따라갈 수 있을까요?"):
    st.write("가능합니다. 입문자용 커리큘럼과 속도 조절, 충분한 실습과 피드백을 제공합니다.")
with st.expander("Q2. 준비물은 무엇인가요?"):
    st.write("노트북(윈도우/맥), Zoom/Google Meet 설치. 수업 첫날 환경설정을 도와드립니다.")
with st.expander("Q3. 환불/보강 규정은 어떻게 되나요?"):
    st.write("첫 수업 전 전액 환불. 시작 후에는 진행 회차 기준 정산. 결석 1회 보강 가능(사전 협의).")

# -----------------------------
# CTA Footer
# -----------------------------
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
cta1, cta2, cta3 = st.columns([0.22,0.22,0.56])
with cta1:
    st.link_button("📅 수업 일정 문의", "https://forms.gle/your-google-form", use_container_width=True)
with cta2:
    st.link_button("💬 카카오톡 상담", "https://pf.kakao.com/_yourchannel", use_container_width=True)
with cta3:
    st.link_button("📧 이메일 문의", "mailto:your@email.com?subject=코딩%20수업%20문의", use_container_width=True)

st.markdown("---")
st.markdown("<div class='footer'>© 2025 코딩 클래스 — 파이썬, 게임 제작, 데이터분석, IGCSE CS</div>", unsafe_allow_html=True)

# -----------------------------
# Simple pageview counter in session
# -----------------------------
if "pv" not in st.session_state:
    st.session_state.pv = 0
st.session_state.pv += 1
st.caption(f"Page views (this session): {st.session_state.pv}")
