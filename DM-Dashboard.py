import streamlit as st

# ===============================
# CONFIG
# ===============================
st.set_page_config(
    page_title="DM Sales3",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ===============================
# CSS
# ===============================
st.markdown("""
<style>

/* Ocultar UI Streamlit */
header {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}
[data-testid="stDecoration"] {display: none;}
[data-testid="stStatusWidget"] {display: none;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Quitar padding */
.block-container {
    padding: 0 !important;
}

/* Contenedor centrado */
.login-wrapper {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 320px;
    text-align: center;
}

/* Reducir tamaño del input */
div[data-baseweb="input"] {
    max-width: 320px;
    margin: auto;
}

/* Reducir tamaño del botón */
.stButton > button {
    width: 320px !important;
    margin-top: 10px;
}

.pbi-frame {
    position: fixed;
    top: 0;
    left: 0;
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

    st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)

    st.markdown("<h1>🔐 Acceso Privado</h1>", unsafe_allow_html=True)
    st.markdown("<h4>DM Sales3</h4><br>", unsafe_allow_html=True)

    password = st.text_input("Contraseña", type="password")

    if st.button("Entrar"):
        if password == PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta")

    st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

# ===============================
# DASHBOARD
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
