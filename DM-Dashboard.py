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
# CSS (LOGIN ESTILO TARJETA)
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

/* Quitar padding general */
.block-container { padding: 0 !important; }

/* Wrapper centrado */
.login-wrapper{
  position: fixed;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Tarjeta */
.login-card{
  width: 520px;
  max-width: 92vw;
  padding: 42px 44px;
  border-radius: 18px;
  background: #ffffff;
  box-shadow: 0 12px 40px rgba(0,0,0,.08);
  border: 1px solid rgba(0,0,0,.06);
}

/* Título grande */
.login-title{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  font-size: 52px;
  font-weight: 800;
  line-height: 1.05;
  margin: 0;
  color: #1f2937;
}

/* Subtítulo */
.login-subtitle{
  text-align: center;
  margin-top: 14px;
  margin-bottom: 26px;
  font-size: 28px;
  font-weight: 700;
  color: #2b2f36;
}

/* Label */
.login-label{
  font-size: 16px;
  color: #6b7280;
  margin: 0 0 8px 0;
  font-weight: 600;
}

/* Forzar ancho del input */
.login-card div[data-baseweb="input"]{
  width: 100%;
}

/* Botón ancho completo */
.login-card .stButton > button{
  width: 100%;
  height: 48px;
  border-radius: 10px;
  font-size: 18px;
  font-weight: 700;
  margin-top: 14px;
}

/* Ajuste input (altura y bordes) */
.login-card input{
  height: 46px !important;
  border-radius: 10px !important;
}

/* Mensajes de error más centrados */
.login-card .stAlert{
  margin-top: 12px;
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
# AUTH
# ===============================
PASSWORD = st.secrets["APP_PASSWORD"]

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ===============================
# LOGIN
# ===============================
if not st.session_state.authenticated:

    st.markdown('<div class="login-wrapper"><div class="login-card">', unsafe_allow_html=True)

    st.markdown("""
      <div class="login-title">🔐 <span>Acceso Privado</span></div>
      <div class="login-subtitle">DM Sales3</div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-label">Contraseña</div>', unsafe_allow_html=True)
    password = st.text_input("", type="password", label_visibility="collapsed")

    if st.button("Entrar"):
        if password == PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta")

    st.markdown('</div></div>', unsafe_allow_html=True)
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
