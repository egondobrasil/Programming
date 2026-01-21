while True:
    print("\n===MENU PRINCIPAL===")
    print("1. Cadastro")
    print("2. Consulta")
    print("3. Relatório")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("\x1b[92m 1Você escolheu Cadastro.\x1b[00m")

        case "2":
            print("\x1b[92m Você escolheu Consulta.\x1b[00m")   

        case "3":
            print("\x1b[92m Você escolheu Relatório.\x1b[00m")
            
        case "4":
            print("\x1b[91m Você escolheu sair do sistema.\x1b[00m") 
            break
        case _:
            print("\x1b[55m Opção inválida. Tente novamente.\x1b[00m")