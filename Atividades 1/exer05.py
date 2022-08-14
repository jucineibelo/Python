'''
5. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule
seu peso ideal, utilizando as seguintes fórmulas:
a) Para homens: (72.7*h) - 58
b) Para mulheres: (62.1*h) - 44.7
'''

alturaH = float(input("Homem, qual a sua estatura? "))
formula = (72.7*alturaH) - 58
print(" Caso realmente seja homem, o peso ideal para sua estatura é de", round(formula,2),"kgs." )

alturaM = float(input("Mulher, qual a sua estatura? "))
formulaM = (62.1*alturaH) - 44.7
print(" Caso realmente seja mulher, o peso ideal para sua estatura é de", round(formulaM,2),"kgs." )


