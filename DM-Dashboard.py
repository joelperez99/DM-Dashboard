import streamlit as st

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
/* Quitar UI Streamlit */
header {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}
[data-testid="stDecoration"] {display: none;}
[data-testid="stStatusWidget"] {display: none;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Quitar padding general */
.block-container { padding: 0 !important; }

/* Centrar todo el contenido del login */
.login-page {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Tarjeta (box) */
.login-card {
  width: 520px;
  max-width: 92vw;
  padding: 44px 44px 34px 44px;
  border-radius: 18px;
  background: #ffffff;
  border: 1px solid rgba(0,0,0,.06);
  box-shadow: 0 12px 40px rgba(0,0,0,.08);
}

/* Título */
.login-title {
  display:flex;
  align-items:center;
  justify-content:center;
  gap: 14px;
  font-size: 52px;
  font-weight: 800;
  margin: 0;
  color: #1f2937;
  line-height: 1.05;
}

/* Subtítulo */
.login-subtitle {
  text-align:center;
  margin-top: 12px;
  margin-bottom: 26px;
  font-size: 28px;
  font-weight: 700;
  color: #2b2f36;
}

/* Label */
.login-label {
  font-size: 16px;
  font-weight: 600;
  color: #6b7280;
  margin-bottom: 8px;
}

/* Input y botón: que no se estiren raro */
.login-card div[data-baseweb="input"]{
  width: 100% !important;
}

.login-card input{
  height: 46px !important;
  border-radius: 10px !important;
}

.login-card .stButton > button{
  width: 100% !important;
  height: 48px !important;
  border-radius: 10px !important;
  font-size: 18px !important;
  font-weight: 700 !important;
  margin-top: 14px !important;
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
# LOGIN
# ===============================
if not st.session_state.authenticated:
    # Capa de centrado
    st.markdown('<div class="login-page">', unsafe_allow_html=True)

    # Usamos columnas para forzar que TODO quede dentro del ancho (tarjeta)
    left, center, right = st.columns([1, 2, 1])

    with center:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)

        st.markdown("""
            <div class="login-title">🔐 <span>Acceso Privado</span></div>
            <div class="login-subtitle">DM Sales3</div>
            <div class="login-label">Contraseña</div>
        """, unsafe_allow_html=True)

        pwd = st.text_input("", type="password", label_visibility="collapsed")

        if st.button("Entrar"):
            if pwd == PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta")

        st.markdown('</div>', unsafe_allow_html=True)

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
