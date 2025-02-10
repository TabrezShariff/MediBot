from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure Google Generative AI
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

# Medical context for the AI
MEDICAL_CONTEXT = """
You are MediBot, a medical assistant chatbot. Your role is to:
1. greet back user if they greet
2. Provide general health information and first-aid or self-treatment advice for common symptoms.
3. Suggest basic remedial measures for common symptoms.
4. Be empathetic, clear, and concise in your responses.
5. Focus on evidence-based information.
6. Never provide diagnoses, only general information.
7. if user thanks you responed them as well

Format your response EXACTLY as follows, with each section separated by two newlines:

1. [Condition]: Brief description (1-2 sentences)

2. Common causes:
Cause 1, 
Cause 2, 
Cause 3

3. Common symptoms:
Symptom 1, 
Symptom 2, 
Symptom 3

4. Basic treatment suggestions:
Suggestion 1, 
Suggestion 2, 
Suggestion 3

5. When to see a doctor:
Criteria 1, 
Criteria 2

Do not use any special characters or formatting other than numbers,and newlines as shown above.

Important: Always end responses with this medical Note, separated by two newlines:

Note: Provided response is for general information only and not a substitute for professional medical advice. Please consult a healthcare professional for proper diagnosis and treatment.
"""
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        # Prepare prompt with medical context
        prompt = f"{MEDICAL_CONTEXT}\nUser symptom: {user_message}\nProvide proper information."
        
        # Generate response
        response = model.generate_content(prompt)
        formatted_response = response.text.strip()

        return jsonify({
            'status': 'success',
            'response': formatted_response
        })
        
    except Exception as e:
        print(f"Error Occurred: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)