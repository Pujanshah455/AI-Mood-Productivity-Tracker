import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import re
from textblob import TextBlob
import altair as alt

# Page configuration
st.set_page_config(
    page_title="🧘 AI Mood & Productivity Tracker",
    page_icon="🧘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
    .mood-button {
        background: #667eea;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        margin: 0.2rem;
        cursor: pointer;
    }
    .affirmation-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        margin: 1rem 0;
    }
    .activity-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'mood_history' not in st.session_state:
    st.session_state.mood_history = []
if 'current_mood' not in st.session_state:
    st.session_state.current_mood = None
if 'affirmation_count' not in st.session_state:
    st.session_state.affirmation_count = 0

# Mood detection functions
def detect_mood_from_text(text):
    """Detect mood from text using keyword analysis and sentiment analysis"""
    text_lower = text.lower()
    
    # Mood keywords
    mood_keywords = {
        'happy': ['happy', 'joy', 'excited', 'great', 'amazing', 'wonderful', 'fantastic', 'good', 'positive', 'cheerful', 'delighted', 'pleased', 'content', 'satisfied', 'optimistic', 'thrilled', 'elated'],
        'sad': ['sad', 'down', 'depressed', 'upset', 'disappointed', 'hurt', 'cry', 'tears', 'blue', 'gloomy', 'melancholy', 'dejected', 'heartbroken', 'sorrowful', 'miserable', 'grief'],
        'anxious': ['anxious', 'worried', 'stress', 'nervous', 'panic', 'overwhelmed', 'tense', 'restless', 'uneasy', 'concerned', 'fearful', 'apprehensive', 'jittery', 'stressed', 'frantic'],
        'angry': ['angry', 'mad', 'frustrated', 'annoyed', 'irritated', 'furious', 'rage', 'pissed', 'upset', 'bothered', 'livid', 'enraged', 'irate', 'outraged'],
        'calm': ['calm', 'peaceful', 'relaxed', 'serene', 'tranquil', 'composed', 'centered', 'balanced', 'quiet', 'still', 'zen', 'mindful', 'meditative'],
        'energetic': ['energetic', 'motivated', 'pumped', 'active', 'dynamic', 'vigorous', 'lively', 'spirited', 'enthusiastic', 'driven', 'focused', 'productive'],
        'tired': ['tired', 'exhausted', 'drained', 'weary', 'fatigued', 'sleepy', 'burnt', 'worn', 'depleted', 'lethargic', 'sluggish']
    }
    
    # Count keyword matches
    mood_scores = {}
    for mood, keywords in mood_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        mood_scores[mood] = score
    
    # Get TextBlob sentiment
    blob = TextBlob(text)
    sentiment = blob.sentiment
    
    # Combine keyword and sentiment analysis
    if sentiment.polarity > 0.3:
        mood_scores['happy'] += 2
    elif sentiment.polarity < -0.3:
        mood_scores['sad'] += 2
    
    if sentiment.subjectivity > 0.7:
        mood_scores['anxious'] += 1
    
    # Return the mood with highest score
    if max(mood_scores.values()) > 0:
        return max(mood_scores, key=mood_scores.get)
    else:
        # Default based on sentiment polarity
        if sentiment.polarity > 0.1:
            return 'happy'
        elif sentiment.polarity < -0.1:
            return 'sad'
        else:
            return 'calm'

def get_mood_emoji(mood):
    """Get emoji for mood"""
    mood_emojis = {
        'happy': '😊',
        'sad': '😢',
        'anxious': '😰',
        'angry': '😠',
        'calm': '😌',
        'energetic': '⚡',
        'tired': '😴'
    }
    return mood_emojis.get(mood, '🙂')

def get_mood_color(mood):
    """Get color for mood"""
    mood_colors = {
        'happy': '#FFD700',
        'sad': '#4169E1',
        'anxious': '#FF6347',
        'angry': '#DC143C',
        'calm': '#90EE90',
        'energetic': '#FF69B4',
        'tired': '#9370DB'
    }
    return mood_colors.get(mood, '#808080')

