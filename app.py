import streamlit as st

# Page Config
st.set_page_config(
    page_title="AI Wallpaper Generator", page_icon="🖼️", layout="centered"
)

st.title("🖼️ AI Wallpaper & Art Generator")
st.write(
    "Apna pasandeeda khayal (prompt) likhein aur high-resolution AI wallpaper"
    " banayein!"
)

prompt = st.text_area(
    "Wallpaper Prompt Likhein:",
    placeholder=(
        "A beautiful scenic mountain view at sunset, 4k, ultra detailed..."
    ),
)

# Wallpaper Size Options
size_option = st.selectbox(
    "Wallpaper Size Select Karein:",
    ["Mobile Portrait (Vertical)", "Desktop Landscape (Horizontal)"],
)

if size_option == "Mobile Portrait (Vertical)":
  width, height = 512, 896
else:
  width, height = 896, 512

if st.button("Generate Wallpaper 🚀"):
  if not prompt:
    st.warning("Barah-e-karam koi prompt zaroor likhein!")
  else:
    with st.spinner(
        "Aapka shandar wallpaper tayar ho raha hai, intezar karein..."
    ):
      try:
        import urllib.parse

        encoded_prompt = urllib.parse.quote(prompt)
        wallpaper_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&nologo=true"

        st.success("Wallpaper kamyabi se ban gaya!")
        st.image(
            wallpaper_url, caption=f"Prompt: {prompt}", use_container_width=True
        )
        st.markdown(
            f"[📥 Download HD Wallpaper]({wallpaper_url})",
            unsafe_allow_html=True,
        )

      except Exception as e:
        st.error(f"Koi error aa gaya: {e}")
