from gtts import gTTS
import pygame

def falar_texto(texto, arquivo="resposta.mp3"):
    # Gera o áudio a partir do texto
    tts = gTTS(texto, lang="pt")
    tts.save(arquivo)

    # Inicializa o mixer do pygame
    pygame.mixer.init()
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()

    # Mantém o programa rodando até terminar a reprodução
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
