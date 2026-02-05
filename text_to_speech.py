from gtts import gTTS
import pygame
import os

def falar_texto(texto, arquivo="resposta.mp3"):
    # 1. Gerar o arquivo de áudio
    tts = gTTS(texto, lang="pt")
    tts.save(arquivo)
    print(f"🔊 Áudio salvo em: {arquivo}")

    # 2. Tentar reproduzir (Só funciona se tiver dispositivo de áudio)
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(arquivo)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    except pygame.error:
        print("⚠️ Aviso: Dispositivo de áudio não encontrado (comum no Codespaces).")
        print("➡️ Baixe o arquivo 'resposta.mp3' para ouvir.")