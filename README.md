MediBot 🏥🤖 - AI-Powered Medical Chatbot

📌 Overview
MediBot is an AI-powered chatbot designed to assist users with medical-related queries. It utilizes the Gemini API for natural language processing and is trained to respond exclusively to medical-related inquiries. The chatbot helps users understand symptoms, provides possible diagnoses, and suggests remedies, ensuring they receive helpful information while emphasizing the need for professional medical consultation.

🚀 Features
✔️ Accepts and processes medical-related queries only
✔️ Utilizes Gemini API for intelligent responses
✔️ Provides symptom analysis and possible health conditions
✔️ Suggests general remedies for minor health concerns
✔️ Displays a user-friendly chat interface for interaction
✔️ Built with Flask and integrated with a custom API key stored securely in .env

🛠 Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask Framework)
API Integration: Gemini API
Security: .env file for storing API keys

⚙️ Installation
Follow these steps to set up the project locally:

1️⃣ Clone the Repository

git clone https://github.com/TabrezShariff/MediBot.git
cd MediBot

2️⃣ Create a Virtual Environment (Recommended)

python -m venv env
source env/bin/activate   # MacOS/Linux  
env\Scripts\activate      # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Configure API Key
Create a .env file in the root directory
Add your Gemini API key as follows:

API_KEY="your_gemini_api_key_here"

5️⃣ Run the Application

python app.py

Open your browser and go to http://127.0.0.1:5000/

🤖 How It Works

User enters a medical-related query in the chatbot.
The chatbot processes the query and interacts with the Gemini API.
The response is analyzed and displayed in a conversational format.
If necessary, the chatbot provides symptom analysis and potential remedies.
The system strictly answers only medical-related questions to maintain focus and reliability.

📜 Disclaimer

MediBot is an AI-based assistant and should not be used as a substitute for professional medical advice. It is intended for informational purposes only. Always consult a licensed medical professional for serious health concerns.

💡 Future Enhancements

🔹 Enhance response accuracy with additional medical datasets
🔹 Improve UI with a more interactive chat experience
🔹 Integrate speech-to-text for voice-based queries
🔹 Implement real-time doctor consultation via chat/video
