import openai
from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_resposta(texto_usuario):
    resposta = openai.Chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": texto_usuario}]
    )
    return resposta.choices[0].message.content
