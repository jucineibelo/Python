#DESAFIO COM LISTAS

num1 = []

for i in range(0,7):
    num1.append(int(input("Insira um número: ")))

print(sorted(num1))

num1.sort(reverse=True)
print(num1)


#DESAFIO COM LAÇO E VARIÁVEIS

n1 = int(input("Insira um número: "))
n2 = int(input("Insira um número: "))
n3 = int(input("Insira um número: "))
n4 = int(input("Insira um número: "))
n5 = int(input("Insira um número: "))
n6 = int(input("Insira um número: "))
n7 = int(input("Insira um número: "))

#crescente
for i in range (0,500):
    if i == n1 or i == n2 or i == n3 or i == n4 or i == n5 or i == n6 or i == n7:
        print(i)

#decrescente
for i in range (500, 0 - 1):
    if i == n1 or i == n2 or i == n3 or i == n4 or i == n5 or i == n6 or i == n7:
        print(i)









