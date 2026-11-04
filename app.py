import streamlit as st

st.set_page_config(
    page_title="UPM - Ultimate Prediction Machine",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Ultimate Prediction Machine")
st.caption("Plataforma de análise e previsões desportivas")

st.info(
    "UPM em construção. As previsões só serão apresentadas "
    "quando existirem dados suficientes e testes que as validem."
)

tab1, tab2, tab3 = st.tabs([
    "⚽ Futebol",
    "🏀 Basquetebol",
    "📊 Centro de controlo"
])

with tab1:
    st.header("Motor de Futebol")
    st.write("BTTS | Mais/Menos golos | Golos das equipas")
    st.write("Cantos | 1X2 | Dupla possibilidade")
    st.warning("Aguardando integração de dados e modelos.")

with tab2:
    st.header("Motor de Basquetebol")
    st.write("Mais/Menos pontos | Total por equipa")
    st.write("Vencedor | Handicap | Pontos por período")
    st.warning("Aguardando integração de dados e modelos.")

with tab3:
    st.header("Centro de controlo")
    st.metric("Desportos", "2")
    st.metric("Filtro", "Rigoroso")
    st.metric("Previsões validadas", "0")
    st.write("Nenhuma previsão será aprovada sem validação.")
