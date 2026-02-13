import streamlit as st

# ===============================
# CONFIGURACIÓN DE PÁGINA
# ===============================

st.set_page_config(
    page_title="DM Sales3",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===============================
# OCULTAR HEADER Y ESPACIOS
# ===============================

st.markdown("""
<style>

/* Ocultar barra superior */
header {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}
[data-testid="stDecoration"] {display: none;}
[data-testid="stStatusWidget"] {display: none;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Quitar espacio superior */
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

/* Quitar padding lateral */
.main .block-container {
    padding-left: 0rem;
    padding-right: 0rem;
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

    st.markdown("""
    <div style='text-align:center; margin-top:150px;'>
        <h1>🔐 Acceso Privado</h1>
        <h3>DM Sales3</h3>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,1,2])

    with col2:
        password = st.text_input("Contraseña", type="password")

        if st.button("Entrar", use_container_width=True):
            if password == PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta")

    st.stop()

# ===============================
# DASHBOARD POWER BI
# ===============================

POWERBI_URL = "https://app.powerbi.com/view?r=eyJrIjoiN2U5MTBhODMtYzgxOS00OTY4LThjMGEtYTRkMmFkMDgzMGFkIiwidCI6ImMyZjliMjM5LTE0YTEtNDgyZi1hMTAyLTQyYjE0NTgzMzFjOSJ9"

st.markdown(
    f"""
    <iframe 
        title="DM Sales3"
        width="100%"
        height="900"
        src="{POWERBI_URL}"
        frameborder="0"
        allowFullScreen="true">
    </iframe>
    """,
    unsafe_allow_html=True
)
