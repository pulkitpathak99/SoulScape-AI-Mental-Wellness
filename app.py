from flask import Flask, request, jsonify, render_template, redirect, url_for
from gemini_client import start_chat_session, get_response
from firebase_client import log_user_activity
from datetime import datetime

app = Flask(__name__)

# Initialize a global chat session
chat_session = start_chat_session()

# Define mood-to-activity mapping
MOOD_ACTIVITIES = {
    "Joy": "game_joy",
    "Anger": "breathing_anger",
    "Disgust": "relax_disgust",
    "Fear": "game_fear",
    "Sadness": "breathing_sadness",
    "Embarrassment": "game_embarrassment",
    "Anxiety": "game_anxiety"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reports")
def reports():
    return render_template("report.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    user_id = data.get("user_id", "default_user")  # Add user_id for tracking

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # Get AI response
    response_text = get_response(chat_session, user_input)

    # Mocked mood detection
    detected_mood = detect_mood(user_input)

    # Get the activity page for the mood
    activity = MOOD_ACTIVITIES.get(detected_mood, "default_activity")

    # Generate activity URL
    activity_url = url_for('activity', activity=activity)

    # Log the activity in Firebase
    timestamp = datetime.utcnow()
    log_user_activity(user_id, activity, detected_mood, timestamp)

    return jsonify({
        "response": response_text,
        "mood": detected_mood,
        "activity": activity,
        "activity_url": activity_url
    })

from flask import jsonify
from firebase_client import db

@app.route('/fetch_activities', methods=['GET'])
def fetch_activities():
    user_id = request.args.get('user_id', 'default_user')  # Replace with actual user ID logic
    try:
        activities_ref = db.collection('user_activities').document(user_id).collection('activities')
        activities = [doc.to_dict() for doc in activities_ref.stream()]
        return jsonify({"activities": activities})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

from textblob import TextBlob

def detect_mood(text):
    """
    Advanced mood detection with context, sarcasm consideration, and handling multi-emotions.
    """
    
    # Sentiment analysis with TextBlob to get polarity (positive/negative) and subjectivity (neutrality)
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity
    
    # Contextual mood detection based on keywords, sentiment, and subjectivity
    mood = []

    # Analyze common mood keywords (simple scenario)
    if "happy" in text or "joy" in text or "elated" in text:
        mood.append("Joy")
    if "angry" in text or "frustrated" in text or "irritated" in text:
        mood.append("Anger")
    if "disgusted" in text or "grossed out" in text:
        mood.append("Disgust")
    if "fear" in text or "scared" in text or "terrified" in text:
        mood.append("Fear")
    if "sad" in text or "unhappy" in text or "heartbroken" in text:
        mood.append("Sadness")
    if "embarrassed" in text or "ashamed" in text:
        mood.append("Embarrassment")
    if "anxious" in text or "nervous" in text or "uneasy" in text:
        mood.append("Anxiety")
    
    # Sentiment analysis influence (adjust mood if necessary based on sentiment polarity)
    if sentiment_polarity < -0.2:
        if not any(mood):  # No mood identified yet
            mood.append("Sadness")
        else:
            if "Joy" in mood:
                mood.remove("Joy")
                mood.append("Sadness")
            elif "Anger" in mood:
                mood.remove("Anger")
                mood.append("Sadness")
    
    elif sentiment_polarity > 0.2:
        if not any(mood):  # No mood identified yet
            mood.append("Joy")
    
    # Handling multi-emotion scenario by checking if more than one mood is present
    if len(mood) > 1:
        mood.append("Mixed emotions")

    # Handling sarcasm: simple rule-based for now (detects certain sentence structures)
    if "oh great" in text or "just what I needed" in text:
        if "Joy" in mood:
            mood.remove("Joy")
            mood.append("Sarcasm")

    # If no specific mood detected, return Neutral
    if not mood:
        return "Neutral"

    # Return the most relevant mood or moods
    return ", ".join(mood)

@app.route("/activity/<activity>")
def activity(activity):
    return render_template(f"{activity}.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

