'''
4. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a
temperatura em graus Celsius. C = 5 * ((F-32) / 9).
'''

tempFah = int(input("Qual é a temperatura em Fahrenheit? "))

transformar = ((tempFah - 32) / 9) * 5

print("A temperatura em graus Celsius é: ", transformar)