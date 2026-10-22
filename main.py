import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Carrega a chave de API do arquivo .env (segurança para não expor no GitHub)
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY or API_KEY == "cole_sua_api_key_do_google_ai_studio_aqui":
    print("[ERRO]: Chave GEMINI_API_KEY não encontrada!")
    print("Crie um arquivo '.env' na mesma pasta e adicione: GEMINI_API_KEY=sua_chave")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)

SYSTEM_INSTRUCTION = """[SYSTEM_DIRECTIVE: SANDBOX_RPG_ENGINE]
Você é um Motor de Simulação e Mestre de RPG de Texto Sandbox detalhista e adaptável.

REGRAS ABSOLUTAS DE AGÊNCIA (ANTI-GODMODDING):
1. PROIBIÇÃO TOTAL DE CONTROLE: Você NUNCA deve falar, pensar, sentir, decidir ou executar ações pelo personagem do usuário.
2. NARRATIVA EXTERNA: Você controla apenas o ambiente, o clima, a passagem do tempo, as leis do mundo e os NPCs.
3. INTERRUPÇÃO EM MOMENTO CRÍTICO: Sempre que um NPC fizer uma pergunta, atacar ou criar uma situação que exija reação do jogador, PARE IMEDIATAMENTE a geração de texto e aguarde o comando do usuário.

DIRETRIZES DE IMERSÃO E COERÊNCIA:
1. DETALHAMENTO SENSORIAL: Descreva o cenário usando visão, audição, olfato, tato e atmosfera.
2. PSICOLOGIA DOS NPCs: Demonstre emoções através de microexpressões, postura e tom de voz. NPCs possuem conhecimentos e interesses próprios (não são oniscientes).
3. COERÊNCIA: Mantenha a lógica interna do mundo. Ações têm consequências reais.
4. SEM CLICHÊS DE ESCOLHA: Nunca termine com listas de opções (A, B, C) nem com a pergunta "O que você faz?".
"""

def salvar_log(texto: str):
    with open("historico_rpg.txt", "a", encoding="utf-8") as f:
        f.write(texto + "\n")

def iniciar_rpg():
    print("=" * 60)
    print("🎲 MOTOR DE RPG SANDBOX (TERMINAL EDITION)")
    print("=" * 60)
    print("Comandos especiais: '/sair' para encerrar | '/salvar' avisa onde o log está.\n")
    
    cenario = input("Descreva o cenário inicial, época e quem é o seu personagem:\n> ").strip()
    if not cenario:
        cenario = "Fantasia medieval sombria. Sou um viajante chegando a uma cidade murada sob forte neblina."

    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.85,
        )
    )

    prompt_inicial = (
        f"Cenário inicial estabelecido pelo jogador: {cenario}.\n"
        "Inicie a história descrevendo detalhadamente o cenário ao redor do jogador e a atmosfera inicial. "
        "NÃO fale nem execute ações pelo jogador."
    )

    print("\n[Gerando mundo...]\n")
    resposta = chat.send_message(prompt_inicial)
    print(f"[NARRADOR]:\n{resposta.text}\n" + "-" * 60)
    salvar_log(f"=== CENÁRIO: {cenario} ===\n\n[NARRADOR]:\n{resposta.text}\n" + "-" * 40)

    while True:
        try:
            acao = input("\n[SUA AÇÃO]: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nEncerrando sessão...")
            break

        if not acao:
            continue
        if acao.lower() in ["/sair", "sair", "exit"]:
            print("Sessão encerrada. Seu histórico foi salvo em 'historico_rpg.txt'.")
            break

        # Reforço invisível em cada turno para impedir amnésia da IA
        prompt_turno = (
            f"Ação/Fala do Jogador: {acao}\n\n"
            "[DIRETRIZ DE TURNO: Narre apenas a reação do mundo e dos NPCs. "
            "Detalhe o ambiente e as emoções dos NPCs com coerência. "
            "É estritamente proibido falar, pensar ou agir pelo personagem do jogador.]"
        )

        resposta = chat.send_message(prompt_turno)
        print(f"\n[NARRADOR]:\n{resposta.text}\n" + "-" * 60)
        salvar_log(f"[JOGADOR]: {acao}\n\n[NARRADOR]:\n{resposta.text}\n" + "-" * 40)

if __name__ == "__main__":
    iniciar_rpg()
