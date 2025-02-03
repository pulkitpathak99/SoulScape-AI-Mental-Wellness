# gemini_client.py

import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
# Replace the config import with:
import os

# Update the configuration line to:
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

# Create and configure the model
generation_config = {
    "temperature": 1.5,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
}


model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    system_instruction="""
        You are a compassionate AI mental wellness companion.
        Your goal is to provide supportive, empathetic, and constructive responses.
        
        Guidelines:
        - Listen actively and validate the user's feelings
        - Offer gentle, evidence-based emotional support
        - Suggest practical coping strategies when appropriate
        - Maintain a warm, non-judgmental tone
        - If the message suggests serious mental health concerns, 
          recommend professional help gently
        
        Response Format:
        1. Acknowledge the emotion
        2. Provide supportive insight
        3. Optional: Offer a small, actionable suggestion
    """,
)

def start_chat_session(history=None):
    """Starts a new chat session with optional history."""
    if history is None:
        history = [
            {
                "role": "user",
                "parts": ["hello\n"],
            },
            {
                "role": "model",
                "parts": [
                    "Hello! It's good to connect with you. I'm here and ready to listen whenever you need an ear. How are you doing today?\n",
                ],
            },
        ]
    return model.start_chat(history=history)

def get_response(chat_session, prompt):
    try:
        response = chat_session.send_message(prompt)
        return response.text
    except Exception as e:
        print(f"Error with Gemini API: {e}")
        return "I'm having trouble understanding. Can you try again?"
