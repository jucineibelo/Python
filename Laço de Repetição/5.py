'''
5. Faça um programa em Python que solicite ao usuário dois valores inteiros (int).
Agora imprima todos os números ímpares e pares existentes entre esses dois
valores, inclusive eles, utilizando para isso o comando While. Veja o exemplo:
- Digite o valor inicial: 5 - Digite o valor final: 20
- Números pares entre “5” e “20”: “6 8 10 12 14 16 18 20”
- Números ímpares entre “5” e “20”: “5 7 9 11 13 15 17 19”
'''

num1 = int(input("Insira um número: "))
num2 = int(input("Insira um número: "))

i = num1

while i <= num2:
    if (i %2 == 0):
        print(i)
    i += 1

print("Números pares {} e {}".format(num1,num2))

i = num1
while i <= num2:
    if (i %2 == 1):
        print(i)
    i += 1

print("Números impares {} e {}".format(num1,num2))
