# 🎲 Sandbox RPG Engine (Anti-Godmodding AI)

![Status](https://img.shields.io/badge/Status-Estável-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Ready-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Um motor de **RPG de Texto Sandbox** movido por Inteligência Artificial, projetado para criar histórias em qualquer universo com **zero interferência na agência do jogador** (*Anti-Godmodding*).

Diferente de chats comuns onde a IA assume o controle do seu personagem, decide suas falas ou força escolhas pré-definidas, este motor utiliza **Diretrizes de Sistema Restritivas** e **Injeção Invisível de Turno** para garantir que a IA atue exclusivamente como o mundo, o ambiente e os NPCs.

---

## ✨ Funcionalidades Principais

- **🔒 Trava Anti-Godmodding:** A IA é proibida em nível de sistema e de turno de falar, pensar, sentir ou agir pelo personagem do jogador.
- **🌍 Liberdade Sandbox Total:** Aceita qualquer cenário, época ou gênero (Fantasia Sombria, Sci-Fi, Cyberpunk, Simulação Política, Histórico, etc.).
- **🎭 Imersão Sensorial e Psicológica:** Foco em descrições de ambiente (luz, som, clima, cheiro) e emoções reais dos NPCs demonstradas por linguagem corporal e tom de voz.
- **🌐 Duas Versões Incluídas:**
  - **Versão Web (`index.html`):** Pronta para rodar direto no **GitHub Pages** sem precisar de servidor backend.
  - **Versão Terminal (`main.py`):** Script em Python com suporte a variáveis de ambiente seguras (`.env`).

---

## 🚀 Como Usar

### Opção 1: Rodando no Navegador (GitHub Pages)
1. Faça o fork ou upload deste repositório no seu GitHub.
2. Vá em **Settings > Pages** e ative o GitHub Pages na branch `main` (pasta `/root`).
3. Acesse o link gerado, insira sua chave da API do Google Gemini (ela fica salva apenas no seu navegador via `localStorage`, nunca no código público) e comece a jogar.

### Opção 2: Rodando no PC via Python
1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/sandbox-rpg-engine.git
   cd sandbox-rpg-engine
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure sua chave de API com segurança:
   - Renomeie o arquivo `.env.example` para `.env`
   - Coloque sua chave dentro dele: `GEMINI_API_KEY=sua_chave_aqui`
4. Execute o motor:
   ```bash
   python main.py
   ```

---

## 🧠 Arquitetura do Prompt (Como a Trava Funciona)

O motor divide cada resposta da IA em 3 etapas obrigatórias:
1. **Consequência:** O impacto direto da última ação do jogador no mundo.
2. **Desenvolvimento e Ambiente:** Detalhamento sensorial do cenário e reações coerentes dos NPCs.
3. **Gancho Aberto:** Interrupção imediata da narração no exato momento em que uma reação do jogador é necessária (sem listas de múltipla escolha).

---

## 📄 Licença
Distribuído sob a licença MIT. Sinta-se livre para modificar e expandir.
