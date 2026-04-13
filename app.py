import gradio as gr
from transformers import pipeline

# Load model
generator = pipeline("text-generation", model="gpt2")

def generate_post(topic, platform):
    prompt = f"""
    Write a professional {platform} post about {topic}.
    Include hook, problem, solution, and hashtags.
    """

    result = generator(prompt, max_length=200, num_return_sequences=1)
    return result[0]['generated_text']


def create_post(topic, platform):
    if not topic:
        return "⚠️ Please enter a topic"
    return generate_post(topic, platform)


interface = gr.Interface(
    fn=create_post,
    inputs=[
        gr.Textbox(label="Enter Topic"),
        gr.Dropdown(["LinkedIn", "Twitter", "Instagram"], label="Platform")
    ],
    outputs=gr.Textbox(label="Generated Post"),
    title="🤖 AI Posting Agent",
    description="Generate posts instantly using AI"
)

interface.launch()
