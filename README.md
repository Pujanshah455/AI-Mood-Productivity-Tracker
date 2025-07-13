# 🧘 AI Mood & Productivity Tracker (No API Required)

An interactive, offline AI wellness assistant built with **Streamlit**. This app helps users check in with their mood, get personalized **affirmations**, **music**, and **activity** recommendations, and visualize mood trends — no API keys required!

![Mood Tracker Banner](screenshots/banner.png)

---

## 📸 Screenshots

### 🧠 Mood Check-in Interface  
> Choose how you feel or describe your day via text input.

![Mood Check-in](screenshots/mood_checkin.png)

---

### 🔄 Personalized Mood-Based Suggestions  
> Instant affirmations, mood-matching music, and suggested uplifting activities.

![Recommendations](screenshots/recommendations.png)

---

### 🎶 Music Recommendations  
> Happy mood = happy vibes. Embedded YouTube/Audio player.

![Music Recommendations](screenshots/music_recommendations.png)

---

### 🌸 Mindfulness & Wellness Library  
> Includes breathing techniques, grounding tips, and productivity hacks.

![Wellness Library](screenshots/wellness_library.png)

---

### 📊 Mood Analytics  
> See how your mood trends evolve over time using charts.

![Mood Analytics](screenshots/mood_analytics.png)

---

## 🚀 Features

- 😌 **Quick Mood Selector** or journal-style input
- 💡 Emotion analysis using local text model (no OpenAI needed)
- 🌻 **Dynamic affirmations**, music, and tasks
- 🎵 YouTube music recommendations
- 📚 Wellness tools like breathing exercises, grounding
- 📈 Visual mood analytics & mood logs (CSV)
- 🖤 Dark UI Theme using custom CSS

---

## 🛠️ Built With

- `Streamlit`
- `Pandas`, `Matplotlib`
- `sklearn` or lightweight NLP for emotion detection
- No API Keys, runs fully offline

---

## 🧪 How It Works

1. User inputs text or selects emotion.
2. App detects the **mood** using rule-based keywords or ML.
3. Generates:
   - Affirmation ✨
   - Music 🎶
   - Activities 🧘
4. Logs entries with timestamp.
5. Visualizes with graphs & pie charts.

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/ai-mood-tracker.git
cd ai-mood-tracker
pip install -r requirements.txt
streamlit run app.py


You said:
Best AI Projects 2025


ChatGPT said:
Here are some of the Best AI Projects for 2025 🚀 — curated for both beginners and advanced developers to showcase skills in ML, DL, NLP, and AI agent systems. Perfect for portfolios, hackathons, and startups!

🔥 Top AI Projects in 2025
🤖 1. Personal AI Assistant (GPT-powered)
What it does: A smart assistant that answers questions, sets reminders, sends emails, and integrates with apps.
Tools: OpenAI GPT-4o, Whisper (voice input), TTS, LangChain, Python, Streamlit
✅ No API version possible with open models like Phi-3, LLaMA, using LLM Studio

📈 2. Stock Price Prediction App
What it does: Predicts future stock prices using historical data
Tools: LSTM, yfinance, TensorFlow, Streamlit
✅ Deployment-ready on Streamlit Cloud
📊 Add technical indicators like RSI, MACD (via ta library)

🧠 3. AI Mental Health Chatbot
What it does: Chatbot that detects user emotions and responds empathetically
Tools: Emotion Classification (BERT), GPT-4, Streamlit, Firebase, HuggingFace
💡 Add mood tracker, meditation suggestions, music APIs

💼 4. AI Resume Analyzer + Job Matcher
What it does: Extracts skills, experience, and matches with job descriptions
Tools: NLP (spaCy, SBERT), Streamlit, Resume Parser, FAISS, LangChain
✅ Can give job fit % or suggest missing skills

🧘 5. AI Mood & Productivity Tracker
What it does: Tracks mood via text input and suggests affirmations, activities, or music
Tools: GPT-4o, Emotion API, Spotify API, MongoDB, Streamlit
✅ Can be extended into a wellness app

🩺 6. Disease Prediction App
What it does: Predicts diseases like diabetes, heart disease from user input
Tools: Scikit-learn, Flask/Streamlit, Pandas, ML models
✅ Can integrate symptom checker and chatbot interface

📚 7. AI Document Search Engine (Semantic Search)
What it does: Finds relevant documents using embeddings, not keywords
Tools: SBERT, FAISS/Chroma, LangChain, OpenAI/GGUF models
✅ Add PDF upload + Streamlit UI
🎯 Ideal for law, healthcare, research industries

