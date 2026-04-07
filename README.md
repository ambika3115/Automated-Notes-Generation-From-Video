🚀 Automated Notes Generation From Video

📌 Overview:
Automated Notes Generation From  Video is a system that automatically converts video content into structured and meaningful notes. It simplifies learning by eliminating manual note-taking and delivers organized notes in PDF format via email.


🚀 Features:
- 🎧 Upload MP3 / Video files
- 🗣️ Automatic Speech-to-Text transcription
- 🧠 AI-based note generation
- 📝 Structured notes (headings, bullet points, summary)
- 📄 PDF generation
- 📧 Email delivery to multiple users
- 💻 User-friendly GUI using Gradio


🏗️ System Architecture:

Input (Audio/Video)
↓

Audio Extraction (if video)
↓

Speech-to-Text (Whisper)
↓

AI Note Generation (LLM)
↓

PDF Creation
↓

Email Delivery


🛠️ Technologies Used:
- Programming Language: Python  
- Frontend: Gradio  
- Audio Processing: MoviePy  
- Speech Recognition: Whisper  
- AI Model: Gemini 
- PDF Generation: FPDF  
- Email Service: SMTP 

📂 Project Structure:
Automated Notes Generation From Video/
│
├── app.py
├── agent.py
├── .env
├── requirements.txt
│
├── modules/
│ ├── audio_extractor.py
│ ├── transcriber.py
│ ├── note_generator.py
│ ├── pdf_generator.py
│ ├── email_sender.py
│
├── outputs/
│ ├── audio/
│ ├── notes/


⚙️ Installation:
1. Clone the repository:
git clone https://github.com/ambika3115/Automated-Notes-Generation-From-Video.git

cd Automated_Notes_Generation_From_Video

3. Create virtual environment (windows):
python -m venv venv
venv\Scripts\activate

4. Install dependencies:
pip install -r requirements.txt

5. Add `.env` file:
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
GEMINI_API_KEY=your_api_key

6. Run the application:
python app.py


7. ▶️ Usage:
- Open browser: `http://127.0.0.1:7860`
- Upload audio/video file
- Get generated notes
- Download PDF
- Notes will be sent via email automatically


🎯 Objectives:
1. To eliminate the need for manual note-taking by automatically extracting key information from video content.
2. To produce AI-powered structured notes using LLM to organize content into clean, easy-to-read notes with clear headings, summaries, and key points.
3. To send generated notes automatically via Email without any manual effort.


✅ Advantages:
- Saves time  
- Easy to use  
- Supports multiple users  
- Improves productivity  
- Works with long content 


⚠️ Limitations:
- Slower on CPU  
-  Depends on audio quality  
- Requires internet for AI processing 


🔮 Future Scope:
- Real-time note generation  
- Multi-language support   
- YouTube link input  
- GPU acceleration for faster processing
