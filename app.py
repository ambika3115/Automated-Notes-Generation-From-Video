import gradio as gr
from agent import run_pipeline

def process(video):
    video_path = video["name"] if isinstance(video, dict) else video
    notes, file_path = run_pipeline(video_path)
    return notes, file_path


interface = gr.Interface(
    fn=process,
    inputs=[
        gr.Video(label="Upload Video")
    ],
    outputs=[
        gr.Textbox(label="Generated Notes"),
        gr.File(label="Download Notes")
    ],
)

interface.launch()