from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega a chave da API
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcrever_audio(caminho_arquivo):
    with open(caminho_arquivo, "rb") as audio_file:
        resposta = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return resposta.text
