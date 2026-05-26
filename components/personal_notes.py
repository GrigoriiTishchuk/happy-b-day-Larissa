import streamlit as st
from dotenv import load_dotenv, dotenv_values
from components.observation_pdf import generate_observation_report
load_dotenv()

def render_pdf():
    st.subheader("Restricted Field Archive Export")
    st.markdown("""
    This archive contains classified observational data.
    Access is restricted due to emotional sensitivity protocols.
    """)
    CORRECT_PASSWORD = dotenv_values().get("CORRECT_PASSWORD", "cheese man")
    st.markdown("""
    Hint:  
    We both love cheese, but I have a unique title, that you gave me.
    """)

    password = st.text_input("Enter access password", type="password", placeholder="Enter cheese-related password")
    # INIT STATE
    if "pdf_buffer" not in st.session_state:
        st.session_state.pdf_buffer = None
    if password:
        if password.lower() == CORRECT_PASSWORD:
            st.success("Access granted. Emotional clearance verified.")
            if st.button("Generate Field Observation PDF"):
                if st.session_state.pdf_buffer is None:
                    with st.spinner("Compiling field notes..."):
                        st.session_state.pdf_buffer = generate_observation_report()
            if st.session_state.pdf_buffer is not None:
                st.download_button(
                    label="Download Field Report",
                    data=st.session_state.pdf_buffer,
                    file_name="field_observations.pdf",
                    mime="application/pdf"
                )

        else:
            st.error("Access denied. Incorrect emotional key.")