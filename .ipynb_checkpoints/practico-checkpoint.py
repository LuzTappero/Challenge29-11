from dotenv import load_dotenv
import json
import ipywidgets as widgets
from IPython.display import display, clear_output
import cohere
import os

load_dotenv()
api_key= os.getenv("COHERE_API_KEY")

COHERE_API_KEY = cohere.ClientV2()


# Paso 1, generar una historia corta 100 palabras como mucho y guardarla en una variable.

response = COHERE_API_KEY.chat(
    model="command-r-plus-08-2024",
    messages=[{"role": "user", "content": "Escribime una historia de 100 palabras de un cuento infantil que sea sobre hadas"}],
)

resp= (response.message.content[0].text)
# print (resp)

# Paso 2, ir generando instrucciones para responder de cirta forma sobre la pregunta

response = COHERE_API_KEY.chat(
    model="command-r-plus-08-2024",
    messages=[{"role": "user", "content": "Escribime una historia de 100 palabras de un cuento infantil que sea sobre hadas"}],
)

resp= (response.message.content[0].text)
# print (resp)
# ir agregando items

# - quiero una respuesta concisa
# - responde ademas del texto utilizando emojis que resuman la respuesta
# - responde en tercera persona
# - responde en el idioma que te pregunta el usuario

idioma = input("Especifique el idioma deseado: ")

response = COHERE_API_KEY.chat(
    model="command-r-plus-08-2024",
    messages=[{"role": "user", "content": f"Primer paso: generar un título en {idioma}; Segundo paso: generar la historia de 200 palabras de un cuento infantil que hable sobre hadas en {idioma}; tercer paso: genera una reflexión de aprendizaje sobre el mismo en {idioma}"}],
)

resp= (response.message.content[0].text)
print (resp)