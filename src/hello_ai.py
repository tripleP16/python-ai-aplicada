""" Import libraties """

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user",
            "content": "Di hello world en tres idiomas (ch, en, fr)"}
    ]
)


text = response.choices[0].message.content

print(text)


print("\n--Uso de tokens--\n")
print(f"Tokens de Input: {response.usage.prompt_tokens}")
print(f"Tokens de Output: {response.usage.completion_tokens}")
print(f"Tokens totales: {response.usage.total_tokens}")


cost_input = (response.usage.prompt_tokens / 1_000_000) * 0.15
cost_output = (response.usage.completion_tokens / 1_000_000) * 0.60
cost_total = cost_input + cost_output

print(f"\n--Costos--\n")
print(f"Costo Input: {cost_input} USD")
print(f"Costo Output: {cost_output} USD")
print(f"Costo Total: {cost_total} USD")
