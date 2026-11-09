import os
from dotenv import load_dotenv
from openai import OpenAI

def config_ia():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Chave da API não encontrada!")

    modelo_ia = OpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    return modelo_ia

def mensagem_da_ia(lista_mensagem):
    modelo_ia = config_ia()

    resposta_modelo = modelo_ia.chat.completions.create(
        messages=lista_mensagem,
        model="gemini-flash-lite-latest"
    )

    resposta_ia = resposta_modelo.choices[0].message.content

    return resposta_ia

    
