'''
2 - Faça um programa em Python que solicite ao usuário um valor inteiro (int).
Agora imprima todos os números existentes entre 0 e o valor digitado, inclusive
ele, mas dessa vez em ordem decrescente. Utilize para isso o comando For. Veja
os exemplos:

'''

n = int(input("Digite um número: "))

for i in range (n,0-1,-1):
    print(i)

