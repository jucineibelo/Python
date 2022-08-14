'''
4. Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10
metros e cresce 3 centímetros por ano. Escreva um programa em Python que
calcule e imprima quantos anos serão necessários para que Zé seja maior que
Chico.
- Números de anos é: “x”:

'''

chico = 1.50
ze = 1.10
contador = 0

while ze < chico:
    ze = ze + 0.03
    chico = chico + 0.02
    contador += 1
print("Quando se passar {} anos a idade de Zé vai ser superior a de Chico.".format(contador))
        
    
