# 🎙️ ChatGPT Voice Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green)
![Status](https://img.shields.io/badge/Status-Didático-orange)

Este projeto é um assistente de voz que integra **Whisper (OpenAI)** para transcrição de áudio, **ChatGPT** para geração de respostas inteligentes e **gTTS/Pygame** para síntese e reprodução de voz.

O objetivo é demonstrar a orquestração de diferentes módulos em Python para criar uma interface de conversação natural.

## 🚀 Tecnologias Utilizadas

- **[Python](https://www.python.org/)**: Linguagem principal.
- **[OpenAI Whisper](https://openai.com/research/whisper)**: Para converter fala em texto (Speech-to-Text).
- **[OpenAI GPT](https://platform.openai.com/)**: Modelo de linguagem para gerar respostas.
- **[gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)**: Para converter texto em áudio.
- **[Pygame](https://www.pygame.org/)**: Para reprodução do áudio gerado.
- **Python-dotenv**: Gerenciamento seguro de chaves de API.

## 📂 Estrutura do Projeto

```plaintext
chatgpt-voice-assistant/
│
├── app.py                # Orquestrador (Main)
├── speech_to_text.py     # Módulo de transcrição (Whisper)
├── chat_response.py      # Módulo de inteligência (GPT)
├── text_to_speech.py     # Módulo de síntese de voz (gTTS)
├── requirements.txt      # Dependências do projeto
├── .env                  # Chave da API (Não versionado)
└── entrada.wav           # Arquivo de áudio para teste

## 🔄 Fluxo de Dados

```mermaid
graph TD;
    A[🎤 entrada.wav] -->|Whisper| B(speech_to_text.py);
    B -->|Texto Transcrito| C(chat_response.py);
    C -->|Consulta GPT| D{OpenAI API};
    D -->|Resposta Texto| C;
    C -->|Texto| E(text_to_speech.py);
    E -->|gTTS| F[🔊 Reprodução Pygame];

    ⚙️ Configuração
1. Pré-requisitos
No Codespaces ou Linux, é recomendável instalar o ffmpeg para manipulação de áudio:

Bash

sudo apt update && sudo apt install -y ffmpeg    

2. Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto e adicione sua chave da OpenAI:

Snippet de código

OPENAI_API_KEY=sk-sua-chave-aqui-xyz...

⚠️ Atenção: Este projeto utiliza a API da OpenAI. É necessário ter créditos ativos na plataforma (Billing) para que a transcrição e a geração de texto funcionem corretamente.

📦 Instalação e Execução
Crie o ambiente virtual (Recomendado):

Bash

python -m venv venv
source venv/bin/activate
Instale as dependências:

Bash

pip install -r requirements.txt
Prepare o áudio: Certifique-se de que existe um arquivo chamado entrada.wav na raiz do projeto (você pode fazer upload de um áudio gravado ou gerar um para teste).

Execute o projeto:

Bash

python app.py
⚠️ Nota sobre Codespaces
Se você estiver rodando este código no GitHub Codespaces:

O script executará a transcrição e a geração da resposta.

Porém, o Pygame não conseguirá reproduzir o som (pois o servidor na nuvem não tem caixas de som).

O arquivo de resposta de áudio (ex: resposta.mp3) será salvo na pasta. Você pode clicar com o botão direito no arquivo e escolher Download para ouvir o resultado.

🎯 Objetivo da Atividade
Este projeto foi desenvolvido como modelo didático para demonstrar:

Integração de APIs: Conexão entre serviços de IA e scripts locais.

Segurança: Uso de variáveis de ambiente (.env) para proteger credenciais.

Modularização: Separação de responsabilidades (STT, LLM, TTS) em arquivos distintos.