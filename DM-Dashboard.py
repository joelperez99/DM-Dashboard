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

/* Ocultar UI de Streamlit */
header {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}
[data-testid="stDecoration"] {display: none;}
[data-testid="stStatusWidget"] {display: none;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Quitar padding */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}

/* Centrado vertical */
.login-spacer {
    height: 18vh;
}

/* Contenedor compacto */
.compact-wrap {
    max-width: 380px;
    margin: 0 auto;
    text-align: center;
}

/* Logo */
.logo-wrap {
    text-align: center;
    margin-bottom: 25px;
}

.logo-wrap img {
    width: 240px;
    max-width: 90%;
    height: auto;
}

/* Input */
.compact-wrap div[data-baseweb="input"]{
    width: 100% !important;
}

.compact-wrap input{
    height: 46px !important;
    border-radius: 10px !important;
}

/* Botón */
.compact-wrap .stButton > button{
    width: 100% !important;
    height: 48px !important;
    border-radius: 10px !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    margin-top: 12px !important;
}

/* Iframe fullscreen */
.pbi-frame{
    position: fixed;
    top: 0; left: 0;
    width: 100vw;
    height: 100vh;
    border: 0;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# AUTENTICACIÓN
# ===============================
PASSWORD = st.secrets["APP_PASSWORD"]

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ===============================
# LOGIN
# ===============================
if not st.session_state.authenticated:

    st.markdown('<div class="login-spacer"></div>', unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.markdown('<div class="compact-wrap">', unsafe_allow_html=True)

        # LOGO CENTRADO Y GRANDE
        st.markdown("""
        <div class="logo-wrap">
            <img src="https://i.postimg.cc/tJvFx7V6/463003060-8370865312967718-7946847523939617482-n.jpg">
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<h2 style='margin-bottom:6px;'>🔐 Acceso Privado</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='margin-top:0; margin-bottom:20px;'>DM Sales3</h4>", unsafe_allow_html=True)

        pwd = st.text_input("Contraseña", type="password")

        if st.button("Entrar"):
            if pwd == PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta")

        st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

# ===============================
# DASHBOARD FULLSCREEN
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
