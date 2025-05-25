from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env variables into environment
load_dotenv()

# Now initialize client using the loaded key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_trending_prompt():
    print("⚙️ Calling OpenAI API...")  # For debug visibility
    system_prompt = (
        "You are an expert AI content strategist. Your job is to craft one short, attention-grabbing prompt "
        "idea for a LinkedIn post based on the latest Artificial Intelligence trends or news, tools, innovations, or breakthroughs. "
        "Keep the tone professional yet engaging, suitable for a startup founder or AI builder."
    )
    user_prompt = "Give me 1 original AI-related post idea for today’s trending topic."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=150,
            temperature=0.9,
            timeout=10  # Add timeout if you're using openai-python >=1.0
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        raise RuntimeError(f"Error generating trending prompt: {str(e)}")
