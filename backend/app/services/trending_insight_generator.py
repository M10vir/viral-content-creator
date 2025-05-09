# backend/app/services/trending_insight_generator.py

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_trending_ai_insight():
    prompt = """
You are an AI-powered content strategist. Create a research-driven, high-engagement LinkedIn-style viral AI insight post tailored for professionals in Qatar.

Requirements:
1. 📍 Focus on 2024–2025 AI breakthroughs and authoritative news from:
   - OpenAI (GPT-4o, Sora)
   - Microsoft Azure AI (Copilot, Responsible AI)
   - Google I/O 2024 (Gemini, Imagen)
   - AWS AI (Bedrock, Titan)
   - RSAC 2024 (AI security insights)
   - Qatar Foundation, QCRI, QSTP, MCIT AI Partnerships
   - Arabic Language Processing, AI in healthcare, transport, smart city

2. 🔍 Mention and hyperlink at least 3 authoritative sources

3. 🇶🇦 Highlight Qatar-based AI developments and initiatives

4. 💬 Include an engaging discussion prompt for LinkedIn

5. 🧠 Write in an insightful, concise, engaging tone with bullet points, emojis, line breaks

Format your response as:
{
  "formatted_post": "<Formatted viral post with emojis, breaks, hashtags>",
  "sources": ["<source 1>", "<source 2>", "<source 3>"]
}
""".strip()

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a content creator and AI strategist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1100
        )
        return response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"Error generating AI insight with sources: {str(e)}")
