import os
from dotenv import load_dotenv

load_dotenv()

#API keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

#Gemini model 
GEMINI_MODEL = "gemini-3.1-flash-lite"

# Sarvam model for Indian language translation
SARVAM_MODEL = "mayura:v1"

SARVAM_MODE = "modern-colloquial"

LANGUAGES = {
    "Hindi": "hi-IN",
    "Gujarati": "gu-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Marathi": "mr-IN",
    "Bengali": "bn-IN",
    "Kannada": "kn-IN",
    "Malayalam": "ml-IN",
    "Punjabi": "pa-IN",
    "Urdu": "ur-IN"
}

PLATFORMS = ["Instagram", "Facebook", "WhatsApp"]

OCCASIONS = [
    "Regular",
    "Diwali",
    "Eid",
    "Christmas",
    "Navratri",
    "Holi",
    "Independence Day",
    "New Year",
    "Weekend Sale"
    "Yearly sale"
]