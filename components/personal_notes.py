from components.observation_pdf import generate_observation_report
import streamlit as st
from dotenv import load_dotenv, dotenv_values 
load_dotenv()

def render_pdf ():
    st.subheader("Restricted Field Archive Export")
    st.markdown("""
    This archive contains classified observational data.
    Access is restricted due to emotional sensitivity protocols.
    """)
    # PASSWORD SYSTEM
    CORRECT_PASSWORD = dotenv_values().get("CORRECT_PASSWORD", "cheese123")
    st.markdown("""
    Hint: 
    We both love cheese, but I have a unique title, that you gave me.
    """)
    password = st.text_input("Enter access password",type="password")

    # AUTH LOGIC
    if password:
        if password.lower() == CORRECT_PASSWORD:
            st.success("Access granted. Emotional clearance verified.")
            if st.button("Generate Field Observation PDF"):
                with st.spinner("Compiling field notes..."):
                    pdf_path = generate_observation_report()
                    with open(pdf_path, "rb") as f:
                        st.download_button(
                            label="Download Field Report",
                            data=f,
                            file_name="field_observations.pdf",
                            mime="application/pdf"
                        )
        else:
            st.error("Access denied. Incorrect emotional key.")