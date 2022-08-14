while True:
    print(" ****(MENU)****:")
    print(" 1. Adição:"
          "\n 2. Subtração:"
          "\n 3. Divisão:"
          "\n 4. Multiplicação:"
          "\n 5. Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        num1 = int(input("Insira um número: "))
        num2 = int(input("Insira um número: "))
        resposta = num1 + num2
        print(resposta)
    elif opcao == 2:
        num1 = int(input("Insira um número: "))
        num2 = int(input("Insira um número: "))
        resposta = num1 - num2
        print(resposta)
    elif opcao == 3:
        num1 = int(input("Insira um número: "))
        num2 = int(input("Insira um número: "))
        resposta = num1 / num2
        print(resposta)
    elif opcao == 4:
        num1 = int(input("Insira um número: "))
        num2 = int(input("Insira um número: "))
        resposta = num1 * num2
        print(resposta)
    elif opcao == 5:
        print("Programa Encerrado!")
        break
    else:
        print("Opção Invalida")

