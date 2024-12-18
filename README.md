SoulScape: Mental Wellness Journal
Pulkit Pathak
Pulkit Pathak

9 min read
·
Just now





GitHub Link

Imagine an AI companion that not only listens to your thoughts but understands your emotions, guiding you towards activities tailored to uplift your mood. What if it also helped you track your mental health progress, offering a safe, interactive space for growth? Welcome to SOULSCAPE, a mental wellness journal that combines the power of Flask, Firebase, Gemini 2.0 Flash, and Google Cloud to redefine how we care for our mental well-being.

In this blog, you’ll learn how to:

How to build an intuitive chat interface powered by advanced AI.
Personalizing user experiences with mood-based activity mapping.
Leveraging Firebase for seamless progress tracking and reporting?.
How to deploy your application on Google Cloud for scalability and accessibility.
Whether you’re a budding developer or a seasoned programmer, SOULSCAPE is a project that will sharpen your technical skills and deepen your understanding of mental wellness through technology. Let’s dive in!


Overview
Problem Statement
Mental wellness is a critical yet often overlooked aspect of daily life. With the rising pressures of modern lifestyles, individuals struggle to manage stress, process emotions, and maintain their mental health. A personalized digital tool that fosters emotional interaction and offers mood-specific activities can bridge this gap and provide proactive mental health support.

Target Audience
Skill Level: Beginner to Intermediate developers with a foundational understanding of web development (HTML, CSS, JavaScript) and Python Flask.
Predefined Terms: Basic knowledge of APIs, AI tools like Gemini 2.0, Firebase Firestore database integration, and deployment platforms like Google Cloud.
Demographics: Students, developers, or enthusiasts interested in mental health applications, AI-powered interactions, and web-based solutions.
Goals
By the end of this blog, readers will:

Understand the importance of creating tools for mental wellness.
Develop a fully functional web application using Flask, HTML, CSS, and JavaScript.
Integrate Gemini 2.0 Flash for AI-driven emotional interactions.
Implement Firebase Firestore to track mental health progress and create personalized reports.
Deploy the application on Google Cloud Platform.
Have a blueprint for building scalable, interactive web applications for wellness or similar projects.
This comprehensive guide empowers readers to create impactful digital solutions addressing mental health challenges while enhancing their development skills.

High-Level Architecture of SOULSCAPE
Solution Design Overview
SOULSCAPE is designed as an interactive, AI-powered mental wellness web application. Its architecture ensures ease of use, real-time interaction, scalability, and personalized user experience. Below is a breakdown of the design choices and their rationale

Architecture Diagram

Core Components
Frontend (HTML, CSS, JavaScript)
Why: To create an intuitive and visually appealing user interface for seamless interaction.
Impact: Enhances usability with responsive design and user-friendly features like real-time chat and scrollable reports.
2. Backend (Flask)

Why: Flask is lightweight yet powerful, making it ideal for integrating APIs and handling server-side logic.
Impact: Simplifies API management, session handling, and seamless communication between the front end and backend.
3. Gemini 2.0 Flash (AI Emotional Interaction)

Why: Leverages advanced AI capabilities to detect moods from user input and provide meaningful responses.
Impact: Personalizes the experience, making it engaging and emotionally supportive.
4. Firebase Firestore

Why: Provides a scalable, NoSQL database to log user activities and generate progress reports.
Impact: Enables dynamic activity tracking and personalized data insights.
5. Google Cloud Platform (Deployment)

Why: Offers a secure, scalable hosting solution with minimal setup complexity.
Impact: Ensures high availability and reliability for users accessing the application.

