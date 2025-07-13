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
