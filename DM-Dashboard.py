import streamlit as st

# ===============================
# CONFIGURACIÓN DE PÁGINA
# ===============================
st.set_page_config(
    page_title="DM Sales3",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ===============================
# CSS: FULLSCREEN + QUITAR BARRAS
# ===============================
st.markdown("""
<style>
/* Ocultar elementos de Streamlit */
header {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}
[data-testid="stDecoration"] {display: none;}
[data-testid="stStatusWidget"] {display: none;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Quitar padding/espacios del contenedor principal */
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
}

/* Quitar margen del body */
html, body {
    margin: 0 !important;
    padding: 0 !important;
    height: 100% !important;
}

/* Iframe full screen */
.pbi-frame {
    width: 100vw;
    height: 100vh;
    border: 0;
    display: block;
}

/* Cuando hay login (pantalla de password) centrado */
.login-wrap {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 12px;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# PASSWORD DESDE SECRETS
# ===============================
PASSWORD = st.secrets["APP_PASSWORD"]

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ===============================
# LOGIN
# ===============================
if not st.session_state.authenticated:
    st.markdown("<div class='login-wrap'><h1>🔐 Acceso Privado</h1><h3>DM Sales3</h3></div>", unsafe_allow_html=True)

    # Centramos el input con columnas
    c1, c2, c3 = st.columns([2, 1.2, 2])
    with c2:
        pwd = st.text_input("Contraseña", type="password")
        if st.button("Entrar", use_container_width=True):
            if pwd == PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ Contraseña incorrecta")

    st.stop()

# ===============================
# DASHBOARD POWER BI (FULL SCREEN)
# ===============================
POWERBI_URL = "https://app.powerbi.com/view?r=eyJrIjoiN2U5MTBhODMtYzgxOS00OTY4LThjMGEtYTRkMmFkMDgzMGFkIiwidCI6ImMyZjliMjM5LTE0YTEtNDgyZi1hMTAyLTQyYjE0NTgzMzFjOSJ9"

st.markdown(
    f"""
    <iframe class="pbi-frame"
        title="DM Sales3"
        src="{POWERBI_URL}"
        allowfullscreen="true">
    </iframe>
    """,
    unsafe_allow_html=True
)
