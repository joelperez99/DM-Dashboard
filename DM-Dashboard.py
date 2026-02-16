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

/* Quitar padding grande */
.block-container{
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}

/* Espacio vertical para centrar */
.login-spacer {
  height: 16vh;
}

/* Contenedor compacto */
.compact-wrap {
  max-width: 360px;
  margin: 0 auto;
}

/* CENTRADO TOTAL del bloque (logo + títulos) */
.center-block {
  text-align: center;
}

/* Logo centrado */
.login-logo {
  width: 220px;          /* más grande (ajusta aquí) */
  max-width: 90%;
  height: auto;
  display: block;
  margin: 0 auto 18px auto;  /* centrado */
}

/* Input y botón */
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

    st.markdown('<div class="login-spacer"></div>', unsafe_allow_html=True)

    left, center, right = st.columns([1.4, 1, 1.4])

    with center:

        st.markdown('<div class="compact-wrap">', unsafe_allow_html=True)

        # TODO centrado
        st.markdown('<div class="center-block">', unsafe_allow_html=True)

        # LOGO centrado y más grande
        st.markdown(
            '<img src="https://i.postimg.cc/tJvFx7V6/463003060-8370865312967718-7946847523939617482-n.jpg" class="login-logo">',
            unsafe_allow_html=True
        )

        st.markdown("<h2 style='margin:0 0 6px 0;'>🔐 Acceso Privado</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='margin:0 0 20px 0;'>DM Sales3</h4>", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)  # cierre center-block

        pwd = st.text_input("Contraseña", type="password")

        if st.button("Entrar"):
            if pwd == PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta")

        st.markdown('</div>', unsafe_allow_html=True)  # cierre compact-wrap

    st.stop()

# ===============================
# DASHBOARD
# ===============================
POWERBI_URL = "https://app.powerbi.com/view?r=eyJrIjoiZTRmN2JiMzAtYmUyOS00MTYxLWI5OGUtM2MwN2FmYTg5OTQzIiwidCI6ImMyZjliMjM5LTE0YTEtNDgyZi1hMTAyLTQyYjE0NTgzMzFjOSf4g"

st.markdown(
    f"""<iframe class="pbi-frame" src="{POWERBI_URL}" allowfullscreen="true"></iframe>""",
    unsafe_allow_html=True
)
