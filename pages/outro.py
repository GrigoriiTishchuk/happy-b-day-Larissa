import streamlit as st
def render_outro():
    st.markdown(
        """
        <div style="text-align: center; padding: 40px;">
            <h2>Final Archive Unlocked</h2>
            <h3>Congratulations! You've explored all the sections and unlocked the final archive.</h3>
            <br>
            <h4>Thank you for being part of this emotional research journey.</h4>
            <h4>Here is the final message from the lead researcher:</h4>
        </div>
        """,
        unsafe_allow_html=True
    )
    # VIDEO
    video_file = open("assets/video/final.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.markdown("---")
    st.caption("End of report.")
    

render_outro()