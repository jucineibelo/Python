'''

9. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A. o produto do dobro do primeiro com metade do segundo
B. a soma do triplo do primeiro com o terceiro.
C. o terceiro elevado ao cubo.

'''

n1 = int(input("Digite o primeiro número? "))
n2 = int(input("Digite o segundo número? "))
n3 = float(input("Digite um número com vírgula? "))

calculoA = (n1 * 2) + (n2 / 2)  #Calculo letra A
calculoB = (n1 * 3) + n3      #Calculo Letra B
calculoC = n3 ** 3


print("A resposta da questão A é: ",calculoA)
print("A resposta da questão B é: ",calculoB)
print("A resposta da questão C é: ",calculoC)


