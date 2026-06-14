"""
Proyecto: CLI Chatbot
"""
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Configuracion
MODEL = "gpt-4o-mini"

SYSTEM_PROMPT = """Eres un asistente técnico experto en Python e IA.
Eres directo, usas ejemplos de código cuando es relevante,
y respondes en el mismo idioma que el usuario.
Si no sabes algo, lo dices honestamente."""

# Costos de la API en USD
INPUT_COSTS = 0.15
OUTPUT_COSTS = 0.60


class Chatbot:
    """Chatbot con IA"""

    def __init__(self, system_prompt: str = SYSTEM_PROMPT, model: str = MODEL):
        """Inicializa el chatbot"""
        self.client = OpenAI()
        self.system_prompt = system_prompt
        self.model = model
        self.history: list[dict] = [
            {"role": "system", "content": system_prompt}
        ]
        self.total_tokens = 0
        self.total_cost = 0.0

    def chat(self, user_message: str) -> str:
        """Chatea con la IA"""
        self.history.append({
            "role": "user",
            "content": user_message
        })

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.history,
            temperature=0.7
        )

        bot_message = response.choices[0].message.content

        self.history.append(
            {
                "role": "assistant",
                "content": bot_message
            }
        )

        self._update_cost(response.usage)

        return bot_message

    def _update_cost(self, usage) -> None:
        """Actualiza costos"""
        input_cost = (usage.prompt_tokens / 1_000_000) * INPUT_COSTS
        output_cost = (usage.completion_tokens / 1_000_000) * OUTPUT_COSTS
        total_cost = input_cost + output_cost

        self.total_tokens += usage.total_tokens
        self.total_cost += total_cost

    def show_stats(self) -> None:
        """Muestra estadísticas"""
        print(f"\n--Estadisticas--\n")
        print(f"Tokens utilizados: {self.total_tokens}")
        print(f"Costo total: ${self.total_cost:.6f}")


def main():
    """Función principal"""
    print("╔══════════════════════════════════════╗")
    print("║      Python IA Aplicada - Chatbot    ║")
    print("║  Escribe 'quit' o Ctrl+C para salir  ║")
    print("╚══════════════════════════════════════╝\n")
    bot = Chatbot()

    while True:
        try:
            try:
                user_input = input("Tú: ").strip()
            except EOFError:
                break

            if not user_input:
                continue

            if user_input.lower() in ("quit", "salir", "exit", "adios", "bye", "q", "exit"):
                break

            if user_input.lower() == "/stats":
                bot.show_stats()
                continue

            if user_input.lower() == "/reset":
                bot.history = [bot.history[0]]
                print("Historial limpiado")
                continue

            response = bot.chat(user_input)
            print("\nIA: ", end="", flush=True)
            try:
                response = bot.chat(user_input)
                print(response)
                print(
                    f"\n Tokens acumulados: {bot.total_tokens} | Costo total: ${bot.total_cost: .4f}USD\n")
            except Exception as e:
                print(f"\nError Inesperado {e}")

        except KeyboardInterrupt:
            print("\n" + "-" * 60)
            break
        finally:
            bot.show_stats()


if __name__ == "__main__":
    main()
