import random
import string

print("=== GERADOR DE SENHAS ===\n")

tamanho = int(input("Tamanho da senha: "))

maiusculas = input("Incluir maiúsculas? (s/n): ").strip().lower() == "s"
numeros = input("Incluir números? (s/n): ").strip().lower() == "s"
simbolos = input("Incluir símbolos? (s/n): ").strip().lower() == "s"

caracteres = string.ascii_lowercase

if maiusculas:
    caracteres += string.ascii_uppercase
if numeros:
    caracteres += string.digits
if simbolos:
    caracteres += string.punctuation

if len(caracteres) == 0:
    print("Nenhum tipo de caractere selecionado.")
else:
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    print(f"\nSenha gerada: {senha}")