🛒 8. AI-Powered E-Commerce Recommender System
What it does: Suggests products based on user behavior and preferences
Tools: Collaborative Filtering, Content-Based Filtering, NLP, TensorFlow
✅ Integrate into your MERN/Django-based e-commerce store

💬 9. Multilingual AI Translator & Summarizer
What it does: Translates and summarizes large documents or conversations
Tools: NLLB, MarianMT, Pegasus, Streamlit, Whisper
✅ Useful for global teams or cross-lingual education

🔍 10. Fake News Detection
What it does: Classifies news headlines/articles as real or fake
Tools: NLP (TF-IDF, BERT), Scikit-learn, Flask/Streamlit
💡 Integrate browser extension to flag articles in real-time

🌐 BONUS: AI for Social Good Ideas
🌱 Climate Data Forecasting (Rainfall, AQI)

🧑‍⚕️ Early Disease Detection from X-rays using CNNs

📜 Legal Document Classifier

🏫 Student Performance Predictor

✅ Tips for Showcasing
Host with Streamlit, Render, Hugging Face Spaces, or GitHub Pages

Use clear README, live demo, and LinkedIn posts with hashtags

Include "Try it yourself" CTA

Would you like GitHub READMEs, Live Demos, or Deployment Guides for any of the above? I can help you build it end to end.








You said:
🧘 5. AI Mood & Productivity Tracker
What it does: Tracks mood via text input and suggests affirmations, activities, or music                       ✅ Can be extended into a wellness app


ChatGPT said:
Here’s a full description + README-style breakdown for your 🧘‍♀️ AI Mood & Productivity Tracker project — perfect for LinkedIn, GitHub, or your portfolio:

🧘 AI Mood & Productivity Tracker
What it does:
An AI-powered wellness companion that tracks your mood via text input, detects emotional tone, and recommends personalized affirmations, focus activities, relaxation tasks, or mood-boosting music.

✅ Ideal for remote workers, students, or anyone needing a mental health check-in.
✅ Can be extended into a habit tracker, mindfulness journal, or mobile app.

🔍 Features
🧠 Emotion Detection: Uses NLP to classify mood (happy, sad, anxious, angry, neutral)

🌟 AI-Powered Affirmations: GPT generates personalized, positive affirmations

🎶 Spotify Integration: Suggests mood-based playlists using Spotify API

📅 Productivity Tips: Recommends Pomodoro, journaling, or short breaks

📊 Mood Chart: Visualizes mood trends over time (using matplotlib or plotly)

🧘 Wellness Suggestions: Suggests breathing exercises, yoga videos (YouTube API)

🛠️ Tech Stack
Tool	Purpose
Python	Backend logic
Streamlit	Web UI
Transformers (BERT/SentimentClassifier)	Emotion detection
OpenAI GPT / Llama / Phi-3	Affirmation generation
Spotify API	Music recommendations
MongoDB / SQLite	Mood history storage
Matplotlib / Plotly	Mood visualization

📦 Folder Structure
kotlin
Copy
Edit
ai-mood-tracker/
├── app.py
├── emotion_model/
│   └── emotion_classifier.pkl
├── data/
│   └── mood_history.csv
├── utils/
│   └── spotify_api.py
│   └── affirmations.py
└── requirements.txt
🚀 How to Run Locally
bash
Copy
Edit
git clone https://github.com/yourusername/ai-mood-tracker.git
cd ai-mood-tracker
pip install -r requirements.txt
streamlit run app.py
✨ Sample Workflow
User enters: “Feeling unmotivated and anxious today…”

App detects emotion: anxious 😟

Recommends:

✨ Affirmation: "You are doing your best. This moment will pass."

🎧 Spotify Playlist: “Peaceful Piano”

🧘 Activity: 5-minute guided meditation

Logs mood in history and updates graph

💡 Future Enhancements
Daily email mood summary 📧

Integration with Google Calendar for scheduling wellness breaks

Mood-based journaling prompts 📝

Mobile app version (Flutter/React Native) 📱

🏷️ Hashtags for LinkedIn
#AIWellness #MoodTracker #MentalHealthAI #ProductivityTools #AIProjects #StreamlitApp #EmotionalAI #GPT4o #SelfCareWithAI

Would you like me to:

Build the full working app for Streamlit?

Create a demo video or images for LinkedIn?

Help deploy it on Streamlit Cloud or Hugging Face Spaces?

Let me know — I can guide or generate the entire codebase too!








You said:
without api possible because i haven't api keys


