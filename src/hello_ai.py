""" Import libraties """

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Di hello world en tres idiomas (ch, en, fr)"}
    ]
)


text = response.choices[0].message.content

print(text)
