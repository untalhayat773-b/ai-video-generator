import streamlit as st

# Page Config
st.set_page_config(
    page_title="AI Video Generator", page_icon="🎬", layout="centered"
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
        # Free public AI video generator endpoint / pollination video format
        video_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&nologo=true"

        # Note: Polli-video or standard video link representation
        st.success("Video kamyabi se ban gayi!")

        # Video player & download support
        st.video(video_url)
        st.markdown(f"[📥 Download Video File]({video_url})", unsafe_allow_html=True)

      except Exception as e:
        st.error(f"Koi error aa gaya: {e}")
