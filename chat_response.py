from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega a chave
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_resposta(texto_usuario):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # Ou "gpt-4" se preferir
            messages=[
                {"role": "system", "content": "Você é um assistente útil e conciso."},
                {"role": "user", "content": texto_usuario}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro ao conectar com a OpenAI: {e}"