num = 1
par = 0
impar = 0

while num != 0:
    num = int(input("Insira um número: "))
    if num == 0:
        break
    elif num % 2 == 0:
        par += 1
    else:
        impar += 1
print("{} pares e  {} impares ".format(par,impar))


# O bloco do while será repetido quando a expressão booleana for verdadeira ou falsa

