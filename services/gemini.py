
from google import genai
from config import GOOGLE_API_KEY, GEMINI_MODEL

client = genai.Client(api_key=GOOGLE_API_KEY)


def generate_caption(product_name, price, category, platform, occasion, language="English"):
    """
    Generate social media caption using Gemini.

    Args:
        product_name (str): Name of the product
        price (str): Product price in INR
        category (str): Product category
        platform (str): Target platform e.g. Instagram
        occasion (str): Occasion context e.g. Diwali
        language (str): Output language — English or Hindi

    Returns:
        str: Generated caption with emojis and hashtags
    """


    prompt = f"""
    You are a social media expert for Indian small businesses.
    Generate a {platform} caption for the following product:
    
    Product: {product_name}
    Category: {category}
    Price: ₹{price}
    Occasion: {occasion}
    
    Requirements:
    - IMPORTANT: Write ONLY in English
    - Include relevant emojis
    - Add a clear call to action
    - Include 5 relevant hashtags at the end in English if the platform is instagram or facebook
    - Keep it short and punchy
    - Use complete meaningful sentences that sound natural
    - USe sentences that can be meaningfully translated to other languages without loosing its meaning
    
    Return only the caption, nothing else.
    """
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text