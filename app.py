import sys, os
sys.path.append(os.path.dirname(__file__))

from speech_to_text import transcrever_audio
from chat_response import gerar_resposta
from text_to_speech import falar_texto

def main():
    texto_usuario = transcrever_audio("entrada.wav")
    print("Usuário:", texto_usuario)

    resposta = gerar_resposta(texto_usuario)
    print("ChatGPT:", resposta)

    falar_texto(resposta)

if __name__ == "__main__":
    main()
