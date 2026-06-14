"""Librerias """


from openai import OpenAI, AuthenticationError, RateLimitError, APIConnectionError
from dotenv import load_dotenv

load_dotenv()


def call_ai(question: str) -> str:
    """Función que llama a la API de OpenAI"""

    client = OpenAI()
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens=500,
            temperature=1.6
        )
        return response.choices[0].message.content
    except AuthenticationError:
        print("Revisa tu api key")
        raise SystemExit(1)
    except RateLimitError:
        print("Limite de velocidad alcanzado")
        raise SystemExit(1)
    except APIConnectionError:
        print("Sin conexion a la api, checa el internet")
        raise SystemExit(1)
    except Exception as e:
        print(f"Error Inesperado: {type(e).__name__}")
        raise SystemExit(1)


if __name__ == "__main__":
    print(call_ai("Dame un titulo para un video de python"))
