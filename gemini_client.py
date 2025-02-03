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


# gemini_client.py
import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

# For latest SDK version (use this instead of system_instruction)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Add system instruction as first message
system_prompt = """You are a compassionate AI mental wellness companion. Guidelines:
- Provide empathetic, non-judgmental support
- Offer practical coping strategies
- Validate emotions
- Suggest professional help when appropriate"""

# Initialize with system prompt
chat.send_message(system_prompt)

def get_response(prompt):
    try:
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return "I'm having trouble responding right now. Could you rephrase that?"

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

# def get_response(chat_session, prompt):
#     try:
#         response = chat_session.send_message(prompt)
#         return response.text
#     except Exception as e:
#         print(f"Error with Gemini API: {e}")
#         return "I'm having trouble understanding. Can you try again?"
