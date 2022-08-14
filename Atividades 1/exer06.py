'''
6. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3
metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe
ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''

areaPintada = float(input("Quantos metros quadrados da a área a ser pintada? "))
calcLatas = areaPintada / 3
calcLitros = calcLatas / 18
calclPreco = calcLitros * 80

print(" Para a área de:", areaPintada," metros quadrados será necessário comprar", round(calcLatas,2), "latas de tinta, o valor gasto será de R$:", round(calclPreco,2))




