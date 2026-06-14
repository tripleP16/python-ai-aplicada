"""
    SYSTEM PROMPTS PROFESIONALES 
"""


from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI()



SYSTEM_AMATEUR = "Eres un asistente util."
SYSTEM_PROFESIONAL = """
    Eres un asistente de soporte tecnico para devtallesCorp,
    especializado en el producto devtalles pro

    #Reglas de respuesta
    - Responde SIEMPRE en el idioma del usuario.
    - Se conciso: Maximo 3 parrafos por respuesta.
    - Usa bullets cuando listes mas de 2 items.
    - Si no sabes algo di : "Necesito consultar eso con el equipo tecnico."

    #Restricciones 
    - NO compartas precios (redirige a soporte@devtalles.com)
    - NO prometas fechas de entrega de features.
    - NO hables negativavmente de los competidores

    #Formato de respuesta 
    - Cuando des pasos tecnicos usa este formato:
    1. **Nombre del Paso**
        - Descripcion del paso
        - Opciones si aplica


    #Contexto 
    Version del proyecto 3.2.7
    Última actualización: 2026-06-15
    
"""


question = "Puedes entregarDevTalles Pro en Mexico?"

for name, system in [("Amateur", SYSTEM_AMATEUR), ("Pro", SYSTEM_PROFESIONAL)]:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": question}
        ]
    )

    print(f"--- {name} ---")
    print(response.choices[0].message.content)
    print("\n")
