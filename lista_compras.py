lista = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Ver lista")
    print("3. Remover item")
    print("4. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item: ")
        lista.append(item)
        print(f'"{item}" adicionado.')

    elif opcao == "2":
        if not lista:
            print("Lista vazia.")
        else:
            print("\nItens na lista:")
            for i, item in enumerate(lista, 1):
                print(f"  {i}. {item}")

    elif opcao == "3":
        if not lista:
            print("Lista vazia.")
        else:
            print("\nItens na lista:")
            for i, item in enumerate(lista, 1):
                print(f"  {i}. {item}")
            try:
                num = int(input("Número do item a remover: "))
                removido = lista.pop(num - 1)
                print(f'"{removido}" removido.')
            except (ValueError, IndexError):
                print("Número inválido.")

    elif opcao == "4":
        print("Até logo!")
        break

    else:
        print("Opção inválida.")
