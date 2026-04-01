# Scripts Python - Projetos Educacionais

Coleção de scripts Python com funcionalidades variadas para fins educacionais.

---

## 📄 Arquivos do Projeto

### 1. **ola.py**
Script simples que pede o nome do usuário e exibe uma saudação com o nome em **maiúscula**.

```bash
python ola.py
```

**O que faz:**
- Solicita o nome via `input()`
- Converte para maiúscula com `.upper()`
- Exibe mensagem de saudação formatada

---

### 2. **celsius_fahrenheit.py**
Conversor de temperatura de **Celsius para Fahrenheit** com formatação de saída.

```bash
python celsius_fahrenheit.py
```

**O que faz:**
- Pede a temperatura em Celsius
- Aplica a fórmula: `(C × 9/5) + 32`
- Exibe resultado com 1 casa decimal

---

### 3. **lista_compras.py**
Gerenciador de lista de compras com menu interativo de 4 opções.

```bash
python lista_compras.py
```

**Funcionalidades:**
- ✅ **Adicionar item** — Insere novo item na lista
- 👁️ **Ver lista** — Exibe todos os itens numerados
- ❌ **Remover item** — Remove por número
- 🚪 **Sair** — Encerra o programa

**Estrutura:** Loop `while True` com menu e tratamento de erros.

---

### 4. **quiz_cyber.py**
Quiz de **5 perguntas sobre Cibersegurança** com múltipla escolha (3 opções).

```bash
python quiz_cyber.py
```

**Perguntas cobertas:**
1. Phishing
2. VPN
3. HTTPS/TLS/SSL
4. Ataque DDoS
5. Boas práticas de senhas

**Resultado:**
- Mostra cada resposta (correta/incorreta)
- Placar final
- **Aprovado** se ≥ 3 acertos | **Reprovado** se < 3

---

### 5. **gerador_senhas.py**
Gerador de senhas aleatórias com opções customizáveis usando `random` e `string`.

```bash
python gerador_senhas.py
```

**Opções de configuração:**
- 📏 Tamanho da senha
- 🔤 Maiúsculas (A-Z)
- 🔢 Números (0-9)
- 🔣 Símbolos (!@#$%^&*)

**Como funciona:**
- Combina caracteres conforme seleção
- Usa `random.choice()` para gerar a senha
- Exibe resultado criptograficamente aleatório

---

## 🛠️ Requisitos

- **Python 3.6+**
- Nenhuma dependência externa (usa apenas bibliotecas padrão)

---

## 🚀 Como usar

Cada script é independente. Execute diretamente:

```bash
python nome_do_arquivo.py
```

---

## 📚 Conceitos Praticados

- ✅ Entrada/saída (`input()`, `print()`)
- ✅ Estruturas de controle (`if/elif/else`, `while`)
- ✅ Listas e iteração (`for`, `.append()`, `.pop()`)
- ✅ Formatação de strings (f-strings)
- ✅ Módulos padrão (`random`, `string`)
- ✅ Tratamento de erros (`try/except`)
- ✅ Funções e lógica programação

---

## 📝 Autor

José Menezes
