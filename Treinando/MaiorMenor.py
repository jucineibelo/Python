'''
Faça uma função que lê 5 valores inteiros e retorna o maior e o
menor deles.
'''

maior = menor = 0
i = 1
while i <= 5:
    num1 = int(input("Digite um número: "))
    if i == 1:
        maior = menor = num1
    if num1 > maior:
        maior = num1
    if num1 < menor:
        menor = num1
    i += 1

print(maior)
print(menor)

