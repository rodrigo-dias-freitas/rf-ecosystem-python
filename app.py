import streamlit as st
import pandas as pd



# 1. Configuração de página e estado da barra lateral
st.set_page_config(
    page_title = "RF System",
    page_icon = "🔴",
    layout= "wide",
    initial_sidebar_state= "expanded"
)

URL_GOOGLE_SHEETS = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRQEc5xPNzM70nrMBKE7lr1kJPee-9Zg9TeTrP1dy8B4454VN9NZP596INODDyF0w/pub?gid=397532593&single=true&output=csv"

# 2. Carregamento dos dados da planilha via Pandas
@st.cache_data(ttl=60)
def carregar_dados(url):
    return pd.read_csv(url, header=None)

try:
    df = carregar_dados(URL_GOOGLE_SHEETS)

    # PDFP DEMAND (linha 5, coluna 7)
    raw_pdfp = df.iloc[5, 7] if df.shape[0] > 5 and df.shape[1] > 7 else 0
    val_pdfp = float(str(raw_pdfp).replace(",", ".").strip()) if pd.notna(raw_pdfp) else 0.0

    delta_pdfp = str(df.iloc[9, 9]).strip() if df.shape[0] > 9 and pd.notna(df.iloc[9, 9]) else "SUSTENTADO"

    # GDP NOW (linha 5, coluna 12)
    raw_gdp = df.iloc[5, 12] if df.shape[0] > 5 and df.shape[1] > 12 else 0
    val_gdp = float(str(raw_gdp).replace(",", ".").strip()) if pd.notna(raw_gdp) else 0.0

    delta_gdp = str(df.iloc[9, 14]).strip() if df.shape[0] > 9 and pd.notna(df.iloc[9, 14]) else "ALTA"

    # PCE INFLATION (linha 5, coluna 17)
    raw_pce = df.iloc[5, 17] if df.shape[0] > 5 and df.shape[1] > 17 else 0
    val_pce = float(str(raw_pce).replace(",", ".").strip()) if pd.notna(raw_pce) else 0.0

    delta_pce = str(df.iloc[9, 19]).strip() if df.shape[0] > 9 and pd.notna(df.iloc[9, 19]) else "SUSTENTADO"

    # Tom do FED (linha 11, coluna 1)
    fed_tone = str(df.iloc[11, 1]).strip() if df.shape[0] > 11 and df.shape[1] > 1 and pd.notna(df.iloc[11, 1]) else "NEUTRAL"

    st.success("✅ Conectado ao Google Sheets em tempo real!")

except Exception as e:
    # Imprime no terminal o erro real para sabermos o motivo da exceção
    print(f"⚠️ ERRO DETALHADO NO GOOGLE SHEETS: {e}")
    
    # Fallback de segurança em caso de oscilação de conexão
    val_pdfp = 0.0
    val_gdp = 0.0
    val_pce = 0.0
    fed_tone = "S/N"


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
    st.info(f"PROVÁVEL TOM DO FED: **{fed_tone}**")
with col_petr:
    st.metric(label="BARRIL DE PETRÓLEO", value="$ 0.00")

# Metrics / KPIs do Dashboard
c1, c2, c3 = st.columns(3)

c1.metric(
    label="PDFP DEMAND (EST.)",
    value=f"{val_pdfp}%",
    delta=delta_pdfp,
    help="Compras finais domésticas privadas"
)

c2.metric(
    label="GDP NOW (EST.)",
    value=f"{val_gdp}%",
    delta=delta_gdp,
    help="Mede a taxa geral da economia"
)

c3.metric(
    label="PCE INFLATION (EST.)",
    value=f"{val_pce}%",
    delta=delta_pce,
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