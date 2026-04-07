from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_notes(transcript):
    prompt = f"""
You are an expert note-taking assistant.

Convert the following transcript into professional, well-structured notes.

Follow these rules strictly:
- Add a clear TITLE at the top
- Use proper HEADINGS
- Use bullet points (•)
- Highlight important keywords in UPPERCASE
- Keep points short and clear
- Add a SUMMARY at the end
- Maintain clean spacing and readability

Format example:

TITLE: ...

1. INTRODUCTION
• Point 1
• Point 2

2. KEY CONCEPTS
• Concept 1
• Concept 2

SUMMARY:
• Key takeaways

Transcript:
{transcript}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text