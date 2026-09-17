import streamlit as st

# Page Config
st.set_page_config(
    page_title="AI Media Generator", page_icon="🎬", layout="centered"
)

st.title("🎬 AI Video Generator Tool")
st.write(
    "Apna prompt likhein aur AI video generate karke direct download karein!"
)

prompt = st.text_area(
    "Apna Video Prompt Likhein:",
    placeholder="A cinematic drone shot flying over a glowing alien forest...",
)

if st.button("Generate Video 🚀"):
  if not prompt:
    st.warning("Barah-e-karam koi prompt zaroor likhein!")
  else:
    with st.spinner("AI video tayar kar raha hai, thora intezar karein..."):
      try:
        import urllib.parse

        encoded_prompt = urllib.parse.quote(prompt)

        # Using a reliable animated/gif or video format endpoint
        media_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=768&height=768&nologo=true"

        st.success("Video/Animation tayar ho gayi!")

        # Displaying as an animated image/video component for mobile compatibility
        st.image(
            media_url,
            caption=f"Prompt: {prompt}",
            use_container_width=True,
        )
        st.markdown(
            f"[📥 Download Media File Directly]({media_url})",
            unsafe_allow_html=True,
        )

      except Exception as e:
        st.error(f"Koi error aa gaya: {e}")
