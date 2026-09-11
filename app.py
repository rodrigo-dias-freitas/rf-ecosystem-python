import streamlit as st
import pandas as pd

# 1. Configuração de página e estado da barra lateral
st.set_page_config(
    page_title = "RF System",
    page_icon = "🔴",
    layout= "wide",
    initial_sidebar_state= "expanded"
)

# 2. Carregamento dos dados da planilha via Pandas
@st.cache_data
def carregar_dados():
    try:
        return pd.read_excel("indicadores_internacionais.xlsx")
    except FileNotFoundError:
        return pd.DataFrame({
            "PDFP":[3.38],
            "GDP NOW":[1.68],
            "PCE_INFLATION":[2.47]
        })
df = carregar_dados()

# 3. Navegação Lateral (Sidebar)
with st.sidebar:
    st.title("RF SYSTEM")
    st.caption("WIN: 128.450 (+0.45%) | IPCA: 0.16%")
    st.divider()

    st.button("Dashboard", use_container_width=True, type="primary")
    st.button("SFLIM Logics", use_container_width=True)
    st.button("Gestão FII", use_container_width=True)
    st.button("Mixology UI", use_container_width=True)

# 4. Perfil / Apresentação
with st.container():
    col_foto, col_info = st.columns([1,11])
    with col_foto:
        st.subheader("")
    with col_info:
        st.subheader("Rodrigo Freitas — UI/UX & Financial Analyst")
        st.caption("Mais de 20 anos unindo design de alta performance à lógica analítica. Desenvolvedor do sistema SFLIM.")

st.divider()

# 5. Indicadores Econômicos Internacionais
st.header("INDICADORES ECONÔMICOS INTERNACIONAIS")
st.caption("US MACRO DRIVERS & FED PROJECTIONS")

col_fed, col_petr = st.columns([3,1])
with col_fed:
    st.info("PROVÁVEL TOM DO FED: **NEUTRAL**")
with col_petr:
    st.metric(label="BARRIL DE PETRÓLEO", value="$ 0.00")

# Metrics / KPIs do Dashboard
c1, c2, c3 = st.columns(3)

val_pdfp = df["PDFP"].iloc[-1] if "PDFP" in df.columns else 3.38
val_gdp = df["GDP_NOW"].iloc[-1] if "GDP_NOW" in df.columns else 1.68
val_pce = df["PCE_INFLATION"].iloc[-1] if "PCE_INFLATION" in df.columns else 2.47

c1.metric(
    label="PDFP DEMAND (EST.)",
    value=f"{val_pdfp}%",
    delta="SUSTENTADO",
    help="Compras finais domésticas privadas"
)

c2.metric(
    label="GDP NOW (EST.)",
    value=f"{val_gdp}%",
    delta="FRAGILIDADE ALTA",
    delta_color="inverse",
    help="Mede a taxa geral da economia"
)

c3.metric(
    label="PCE INFLATION (EST.)",
    value=f"{val_pce}%",
    delta="SUSTENTADO",
    help="Métrica principal de inflação do FED"
)

st.divider()

# 6. Estrutura de Motores Macro
st.subheader("ESTRUTURA DE MOTORES MACRO")

m1, m2, m3, m4 = st.columns(4)
m1.metric("PCE", "▼ DESCENDO", delta_color="inverse")
m2.metric("ISM", "▲ SUBINDO", delta_color="normal")
m3.metric("CES", "• FRACO", delta_color="off")
m4.metric("UNEMPLOYMENT RATE", "▼ DESCENDO", delta_color="inverse")

st.divider()

# 7. Projeções IPCA (SFLIM vs IBGE)
st.subheader("PROJEÇÕES IPCA (SFLIM VS IBGE)")

ipca1, ipca2, ipca3 = st.columns(3)

with ipca1:
    st.caption("Março 2026")
    st.metric("SFLIM / REAL", "0.46% | 0.88%", delta="DIVERGÊNCIA DE MERCADO", delta_color="inverse")

with ipca2:
    st.caption("Fevereiro 2026")
    st.metric("SFLIM / REAL", "0.75% | 0.70%", delta="ALTA PRECISÃO")

with ipca3:
    st.caption("Janeiro 2026")
    st.metric("SFLIM / REAL", "0.33% | 0.23%", delta="ALTA PRECISÃO")