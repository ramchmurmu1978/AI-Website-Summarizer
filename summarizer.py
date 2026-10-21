import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("grok_api_key"),
    base_url="https://api.groq.com/openai/v1"
)

def summarize_text(text):
    prompt = f"""
Summarize the following webpage content.
****************************************
Create:
1. A short overview in 2-3 sentences.
2. 5 key points.
3. A one-sentence takeaway.

Keep the summary clear and easy to understand.

Webpage content:
{text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role" : "system",
                "content" : "You are an expert at summarizing web content accurately and clearly."
            },
            {
                "role" : "user",
                "content" : prompt
            }
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":

    sample_text = """
    Artificial Intellegence is a field of computer science focussed on 
    creating systems that can perform tasks that normally require human
    intelligence, such as learning, reasoning, and understanding language.
    """

    summary = summarize_text(sample_text)

    print("\n---Summary---\n")
    print(summary)