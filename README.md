# ChatGPT Voice Assistant 🎙️🤖

Este projeto integra **Whisper (OpenAI)** para transcrição de áudio, **ChatGPT** para geração de respostas inteligentes e **gTTS** para síntese de voz.

## 🚀 Tecnologias
- Python
- OpenAI Whisper
- OpenAI ChatGPT
- Google Text-to-Speech (gTTS)

## 📂 Estrutura
- `speech_to_text.py` → transcreve áudio
- `chat_response.py` → gera resposta com ChatGPT
- `text_to_speech.py` → converte resposta em voz
- `app.py` → orquestra tudo

## ▶️ Como executar
```bash
git clone https://github.com/seuusuario/chatgpt-voice-assistant.git
cd chatgpt-voice-assistant
pip install -r requirements.txt
python app.py
