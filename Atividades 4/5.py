n1 = float(input("Insira um número: "))
escolha = int(input("======================="
              "\nAgora escolha uma opção "
              "\n1 - Par ou Impar? "
              "\n2 - Positivo ou Negativo? "
              "\n3 - Inteiro ou Decimal? "))
if escolha == 1:
    if (n1 % 2 == 0) and (n1 != 0) :
        print("O numero,",n1," é par")
    elif n1 == 0:
        print("O número", n1, "é nulo.")
    else:
        print("O numero,",n1, "é impar")
elif escolha == 2:
    if n1 >= 1:
        print("O numero,",n1, "é positivo.")
    elif n1 == 0:
        print("O número", n1, "é nulo.")
    else:
        print("O numero,",n1, "é negativo")

elif escolha == 3:
    if (int(n1) == n1) and (n1 != 0):
        print(n1, "É um número inteiro")
    elif n1 == 0:
        print("O número", n1, "é nulo.")
    else:
        print(n1, "É um número decimal")






