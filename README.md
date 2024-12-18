# SOULSCAPE: Mental Wellness Journal

Welcome to **SOULSCAPE**, a mental wellness journal that redefines how we care for our mental well-being. This AI-powered application listens to your thoughts, understands your emotions, and guides you towards mood-specific activities, all while helping you track your mental health progress in a secure and interactive environment.

---

## Features

- **AI-Powered Chat Interface**: Advanced AI enables real-time emotional interactions.
- **Mood-Based Activities**: Personalized suggestions to uplift your mood.
- **Progress Tracking**: Seamless tracking of mental health progress using Firebase Firestore.
- **Cloud Deployment**: Scalable, accessible, and reliable hosting via Google Cloud.

---

## Overview

### Problem Statement
Mental wellness is a critical yet often overlooked aspect of daily life. Modern lifestyles often lead to stress, emotional struggles, and neglect of mental health. SOULSCAPE bridges this gap with a personalized digital tool to foster emotional interactions and offer proactive mental health support.

### Target Audience
- **Skill Level**: Beginner to Intermediate developers with a foundational understanding of web development (HTML, CSS, JavaScript) and Python Flask.
- **Demographics**: Students, developers, or enthusiasts interested in mental health applications, AI interactions, and web-based solutions.

---

## Goals
By the end of this project, you will:

- Build a web application using Flask, HTML, CSS, and JavaScript.
- Integrate AI-driven emotional interactions with Gemini 2.0 Flash.
- Implement Firebase Firestore to track mental health progress.
- Deploy the application on Google Cloud Platform.
- Understand how to create scalable, impactful digital wellness solutions.

---

## Architecture

### High-Level Architecture of SOULSCAPE
SOULSCAPE's design ensures ease of use, real-time interaction, scalability, and personalized user experiences.

#### Core Components

1. **Frontend (HTML, CSS, JavaScript)**
   - **Why**: For an intuitive and visually appealing user interface.
   - **Impact**: Enhances usability with responsive design and user-friendly features.

2. **Backend (Flask)**
   - **Why**: Lightweight yet powerful for API integration and server-side logic.
   - **Impact**: Simplifies API management and communication between components.

3. **Gemini 2.0 Flash (AI Emotional Interaction)**
   - **Why**: Detects moods from user input to provide meaningful responses.
   - **Impact**: Engages users with personalized emotional interactions.

4. **Firebase Firestore**
   - **Why**: Scalable NoSQL database for logging user activities and generating reports.
   - **Impact**: Enables dynamic activity tracking and personalized data insights.

5. **Google Cloud Platform (Deployment)**
   - **Why**: Secure, scalable hosting solution.
   - **Impact**: Ensures high availability and reliability.

---

## Prerequisites

### Assumed Prior Knowledge
- Python programming (modules, functions, libraries).
- Web development basics (HTML, CSS, JavaScript).
- Flask concepts (routes, templates, APIs).
- Cloud deployment using Google Cloud Platform.
- Firebase Firestore basics (creating collections and managing data).

### Additional Learning Resources
- **Python**: [Python for Beginners](https://docs.python.org/3/tutorial/)
- **Flask**: [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- **Google Cloud**: [GCP Basics](https://cloud.google.com/docs)
- **Firebase**: [Firestore Tutorial](https://firebase.google.com/docs/firestore)
- **Gemini 2.0 Flash**: [Gemini Documentation](https://cloud.google.com/ai/)

---

## Step-by-Step Guide

### A. Set Up the Project Environment

1. **Install Python and Flask**
   ```bash
   pip install flask
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install flask-cors firebase-admin requests
   ```

### B. Configure Google Cloud and Firebase

1. **Create a Google Cloud Project**
   - Visit [Google Cloud Console](https://console.cloud.google.com) and create a project named SOULSCAPE.

2. **Enable APIs**
   - Enable the Firestore API and Gemini 2.0 Flash API.

3. **Set Up Firestore**
   - Add Firestore to your Firebase project and create a `users` collection with fields such as `name`, `email`, `mood`, and `progress`.

4. **Download Firebase Admin SDK**
   - Use the SDK for authentication and database interaction.

### C. Build the Flask Backend

1. **Initialize Flask App**
   ```python
   from flask import Flask, request, jsonify
   import firebase_admin
   from firebase_admin import credentials, firestore

   app = Flask(__name__)
   
   # Initialize Firebase
   cred = credentials.Certificate("path_to_service_account.json")
   firebase_admin.initialize_app(cred)
   db = firestore.client()
   ```

2. **Create Routes**
   Example: Save user mood data.
   ```python
   @app.route('/save_mood', methods=['POST'])
   def save_mood():
       data = request.json
       doc_ref = db.collection('users').document(data['email'])
       doc_ref.set({'mood': data['mood']}, merge=True)
       return jsonify({'message': 'Mood saved successfully'})
   ```

3. **Run the Flask Server**
   ```bash
   python app.py
   ```

### D. Design the Frontend Interface

1. **Basic Layout**
   Create an `index.html` with a chat interface.

2. **JavaScript Functionality**
   Create a `chat.js` file to handle frontend-backend communication.

3. **Style the Interface**
   Use a `style.css` file for responsive and appealing design.

### E. Integrate Gemini 2.0 Flash

1. **Install Gemini SDK**
   ```bash
   pip install gemini-sdk
   ```

2. **Analyze Mood Data**
   Extend your Flask app to use Gemini:
   ```python
   from gemini_sdk import Gemini

   @app.route('/analyze_mood', methods=['POST'])
   def analyze_mood():
       data = request.json
       mood_analysis = Gemini.analyze(data['mood'])
       return jsonify(mood_analysis)
   ```

### F. Deploy to Google Cloud

1. **Prepare for Deployment**
   Create a `requirements.txt` file:
   ```bash
   pip freeze > requirements.txt
   ```
   Add a `Procfile` for deployment:
   ```
   web: python app.py
   ```

2. **Deploy on App Engine**
   ```bash
   gcloud app deploy
   ```

---

## Ideas for Expansion

1. **Advanced Emotional Analysis**: Incorporate NLP models for complex emotion detection.
2. **Activity Recommendation**: Suggest mindfulness activities via APIs like Spotify or YouTube.
3. **Gamification**: Add a rewards system to encourage regular use.
4. **Mobile Integration**: Convert the app into a mobile app using Flutter or React Native.
5. **Community Building**: Enable anonymous social features for user interaction.

---

## Call to Action
To explore Google Cloud services and create impactful projects:

- Register for Code Vipassana sessions.
- Join the Datapreneur Social Meetup group.
- Sign up to become a Google Cloud Innovator.

[Let's Connect on LinkedIn!](https://linkedin.com/pulkit-pathak)
