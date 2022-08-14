

#função simples

def soma(a,b):
    return a + b

print(soma(20,50))

###############################################


def imprimirJuci():
    mercado = ["Pastel", "Bolacha Recheada", "Coca","Pizza"]
    print("Comprar no Gentil ")
    for item in mercado:
        print("Lista de compras: ", item)

imprimirJuci()

########################################################

# função com retorno

def maior(x,y):
    if x > y:
        return x
    else:
        return y

merda = int(input("Insira um valor: "))
bosta = int(input("Insira um valor: "))
z = maior(merda,bosta)
print(z)


#############################################################

#com recursão

def fatorial(x):
    if x == 0:
        return 1
    else:
        return x * fatorial (x-1)

num = int(input("Insira um valor para fatorar: "))
fatorial = fatorial(num)
print("O fatorial de {} é {} ".format(num,fatorial))


##############################################################

