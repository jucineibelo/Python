med1 = int(input("Insira a primeira medida do Triângulo: "))
med2 = int(input("Insira a segunda medida do Triângulo: "))
med3 = int(input("Insira a terceira medida do Triângulo: "))
soma = (med1 + med2) > med3
if (med1 == med2 != 0) and (med2 == med3):
    print("Os valores formam um Triangulo Equilátero")
elif soma == True and (med1 == med2 != 0) or (med1 == med3 != 0):
    print("Os valores formam um Triangulo Isósceles")
elif soma == True and (med1 != med2) and (med1 != med3):
    print("Os valores formam um Triangulo Escaleno")
else:
    print("Os valores não formam um triângulo")



