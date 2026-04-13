
# -----------------------------
# Title
# -----------------------------
st.title("🤖 AI Posting Agent")
st.markdown("Generate expert-level posts for different platforms")

# -----------------------------
# Input Section
# -----------------------------
topic = st.text_input("Enter Topic", placeholder="e.g. AI Resume Screening")

platform = st.selectbox(
    "Select Platform",
    ["LinkedIn", "Twitter", "Instagram"]
)

# -----------------------------
# Generate Function (Ollama)
# -----------------------------
def generate_post(topic, platform):
    prompt = f"""
    Write a professional {platform} post about {topic}.

    Include:
    - Strong hook
    - Problem
    - Solution
    - Tech insights
    - Relevant hashtags

    Make it engaging and expert-level.
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    except:
        return "❌ Error connecting to Ollama. Make sure it is running."

# -----------------------------
# Button Action
# -----------------------------
if st.button("🚀 Generate Post"):
    if not topic:
        st.warning("⚠️ Please enter a topic")
    else:
        with st.spinner("Generating..."):
            post = generate_post(topic, platform)

        st.success("✅ Post Generated!")

        st.text_area("📄 Your Post", post, height=300)

        st.download_button(
            label="📥 Download Post",
            data=post,
            file_name="post.txt",
            mime="text/plain"
        )
