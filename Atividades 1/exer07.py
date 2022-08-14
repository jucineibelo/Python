'''
7. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade
de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima
os dados do programa com as mensagens adequadas.

'''

pescaria = float(input("Quantos kg de peixe João pescou? "))

if pescaria > 50:
    print("João pescou ",pescaria,"KG, devido exceder o peso gratutíto vai ter que pagar um total de R$:", pescaria * 4,".")

elif pescaria <= 49:
    print("João pescou", pescaria, "KGs de peixes.")






