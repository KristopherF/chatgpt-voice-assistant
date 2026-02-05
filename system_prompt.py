from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega a chave
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_resposta(texto_usuario):
    # Personalidade do Assistente Financeiro (Engenharia de Prompt)
    system_prompt = """
    Você é o 'FinBot', um consultor financeiro pessoal baseado em IA.
    Seu objetivo é democratizar o acesso à informação financeira com clareza e empatia.
    
    Diretrizes de comportamento:
    1. Explique termos complexos (CDB, FIIs, Selic) de forma simples (UX Writing).
    2. Se o usuário perguntar sobre valores, faça simulações estimadas e avise que não é recomendação de investimento.
    3. Seja conciso, pois sua resposta será falada em áudio (evite listas longas).
    4. Mantenha um tom profissional, porém amigável e encorajador.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": texto_usuario}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Desculpe, tive um problema ao consultar meus dados financeiros. Erro: {e}"