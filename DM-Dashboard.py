import streamlit as st

st.set_page_config(page_title="DM Sales Dashboard", layout="wide")

# --- PASSWORD DESDE SECRETS ---
PASSWORD = st.secrets["APP_PASSWORD"]

# --- SESSION STATE ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --- LOGIN ---
if not st.session_state.authenticated:

    st.title("🔐 Acceso Privado")
    password = st.text_input("Ingresa la contraseña", type="password")

    if st.button("Entrar"):
        if password == PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta")

    st.stop()

# --- DASHBOARD ---
st.title("📊 DM Sales3")

st.markdown(
    """
    <iframe title="DM Sales3"
        width="100%"
        height="600"
        src="https://app.powerbi.com/reportEmbed?reportId=fada8221-7a53-4e42-8f30-1fe1309abfc1&autoAuth=true&ctid=c2f9b239-14a1-482f-a102-42b1458331c9"
        frameborder="0"
        allowFullScreen="true">
    </iframe>
    """,
    unsafe_allow_html=True
)
