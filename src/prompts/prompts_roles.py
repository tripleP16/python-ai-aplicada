"""
    Roles en los prompts 
"""


from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def show_roles():
    """Funcion que muestra los roles"""

    print("="*50)
    print("Rol: User. (Sin system)")
    print("="*50)
    response_1 = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "¿Cuanto es 2 + 2"
            }
        ]
    )

    print(f"Respuesta del User: {response_1.choices[0].message.content}\n")


if __name__ == "__main__":
    show_roles()