# Recommendation functions
def get_affirmations(mood):
    """Get mood-specific affirmations"""
    affirmations = {
        'happy': [
            "I am radiating joy and positivity today!",
            "My happiness is contagious and brightens others' days.",
            "I choose to see the good in every situation.",
            "I am grateful for this moment of joy.",
            "My positive energy creates wonderful opportunities."
        ],
        'sad': [
            "This feeling is temporary, and I will get through this.",
            "I am allowed to feel my emotions and process them healthily.",
            "I am stronger than I know and more resilient than I feel.",
            "Tomorrow brings new possibilities and hope.",
            "I am worthy of love and compassion, especially from myself."
        ],
        'anxious': [
            "I am safe in this moment and can handle whatever comes.",
            "I breathe deeply and release all tension from my body.",
            "I trust in my ability to navigate challenges.",
            "I am in control of my thoughts and choose peace.",
            "This anxiety will pass, and I am stronger than my fears."
        ],
        'angry': [
            "I acknowledge my anger and choose to respond with wisdom.",
            "I release this anger and choose peace over conflict.",
            "I am in control of my reactions and choose kindness.",
            "My anger is valid, but I choose healthy ways to express it.",
            "I forgive others and myself, freeing my heart from resentment."
        ],
        'calm': [
            "I am present, centered, and at peace with myself.",
            "My calm energy creates harmony in my environment.",
            "I trust in the natural flow of life.",
            "I am grounded and connected to my inner wisdom.",
            "Peace flows through me like a gentle river."
        ],
        'energetic': [
            "I channel my energy into positive and productive actions.",
            "My enthusiasm inspires others and creates positive change.",
            "I am focused and ready to tackle any challenge.",
            "My energy is a gift that I use to serve my highest purpose.",
            "I am unstoppable when I align my energy with my goals."
        ],
        'tired': [
            "I give myself permission to rest and recharge.",
            "My body and mind deserve care and restoration.",
            "Rest is productive and necessary for my well-being.",
            "I honor my need for sleep and relaxation.",
            "Tomorrow I will feel refreshed and renewed."
        ]
    }
    return random.choice(affirmations.get(mood, affirmations['calm']))

def get_activities(mood):
    """Get mood-specific activities"""
    activities = {
        'happy': [
            "🎨 Creative Expression: Paint, draw, or write in a journal",
            "🤝 Social Connection: Call a friend or family member",
            "🎵 Music & Dance: Put on your favorite songs and dance",
            "🌱 Spread Joy: Do something kind for someone else",
            "📸 Capture Memories: Take photos of things that make you smile"
        ],
        'sad': [
            "🛁 Self-Care: Take a warm bath or shower",
            "📚 Gentle Reading: Read something comforting or inspirational",
            "🍵 Mindful Tea: Brew your favorite tea and savor it slowly",
            "🌳 Nature Walk: Take a gentle walk outside",
            "💭 Journaling: Write down your thoughts and feelings"
        ],
        'anxious': [
            "🧘 Deep Breathing: Practice 4-7-8 breathing technique",
            "🏃 Light Exercise: Go for a walk or do gentle yoga",
            "🎵 Calming Music: Listen to relaxing or meditative music",
            "📱 Mindfulness App: Use a guided meditation app",
            "🧩 Focus Activity: Do a puzzle or organized activity"
        ],
        'angry': [
            "🥊 Physical Release: Go for a run or do intense exercise",
            "📝 Anger Journal: Write down what's bothering you",
            "🧘 Meditation: Practice loving-kindness meditation",
            "🎵 Music Therapy: Listen to music that matches then soothes your mood",
            "🗣️ Talk it Out: Call a trusted friend or counselor"
        ],
        'calm': [
            "📖 Mindful Reading: Read something that interests you",
            "🌅 Gratitude Practice: Write down 3 things you're grateful for",
            "🎨 Creative Flow: Engage in art, music, or writing",
            "🌿 Nature Connection: Spend time in nature or tend to plants",
            "🧘 Meditation: Practice mindfulness or loving-kindness meditation"
        ],
        'energetic': [
            "🎯 Goal Setting: Plan and work on important projects",
            "🏃 Exercise: Go for a run, bike ride, or gym workout",
            "🧹 Productive Tasks: Organize, clean, or tackle your to-do list",
            "💡 Learning: Take on a new skill or educational challenge",
            "🤝 Social Activities: Meet friends for active pursuits"
        ],
        'tired': [
            "😴 Quality Rest: Take a 20-minute power nap",
            "🛁 Relaxation: Take a warm bath with calming scents",
            "📚 Light Reading: Read something easy and enjoyable",
            "🍵 Herbal Tea: Drink chamomile or other calming teas",
            "🧘 Gentle Stretching: Do light yoga or stretching exercises"
        ]
    }
    return activities.get(mood, activities['calm'])

