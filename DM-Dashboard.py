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
# CSS: quitar UI y centrar
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

/* Quitar padding grande */
.block-container{
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}

/* Centrar vertical el “bloque” de login */
.login-spacer {
  height: 18vh;
}

/* Compactar input + botón (ancho fijo) */
.compact-wrap {
  max-width: 360px;
  margin: 0 auto;
}

/* Input y botón 100% del wrap */
.compact-wrap div[data-baseweb="input"]{
  width: 100% !important;
}

.compact-wrap input{
  height: 46px !important;
  border-radius: 10px !important;
}

.compact-wrap .stButton > button{
  width: 100% !important;
  height: 48px !important;
  border-radius: 10px !important;
  font-size: 18px !important;
  font-weight: 700 !important;
  margin-top: 12px !important;
}

/* Iframe full screen */
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
# AUTH
# ===============================
PASSWORD = st.secrets["APP_PASSWORD"]
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ===============================
# LOGIN (centrado y compacto)
# ===============================
if not st.session_state.authenticated:

    # Espaciador para centrar visualmente (ajusta 18vh si lo quieres más arriba/abajo)
    st.markdown('<div class="login-spacer"></div>', unsafe_allow_html=True)

    # 3 columnas: todo va en la del centro
    left, center, right = st.columns([1.4, 1, 1.4])

    with center:
        st.markdown("<h1 style='text-align:center; margin-bottom:6px;'>🔐 Acceso Privado</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center; margin-top:0; margin-bottom:22px;'>DM Sales3</h3>", unsafe_allow_html=True)

        st.markdown('<div class="compact-wrap">', unsafe_allow_html=True)

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
# DASHBOARD
# ===============================
POWERBI_URL = "https://app.powerbi.com/view?r=eyJrIjoiN2U5MTBhODMtYzgxOS00OTY4LThjMGEtYTRkMmFkMDgzMGFkIiwidCI6ImMyZjliMjM5LTE0YTEtNDgyZi1hMTAyLTQyYjE0NTgzMzFjOSJ9"

st.markdown(
    f"""<iframe class="pbi-frame" src="{POWERBI_URL}" allowfullscreen="true"></iframe>""",
    unsafe_allow_html=True
)
