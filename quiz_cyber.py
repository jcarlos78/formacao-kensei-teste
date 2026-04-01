perguntas = [
    {
        "pergunta": "O que é phishing?",
        "opcoes": ["1. Técnica de invasão por força bruta", "2. Golpe para roubar dados via e-mail falso", "3. Tipo de vírus que criptografa arquivos"],
        "resposta": "2"
    },
    {
        "pergunta": "O que significa VPN?",
        "opcoes": ["1. Virtual Private Network", "2. Verified Public Node", "3. Virtual Protocol Number"],
        "resposta": "1"
    },
    {
        "pergunta": "Qual protocolo é usado para criptografar sites (HTTPS)?",
        "opcoes": ["1. FTP", "2. SSH", "3. TLS/SSL"],
        "resposta": "3"
    },
    {
        "pergunta": "O que é um ataque DDoS?",
        "opcoes": ["1. Roubo de senhas via teclado", "2. Sobrecarga de um servidor com muitas requisições", "3. Acesso remoto não autorizado"],
        "resposta": "2"
    },
    {
        "pergunta": "Qual é a melhor prática para senhas?",
        "opcoes": ["1. Usar a mesma senha em todos os sites", "2. Senha curta e fácil de lembrar", "3. Senha longa, única e com caracteres variados"],
        "resposta": "3"
    }
]

print("=== QUIZ DE CIBERSEGURANÇA ===\n")

pontuacao = 0

for i, q in enumerate(perguntas, 1):
    print(f"Pergunta {i}: {q['pergunta']}")
    for opcao in q["opcoes"]:
        print(f"  {opcao}")

    resposta = input("Sua resposta (1, 2 ou 3): ").strip()

    if resposta == q["resposta"]:
        print("Correto!\n")
        pontuacao += 1
    else:
        correto = q["opcoes"][int(q["resposta"]) - 1]
        print(f"Errado. Resposta correta: {correto}\n")

print("=" * 30)
print(f"Pontuação: {pontuacao}/5")

if pontuacao >= 3:
    print("Resultado: APROVADO! Bom conhecimento em cyber!")
else:
    print("Resultado: REPROVADO. Estude mais sobre cibersegurança!")
