# 💰 FinBot - Assistente Financeiro com IA Generativa

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-Whisper%20%7C%20GPT-green)
![UX](https://img.shields.io/badge/UX-Financial%20Experience-purple)

> Projeto desenvolvido para o desafio "Construa seu Assistente Virtual", focado em **relacionamento financeiro** e boas práticas de experiência do usuário.

## 🎯 Objetivo do Projeto
Criar uma experiência digital acessível onde o usuário pode tirar dúvidas sobre **investimentos, taxas (Selic/CDI)** e solicitar **simulações financeiras** usando apenas a voz. A solução democratiza o acesso à informação financeira através de uma interface natural e sem barreiras de digitação.

## 🧠 Inteligência Financeira (Features)
O sistema foi projetado com um *System Prompt* especialista que garante:
- **Linguagem Acessível:** Tradução de "bancavês" para português claro.
- **Simulações Rápidas:** Cálculos estimativos de rendimento (ex: Poupança vs. FIIs).
- **Educação Financeira:** Explicação de conceitos complexos de forma didática.

## 🛠️ Arquitetura Técnica
A solução integra três pilares de IA para criar um fluxo contínuo:
1.  **Audição (Input):** `OpenAI Whisper` transcreve a dúvida financeira do usuário.
2.  **Raciocínio (Core):** `GPT-3.5 Turbo` (configurado como consultor financeiro) processa a dúvida e gera uma resposta empática e técnica.
3.  **Fala (Output):** `gTTS` converte a orientação financeira em áudio para resposta imediata.

## 📂 Estrutura
- `app.py`: Orquestrador da experiência do usuário.
- `chat_response.py`: Contém a lógica de **Engenharia de Prompt** focada em finanças.
- `speech_to_text.py`: Módulo de transcrição de voz.
- `text_to_speech.py`: Módulo de síntese de voz.

## 🚀 Como testar a experiência
1. Instale as dependências: `pip install -r requirements.txt`
2. Configure sua `OPENAI_API_KEY` no arquivo `.env`.
3. Adicione um arquivo `entrada.wav` com uma dúvida (Ex: *"Quanto rende 1000 reais no Tesouro Selic?"*).
4. Execute: `python app.py`.

---
*Desenvolvido aplicando conceitos de Generative AI, Python e Financial UX.*