a = int(input("Digite um valor inteiro: "))
b = int(input("Digite um valor inteiro: "))
c = int(input("Digite um valor inteiro: "))
delta = (b ** 2) - (4 * a * c)
if a == 0:
    print("A equação não é do segundo grau")
elif delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    print("A equação possui apenas uma raiz real.")
elif delta >= 1:
    print("A equação possui duas raizes reais.",delta)


