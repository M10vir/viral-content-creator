import openai
import os

# Load your OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_trending_prompt():
    """
    Calls GPT to generate a creative prompt idea based on current AI trends and innovation.
    Returns:
        str: A compelling AI-related prompt idea.
    """
    system_prompt = (
        "You are an expert AI content strategist. Your job is to craft one short, attention-grabbing prompt "
        "idea for a LinkedIn post based on the latest Artificial Intelligence trends or news, tools, innovations, or breakthroughs. "
       "Keep the tone professional yet engaging, suitable for a startup founder or AI builder."
    )

    user_prompt = "Give me 1 original AI-related post idea for today’s trending topic."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-3.5-turbo" if preferred
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=150
            temperature=0.9
        )
        ai_prompt = response["choices"][0]["message"]["content"].strip()
        return ai_prompt

    except Exception as e:
        raise RuntimeError(f"Error generating trending prompt: {str(e)}")