def get_music_recommendations(mood):
    """Get mood-specific music recommendations with playable links"""
    music = {
        'happy': [
            {
                'title': "Happy - Pharrell Williams",
                'url': "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
                'audio': "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
                'description': "🎵 Upbeat and joyful"
            },
            {
                'title': "Can't Stop the Feeling - Justin Timberlake", 
                'url': "https://www.youtube.com/watch?v=ru0K8uYEZWw",
                'audio': "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
                'description': "🎶 Feel-good pop anthem"
            },
            {
                'title': "Uptown Funk - Mark Ronson ft. Bruno Mars",
                'url': "https://www.youtube.com/watch?v=OPf0YbXqDm0", 
                'audio': "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
                'description': "🎸 Funky and energetic"
            }
        ],
        'sad': [
            {
                'title': "Someone Like You - Adele",
                'url': "https://www.youtube.com/watch?v=hLQl3WQQoQ0",
                'audio': "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
                'description': "🎵 Emotional ballad"
            },
            {
                'title': "Mad World - Gary Jules",
                'url': "https://www.youtube.com/watch?v=4N3N1MlvVc4",
                'audio': "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav", 
                'description': "🎶 Melancholic and introspective"
            },
            {
                'title': "Hurt - Johnny Cash",
                'url': "https://www.youtube.com/watch?v=8AHCfZTRGiI",
                'audio': "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
                'description': "🎸 Deep and moving"
            }
        ],
        'anxious': [
            {
                'title': "Weightless - Marconi Union",
                'url': "https://www.youtube.com/watch?v=UfcAVejslrU",
                'audio': "https://www.soundjay.com/nature/sounds/rain-03.wav",
                'description': "🎵 Scientifically proven to reduce anxiety"
            },
            {
                'title': "Clair de Lune - Debussy",
                'url': "https://www.youtube.com/watch?v=CvFH_6DNRCY",
                'audio': "https://www.soundjay.com/nature/sounds/rain-03.wav",
                'description': "🎶 Calming classical piece"
            },
            {
                'title': "Rain Sounds for Sleep",
                'url': "https://www.youtube.com/watch?v=mPZkdNFkNps",
                'audio': "https://www.soundjay.com/nature/sounds/rain-03.wav",
                'description': "🌊 Nature sounds for relaxation"
            }
        ],
        'angry': [
            {
                'title': "Break Stuff - Limp Bizkit",
                'url': "https://www.youtube.com/watch?v=ZpUYjpKg9KY",
                'audio': "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
                'description': "🎵 High-energy rock for release"
            },
            {
                'title': "Killing in the Name - Rage Against the Machine",
                'url': "https://www.youtube.com/watch?v=bWXazVhlyxQ",
                'audio': "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
                'description': "🎶 Intense and powerful"
            },
            {
                'title': "Lose Yourself - Eminem",
                'url': "https://www.youtube.com/watch?v=_Yhyp-_hX2s",
                'audio': "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
                'description': "🎤 Channeling anger into motivation"
            }
        ],
        'calm': [
            {
                'title': "Gymnopédie No. 1 - Erik Satie",
                'url': "https://www.youtube.com/watch?v=S-Xm7s9eGM4",
                'audio': "https://www.soundjay.com/nature/sounds/ocean-wave-1.wav",
                'description': "🎵 Peaceful and meditative"
            },
            {
                'title': "Spiegel im Spiegel - Arvo Pärt",
                'url': "https://www.youtube.com/watch?v=TJ6Mzvh3XCc",
                'audio': "https://www.soundjay.com/nature/sounds/ocean-wave-1.wav",
                'description': "🎶 Minimalist and serene"
            },
            {
                'title': "Ocean Waves - Nature Sounds",
                'url': "https://www.youtube.com/watch?v=WHPEKLQID4U",
                'audio': "https://www.soundjay.com/nature/sounds/ocean-wave-1.wav",
                'description': "🌊 Soothing ocean sounds"
            }
        ],
        'energetic': [
            {
                'title': "Thunderstruck - AC/DC",
                'url': "https://www.youtube.com/watch?v=v2AC41dglnM",
                'audio': "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
                'description': "🎵 High-energy rock anthem"
            },
            {
                'title': "Pump It - Black Eyed Peas",
                'url': "https://www.youtube.com/watch?v=ZaI2IlHwmgQ",
                'audio': "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
                'description': "🎶 Motivational and upbeat"
            },
            {
                'title': "Levels - Avicii",
                'url': "https://www.youtube.com/watch?v=_ovdm2yX4MA",
                'audio': "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav",
                'description': "🎸 Electronic dance energy"
            }
        ],
        'tired': [
            {
                'title': "Sleep Baby Sleep - Broods",
                'url': "https://www.youtube.com/watch?v=0wf-RHgP1k0",
                'audio': "https://www.soundjay.com/nature/sounds/rain-03.wav",
                'description': "🎵 Gentle and soothing"
            },
            {
                'title': "Nocturne in E-flat major - Chopin",
                'url': "https://www.youtube.com/watch?v=9E6b3swbnWg",
                'audio': "https://www.soundjay.com/nature/sounds/rain-03.wav",
                'description': "🎶 Relaxing classical"
            },
            {
                'title': "Sleepyhead - Passion Pit",
                'url': "https://www.youtube.com/watch?v=5bfseWNmlds",
                'audio': "https://www.soundjay.com/nature/sounds/rain-03.wav",
                'description': "🎹 Dreamy and soft"
            }
        ]
    }
    return music.get(mood, music['calm'])