Rationale Behind Design Choices
Modular Approach:
Each component is independent, making it easier to test, maintain, and scale.
AI-Powered Interaction:
Real-time emotional responses drive user engagement, making SOULSCAPE a practical tool for wellness.
Scalability:
The use of Firebase and GCP ensures the app can handle increasing user demand without performance issues.
Ease of Deployment:
By using GCP and a lightweight Flask server, deployment becomes seamless, allowing developers to focus on features rather than infrastructure.
Impact on Usability and Functionality
Personalization: Custom-tailored mood-based activities.
Engagement: Conversational AI keeps users engaged and connected.
Reliability: Scalable infrastructure ensures consistent user experience.
User-Centric: Clear and simple navigation caters to users with varying technical abilities.
Prerequisites
Additional Learning Resources
Python
Python for Beginners — Interactive tutorials for learning Python basics.
Official Python Documentation — Comprehensive guide to Python.
HTML, CSS, and JavaScript
HTML Tutorial — Learn HTML to build the structure of your web pages.
CSS Tutorial — Style your web application with CSS.
JavaScript Basics — Learn JS to add interactivity to your web app.
Flask
Flask Documentation — Official Flask tutorial for building web apps.
Flask for Beginners — A collection of practical tutorials for beginners.
Google Cloud Platform
GCP Basics — Learn the fundamentals of GCP.
Deploy Flask Apps on GCP — Guide to deploying Python apps.
Gemini 2.0 Flash Pro
Getting Started with Gemini — Official introduction to Google’s Gemini platform.
Integrating Gemini AI — Learn how to integrate Gemini AI in projects.
Firebase Firestore
Firebase Firestore Tutorial — Set up Firestore and create collections.
Firestore Crash Course — Quick beginner-friendly video.
Visual Studio Code
VS Code for Beginners — Get started with VS Code features and extensions.
Postman
Postman API Testing — Understand API testing and usage with Postman.
Assumed Prior Knowledge
Familiarity with Python programming, including modules, functions, and libraries.
Basic understanding of HTML, CSS, and JavaScript for web development.
Knowledge of Flask concepts like routes, templates, and API creation.
Understanding of cloud deployment using Google Cloud Platform.
Working knowledge of Firebase Firestore for creating and managing database collections and documents.
Step-by-Step Instructions to Build Your Mental Wellness Application
A. Set Up the Project Environment
Task: Prepare your development environment.

Install Python and Flask
Download and install Python.
Install Flask:
pip install flask
2. Create a Virtual Environment

Set up a virtual environment to manage dependencies:
python -m venv venv
source venv/bin/activate  # Use `venv\Scripts\activate` on Windows
3. Install Necessary Packages

Install additional dependencies:
pip install flask-cors firebase-admin requests
Troubleshooting Tip:
If the pip command fails, upgrade it with pip install --upgrade pip.

B. Configure Google Cloud and Firebase
Task: Connect your project to Google Cloud and Firebase Firestore.

Create a Google Cloud Project
Visit Google Cloud Console and create a new project named SOULSCAPE.
2. Enable APIs

Enable the Firestore API and the Gemini 2.0 Flash API for your project.
3. Set Up Firestore

Navigate to Firebase Console and add Firestore to your project.
Create a users collection with fields like name, email, mood, progress, etc.
4. Download Firebase Admin SDK

Add the Firebase Admin SDK to your Flask app for authentication and database interaction.
C. Build the Flask Backend
Task: Create RESTful endpoints to interact with your app’s components.

Initialize Flask App
Create a file named app.py:
from flask import Flask, request, jsonify 
import firebase_admin from firebase_admin 
import credentials, firestore  app = Flask(__name__)  
# Initialize Firebase 
cred = credentials.Certificate("path_to_service_account.json") f
irebase_admin.initialize_app(cred) db = firestore.client(
2. Create Routes

Example: Add a route to save user mood data.
@app.route('/save_mood', methods=['POST']) 
def save_mood():     
  data = request.json     
  doc_ref = db.collection('users').document(data['email'])     
  doc_ref.set({'mood': data['mood']}, merge=True)     
  return jsonify({'message': 'Mood saved successfully'})
3. Run the Flask Server

Start the server with:
python app.py
Troubleshooting Tip:
If you see an import error, ensure dependencies are installed and the SDK path is correct.

4. Design the Frontend Interface
Task: Build a responsive web interface using HTML, CSS, and JavaScript.

Create Basic Layout
Add the following to index.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mental Wellness Chat</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="chat-container">
        <header>
            <h1>SOULSCAPE</h1>
        </header>
        <div class="chat-box" id="chat-box">
            <!-- Messages will be dynamically inserted here -->
        </div>
        <div class="chat-input">
            <input type="text" id="user-input" placeholder="Type your message here...">
            <button id="send-btn">Send</button>
        </div>
        <button id="fetch-report-btn">View Activity Report</button>
    </div>

    <div id="activity-report">
        <button id="close-report-btn">Close</button>
        <h2>Activity Report</h2>
        <ul id="activity-list"></ul>
    </div>

    <script src="/static/js/chat.js"></script>
    <script>
        // JavaScript for fetching and displaying activity report
        document.getElementById('fetch-report-btn').addEventListener('click', () => {
            fetch('/fetch_activities')
                .then(response => response.json())
                .then(data => {
                    const reportDiv = document.getElementById('activity-report');
                    const activityList = document.getElementById('activity-list');
                    activityList.innerHTML = '';

                    data.activities.forEach(activity => {
                        const listItem = document.createElement('li');
                        listItem.textContent = `Activity: ${activity.activity}, Mood: ${activity.mood}, Timestamp: ${activity.timestamp}`;
                        activityList.appendChild(listItem);
                    });

                    reportDiv.style.display = 'block';
                })
                .catch(err => {
                    console.error('Error fetching activities:', err);
                });
        });

        // Close the activity report when the close button is clicked
        document.getElementById('close-report-btn').addEventListener('click', () => {
            const reportDiv = document.getElementById('activity-report');
            reportDiv.style.display = 'none'; // Hide the activity report
        });
    </script>
</body>
</html>
2. Add JavaScript Functionality

Create app.js to connect the frontend with the backend.
async function submitMood() {
    const mood = document.getElementById('user-input').value;
    const response = await fetch('/save_mood', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: 'test@example.com', mood }),
    });
    const data = await response.json();
    alert(data.message);
}
3. Style the Interface

