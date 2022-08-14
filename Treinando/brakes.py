'''
saíndo de loops com break

Utilizamos o break para sair de loops de maneira projetada
'''

for numero in range(1,11):
    if numero ==6:
        break
    else:
        print(numero)
print("Sai do loop")


while True:
    comando = str((input("Digite 'sair' para sair: ")))
    if comando == "sair":
        print("Você saiu")
        break