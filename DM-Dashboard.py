import streamlit as st

# ===============================
# CONFIGURACIÓN
# ===============================
st.set_page_config(
    page_title="DM Sales3",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ===============================
# CSS GLOBAL
# ===============================
st.markdown("""
<style>

/* Ocultar elementos Streamlit */
header {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}
[data-testid="stDecoration"] {display: none;}
[data-testid="stStatusWidget"] {display: none;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Quitar padding */
.block-container {
    padding: 0rem !important;
    max-width: 100% !important;
}

/* Centrado absoluto del login */
.login-container {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

/* Caja login */
.login-box {
    width: 320px;
}

/* Iframe fullscreen */
.pbi-frame {
    width: 100vw;
    height: 100vh;
    border: 0;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# PASSWORD
# ===============================
PASSWORD = st.secrets["APP_PASSWORD"]

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ===============================
# LOGIN
# ===============================
if not st.session_state.authenticated:

    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    st.markdown("""
        <h1 style='text-align:center;'>🔐 Acceso Privado</h1>
        <h3 style='text-align:center; margin-bottom:40px;'>DM Sales3</h3>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    password = st.text_input("Contraseña", type="password")

    if st.button("Entrar", use_container_width=True):
        if password == PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta")

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

# ===============================
# DASHBOARD FULL SCREEN
# ===============================
POWERBI_URL = "https://app.powerbi.com/view?r=eyJrIjoiN2U5MTBhODMtYzgxOS00OTY4LThjMGEtYTRkMmFkMDgzMGFkIiwidCI6ImMyZjliMjM5LTE0YTEtNDgyZi1hMTAyLTQyYjE0NTgzMzFjOSJ9"

st.markdown(
    f"""
    <iframe class="pbi-frame"
        src="{POWERBI_URL}"
        allowfullscreen="true">
    </iframe>
    """,
    unsafe_allow_html=True
)