ChatGPT said:
Absolutely! You can build the full AI Mood & Productivity Tracker without any paid API keys 💯 using open-source models and local logic.

Here’s a breakdown of how to make it work without APIs like OpenAI or Spotify:

🧘 AI Mood & Productivity Tracker (No API Version)
✅ What It Still Does (Without APIs):
Detects your mood/emotion from text input

Generates affirmations using offline models

Recommends preloaded music links, activities, or tips

Tracks and visualizes mood history

🛠️ Tech Stack (API-Free)
Component	Tool
UI	Streamlit
Emotion Detection	Pretrained BERT or DistilBERT from HuggingFace (no key needed)
Affirmation Generator	Offline small GPT model or rule-based sentences
Music Suggestion	Local .mp3s or YouTube playlist links (stored locally)
Storage	CSV or SQLite
Charting	Matplotlib or Plotly

💡 How to Replace APIs
API Feature	Replace With
GPT	Use open models like distilgpt2 or rule-based affirmations
Spotify	Manually store 5-10 public YouTube playlist links per mood
Firebase/MongoDB	Use CSV or SQLite
YouTube/Google Calendar	Skip or use static links/text

🧠 Sample Affirmations (Offline)
Use a small library or write your own:

python
Copy
Edit
affirmations = {
    "happy": ["Keep smiling! Life loves you back!"],
    "sad": ["You are stronger than you think."],
    "anxious": ["Breathe. Trust. Let go."],
    "angry": ["Let go. Peace is within you."],
    "neutral": ["Stay grounded and present."]
}
🎵 Sample Music Suggestions (YouTube Links)
Store them like this in a dictionary:

python
Copy
Edit
music_links = {
    "happy": "https://youtu.be/9nQO9TQo5XI",
    "sad": "https://youtu.be/3tDHHnWTx6U",
    "anxious": "https://youtu.be/MIr3RsUWrdo",
    "angry": "https://youtu.be/DLZMuOJkBvs",
    "neutral": "https://youtu.be/Y7Q7YZznIWE"
}
📊 Mood Tracker CSV Example
csv
Copy
Edit
date,text_input,emotion
2025-07-13,I feel anxious and tired,anxious
2025-07-14,I’m doing okay today,neutral
🧘 Streamlit App – Key Functions (No API)
detect_emotion(text) – using transformers (e.g. BERT)

get_affirmation(emotion) – from offline list

get_music(emotion) – return from saved YouTube links

save_mood(date, text, emotion) – write to CSV

visualize_mood() – chart moods from CSV

📦 Requirements
nginx
Copy
Edit
streamlit
transformers
torch
pandas
matplotlib
✅ Next Step
Would you like me to generate the full working code (app.py) with:

Offline emotion detection

Predefined affirmations/music

CSV-based tracking

Mood chart?

Just say "Yes, create app.py", and I’ll send it right away!








You said:
i want add readme file


ChatGPT said:
Here's a complete README.md file for your 🧘‍♀️ AI Mood & Productivity Tracker (No API Version) — perfect for GitHub or portfolio documentation:

markdown
Copy
Edit
# 🧘 AI Mood & Productivity Tracker (No API Version)

A simple and elegant AI-powered Streamlit app that tracks your **mood via text input**, detects the emotional tone using a local NLP model, and recommends **affirmations**, **music**, and **activities** — without using any external API keys!

## 🌟 Features

- 🧠 **Emotion Detection** from text (happy, sad, angry, anxious, neutral)
- ✨ **Offline Affirmations** based on detected emotion
- 🎧 **Music Recommendations** via YouTube links (no Spotify API needed)
- 📅 **Mood History Logging** in CSV
- 📊 **Mood Trend Visualization** using Matplotlib

---

## 🛠️ Tech Stack

| Tool          | Purpose                      |
|---------------|------------------------------|
| Streamlit     | Frontend Web App             |
| Transformers  | Emotion classification (BERT)|
| Torch         | Backend support for models   |
| Pandas        | Data storage + history       |
| Matplotlib    | Mood chart plotting          |

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/ai-mood-tracker.git
cd ai-mood-tracker
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run app.py ##

🧠 How it Works
User types how they feel, e.g., "I'm tired and frustrated today."

The app detects the emotion (angry)

It suggests:

🎧 A calming music playlist from YouTube

✨ A motivational affirmation

🧘 A helpful activity like a short walk or breathing exercise

It saves the entry to a CSV file with date + emotion

Displays a mood trend chart based on previous entries

#AIWellness #MentalHealthAI #Productivity #MoodTracker #Streamlit #NoAPI #GPTFree #BERT #SelfCare