Add a simple style in styles.css:
body {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #f0f8ff;
}
textarea {
    width: 80%;
    height: 100px;
    margin: 20px 0;
}
button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}
Troubleshooting Tip:
Check the browser console (F12) for errors if the functionality doesn’t work as expected.

5. Integrate Gemini 2.0 Flash Pro
Task: Use the AI model to analyze user mood and suggest activities.

Install and Configure Gemini SDK
Add Gemini SDK:
pip install gemini-sdk
2. Analyze Mood Data

Extend your Flask app to use Gemini:
from gemini_sdk import Gemini

@app.route('/analyze_mood', methods=['POST'])
def analyze_mood():
    data = request.json
    mood_analysis = Gemini.analyze(data['mood'])
    return jsonify(mood_analysis)
Troubleshooting Tip:
Ensure your Google Cloud project is linked to the correct billing account to use Gemini.
6. Deploy to Google Cloud
Task: Host the application on GCP for public access.

Prepare for Deployment
Create a requirements.txt file for your dependencies:
pip freeze > requirements.txt
Add a Procfile for deployment:
web: python app.py
2. Deploy on App Engine

Use Google App Engine for deployment:
gcloud app deploy
Result / Demo

Chat Interface of SoulScape

Mood Detection by Gemini 2.0 Flash

Mood Joy Activity Developed using Phaser JS

Fear Mood Activity Developed using Phaser JS

Anxiety Relief Activity

Activity Report FireBase Integration
Resources for Implementation
Flask and Python Development
Flask Documentation
Python Firestore SDK
Google Cloud Services
Google Cloud Console
Firebase Firestore Overview
Gemini AI API Reference
Frontend Development
Mozilla Developer Network (MDN) for HTML, CSS, and JavaScript.
Bootstrap for responsive UI design.
Ideas for Expanding the Project
Advanced Emotional Analysis
Incorporate natural language processing (NLP) models to detect complex emotions and tailor activities accordingly.
Use sentiment analysis for journaling features where users log daily reflections.
2. Activity Recommendation Engine

Expand the AI to recommend personalized mindfulness activities such as guided meditations, calming playlists, or breathing exercises.
Integrate APIs like Spotify for music or YouTube for video recommendations.
3. Gamification and Progress Tracking

Add a rewards system to gamify user interactions, encouraging regular app use.
Create dashboards that visualize mental health trends and achievements over time.
4. Mobile Application Integration

Convert the web app into a mobile app using frameworks like Flutter or React Native.
Implement push notifications for activity reminders or motivational quotes.
5. Community Building

Add a social feature to connect users anonymously to share experiences and support each other.
Host weekly challenges promoting mental wellness (e.g., a gratitude journal challenge).
Challenges to Hone Your Skills
Deploying on Other Platforms
Try deploying your app on platforms like AWS, Azure, or Heroku for cross-platform learning.
2. Real-Time Interactivity

Integrate WebSocket or MQTT protocols to provide real-time updates and interaction.
3. Data Privacy and Security

Implement end-to-end encryption for user data.
Add authentication systems using OAuth or Firebase Authentication.
4. Scalability and Performance Optimization

Improve database query efficiency and optimize API response times.
Use tools like Cloud Run or Kubernetes for load balancing and scalability.
5. AI Model Customization

Train your own AI models for specific mental health tasks using TensorFlow or PyTorch.
Fine-tune the existing Gemini model for niche use cases such as cognitive-behavioural therapy support.
By exploring these resources and challenges, you’ll deepen your understanding of AI, cloud services, and frontend-backend integration while creating meaningful tools for mental wellness. Let your curiosity drive you to innovate and expand on this project!

Call to action
To learn more about Google Cloud services and to create impact for the work you do, get around to these steps right away:

Register for Code Vipassana sessions
Join the meetup group Datapreneur Social
Sign up to become Google Cloud Innovator
Let’s Connect on Linkedin
