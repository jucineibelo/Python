quantidade = int(input("Digite quantas vezes você quer que o loop repita: "))

soma = 0

for i in range (1, quantidade+1):
    num = int(input("Insira um número para somar: "))
    soma += num

print("O resultado da soma é {}.".format(soma))
