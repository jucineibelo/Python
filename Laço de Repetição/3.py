'''
3. Faça um programa em Python que solicite ao usuário dois valores inteiros (int).
Agora imprima todos os números existentes entre esses dois valores, inclusive
eles, utilizando para isso o comando for. Veja os exemplos:

'''

n1 = int(input("Insira um número: "))
n2 = int(input("Insira um número: "))

for i in range(n1,n2+1):
    print(i)
