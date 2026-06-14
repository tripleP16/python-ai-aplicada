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

    print("="*50)
    print("Rol: System")
    print("="*50)

    response_2 = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """"
                Eres un matematico gruñon que contesta preguntas simples con desden 
                pero con una precision absoluta , y a las preguntas muy muy sencillas les incluyes un comentario
                digno del dr house 
                """
            },
            {
                "role": "user",
                "content": "¿Cuanto es 2 + 2"
            }
        ]
    )

    print(f"Respuesta del System: {response_2.choices[0].message.content}\n")


if __name__ == "__main__":
    show_roles()