# Main app
def main():
    # Header
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.markdown("# 🧘 AI Mood & Productivity Tracker")
    st.markdown("### Your AI-powered wellness companion for mental health and productivity")
    st.markdown('</div>', unsafe_allow_html=True)

    # Sidebar
    st.sidebar.markdown("## 🎯 Navigation")
    page = st.sidebar.selectbox("Choose a section:", 
        ["🏠 Mood Check-in", "📊 Mood Analytics", "💡 Recommendations", "📚 Wellness Library"])

    if page == "🏠 Mood Check-in":
        mood_checkin()
    elif page == "📊 Mood Analytics":
        mood_analytics()
    elif page == "💡 Recommendations":
        recommendations_page()
    elif page == "📚 Wellness Library":
        wellness_library()

def mood_checkin():
    st.header("🌟 How are you feeling today?")
    
    # Quick mood buttons
    st.subheader("Quick Mood Selection:")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("😊 Happy"):
            st.session_state.current_mood = 'happy'
    with col2:
        if st.button("😢 Sad"):
            st.session_state.current_mood = 'sad'
    with col3:
        if st.button("😰 Anxious"):
            st.session_state.current_mood = 'anxious'
    with col4:
        if st.button("😠 Angry"):
            st.session_state.current_mood = 'angry'
    
    col5, col6, col7 = st.columns(3)
    with col5:
        if st.button("😌 Calm"):
            st.session_state.current_mood = 'calm'
    with col6:
        if st.button("⚡ Energetic"):
            st.session_state.current_mood = 'energetic'
    with col7:
        if st.button("😴 Tired"):
            st.session_state.current_mood = 'tired'

    st.markdown("---")
    
    # Text input for mood detection
    st.subheader("💭 Tell me about your day:")
    mood_text = st.text_area("How are you feeling? What's on your mind?", height=100)
    
    if st.button("🔍 Analyze My Mood"):
        if mood_text.strip():
            detected_mood = detect_mood_from_text(mood_text)
            st.session_state.current_mood = detected_mood
            
            # Save to history
            mood_entry = {
                'timestamp': datetime.now(),
                'mood': detected_mood,
                'text': mood_text,
                'emoji': get_mood_emoji(detected_mood)
            }
            st.session_state.mood_history.append(mood_entry)
            
            st.success(f"Mood detected: {get_mood_emoji(detected_mood)} {detected_mood.title()}")
        else:
            st.warning("Please enter some text to analyze your mood!")
    
    # Display current mood
    if st.session_state.current_mood:
        mood = st.session_state.current_mood
        emoji = get_mood_emoji(mood)
        color = get_mood_color(mood)
        
        st.markdown(f"""
        <div style="background-color: {color}; padding: 2rem; border-radius: 10px; text-align: center; margin: 2rem 0;">
            <h2 style="color: white; margin: 0;">Current Mood: {emoji} {mood.title()}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Get and display affirmation
        affirmation = get_affirmations(mood)
        st.markdown(f"""
        <div class="affirmation-box">
            <h3>🌟 Your Personal Affirmation:</h3>
            <p>"{affirmation}"</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 New Affirmation"):
            st.rerun()

def mood_analytics():
    st.header("📊 Mood Analytics & Insights")
    
    if not st.session_state.mood_history:
        st.info("No mood data yet. Start by checking in with your mood!")
        return
    
    # Convert to DataFrame
    df = pd.DataFrame(st.session_state.mood_history)
    df['date'] = df['timestamp'].dt.date
    df['hour'] = df['timestamp'].dt.hour
    
    # Mood distribution
    st.subheader("📈 Mood Distribution")
    mood_counts = df['mood'].value_counts()
    
    fig = px.pie(values=mood_counts.values, names=mood_counts.index, 
                 title="Overall Mood Distribution")
    st.plotly_chart(fig, use_container_width=True)
    
    # Mood over time
    st.subheader("📅 Mood Timeline")
    daily_mood = df.groupby(['date', 'mood']).size().reset_index(name='count')
    
    fig = px.line(daily_mood, x='date', y='count', color='mood',
                  title="Mood Trends Over Time")
    st.plotly_chart(fig, use_container_width=True)
    
    # Mood by time of day
    st.subheader("🕐 Mood by Time of Day")
    hourly_mood = df.groupby(['hour', 'mood']).size().reset_index(name='count')
    
    fig = px.bar(hourly_mood, x='hour', y='count', color='mood',
                 title="Mood Patterns by Hour")
    st.plotly_chart(fig, use_container_width=True)
    
    # Recent mood entries
    st.subheader("📝 Recent Mood Entries")
    recent_entries = df.tail(10).sort_values('timestamp', ascending=False)
    
    for _, entry in recent_entries.iterrows():
        st.markdown(f"""
        <div class="activity-card">
            <strong>{entry['emoji']} {entry['mood'].title()}</strong> - {entry['timestamp'].strftime('%Y-%m-%d %H:%M')}
            <br><em>"{entry['text'][:100]}..."</em>
        </div>
        """, unsafe_allow_html=True)

def recommendations_page():
    st.header("💡 Personalized Recommendations")
    
    if not st.session_state.current_mood:
        st.info("Please check in with your mood first to get personalized recommendations!")
        return
    
    mood = st.session_state.current_mood
    emoji = get_mood_emoji(mood)
    
    st.markdown(f"## Recommendations for your {emoji} {mood.title()} mood")
    
    # Tabs for different recommendation types
    tab1, tab2, tab3 = st.tabs(["🎯 Activities", "🎵 Music", "🌟 Affirmations"])
    
    with tab1:
        st.subheader("🎯 Recommended Activities")
        activities = get_activities(mood)
        for activity in activities:
            st.markdown(f"""
            <div class="activity-card">
                {activity}
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.subheader("🎵 Music Recommendations")
        music = get_music_recommendations(mood)
        
        # Add music player functionality
        st.markdown("### 🎧 Click to play music:")
        
        for i, song in enumerate(music):
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.markdown(f"""
                <div class="activity-card">
                    <strong>{song['title']}</strong><br>
                    <em>{song['description']}</em>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                # Audio player for sample sounds
                if song['audio']:
                    st.audio(song['audio'], format='audio/wav')
            
            with col3:
                # YouTube link button
                st.markdown(f"""
                <a href="{song['url']}" target="_blank">
                    <button style="background: #FF0000; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">
                        ▶️ YouTube
                    </button>
                </a>
                """, unsafe_allow_html=True)
        
        # Add embedded music player option
        st.markdown("---")
        st.subheader("🎼 Embedded Music Player")
        
        # Create a simple music player with pre-selected tracks
        selected_song = st.selectbox(
            "Choose a song to play:",
            options=[song['title'] for song in music],
            key="music_selector"
        )
        
        if selected_song:
            selected_track = next(song for song in music if song['title'] == selected_song)
            
            # Show YouTube embed (Note: This requires the video to allow embedding)
            st.markdown("### 🎵 Now Playing:")
            video_id = selected_track['url'].split('v=')[1].split('&')[0]
            
            # YouTube embed
            st.markdown(f"""
            <iframe width="100%" height="315" 
                    src="https://www.youtube.com/embed/{video_id}" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen>
            </iframe>
            """, unsafe_allow_html=True)
        
        # Add nature sounds and ambient music
        st.markdown("---")
        st.subheader("🌿 Nature Sounds & Ambient Music")
        
        ambient_sounds = {
            "🌧️ Rain": "https://www.soundjay.com/nature/sounds/rain-03.wav",
            "🌊 Ocean Waves": "https://www.soundjay.com/nature/sounds/ocean-wave-1.wav", 
            "🐦 Birds": "https://www.soundjay.com/nature/sounds/bird-2.wav",
            "🔥 Fireplace": "https://www.soundjay.com/nature/sounds/rain-03.wav"
        }
        
        cols = st.columns(len(ambient_sounds))
        for i, (sound_name, sound_url) in enumerate(ambient_sounds.items()):
            with cols[i]:
                st.markdown(f"**{sound_name}**")
                st.audio(sound_url, format='audio/wav')
    
    with tab3:
        st.subheader("🌟 Affirmations")
        if st.button("🔄 Generate New Affirmation"):
            st.session_state.affirmation_count += 1
        
        affirmation = get_affirmations(mood)
        st.markdown(f"""
        <div class="affirmation-box">
            <h3>Your Affirmation:</h3>
            <p>"{affirmation}"</p>
        </div>
        """, unsafe_allow_html=True)

def wellness_library():
    st.header("📚 Wellness Library")
    
    # Wellness tips and resources
    st.subheader("🧘 Mindfulness & Meditation")
    st.markdown("""
    <div class="activity-card">
        <h4>🎯 4-7-8 Breathing Technique</h4>
        <p>1. Inhale for 4 counts<br>
        2. Hold for 7 counts<br>
        3. Exhale for 8 counts<br>
        4. Repeat 3-4 times</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="activity-card">
        <h4>🌟 5-4-3-2-1 Grounding Technique</h4>
        <p>Notice:<br>
        5 things you can see<br>
        4 things you can touch<br>
        3 things you can hear<br>
        2 things you can smell<br>
        1 thing you can taste</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("💡 Productivity Tips")
    st.markdown("""
    <div class="activity-card">
        <h4>🍅 Pomodoro Technique</h4>
        <p>Work for 25 minutes, then take a 5-minute break. After 4 cycles, take a longer 15-30 minute break.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="activity-card">
        <h4>📝 Daily Planning</h4>
        <p>Each morning, write down 3 important tasks for the day. Focus on completing these before moving to other activities.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🌱 Self-Care Practices")
    st.markdown("""
    <div class="activity-card">
        <h4>💧 Hydration Reminder</h4>
        <p>Drink water regularly throughout the day. Aim for 8 glasses or more, and notice how hydration affects your mood and energy.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="activity-card">
        <h4>🌙 Sleep Hygiene</h4>
        <p>Maintain a consistent sleep schedule, avoid screens 1 hour before bed, and create a calm bedtime routine.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()