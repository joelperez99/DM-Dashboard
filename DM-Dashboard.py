import streamlit as st

st.set_page_config(
    page_title="DM Sales3",
    layout="wide"
)

# ===============================
# PASSWORD DESDE STREAMLIT SECRETS
# ===============================

PASSWORD = st.secrets["APP_PASSWORD"]

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ===============================
# LOGIN
# ===============================

if not st.session_state.authenticated:

    st.markdown("## 🔐 Acceso Privado - DM Sales3")

    password = st.text_input("Ingresa la contraseña", type="password")

    if st.button("Entrar"):
        if password == PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ Contraseña incorrecta")

    st.stop()

# ===============================
# DASHBOARD
# ===============================

st.markdown("## 📊 DM Sales3")

POWERBI_URL = "https://app.powerbi.com/view?r=eyJrIjoiN2U5MTBhODMtYzgxOS00OTY4LThjMGEtYTRkMmFkMDgzMGFkIiwidCI6ImMyZjliMjM5LTE0YTEtNDgyZi1hMTAyLTQyYjE0NTgzMzFjOSJ9"

st.markdown(
    f"""
    <iframe 
        title="DM Sales3"
        width="100%"
        height="750"
        src="{POWERBI_URL}"
        frameborder="0"
        allowFullScreen="true">
    </iframe>
    """,
    unsafe_allow_html=True
)
