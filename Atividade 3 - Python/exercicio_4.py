while True:
    print("\nMenu:")
    print("[1] Olá")
    print("[2] Ajuda")
    print("[3] Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print("Olá!")
    elif opcao == "2":
        print("Este é um menu interativo.")
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")