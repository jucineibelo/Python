morango = float(input("Quantos KG de morango deseja comprar? "))
maca = float(input("Quantos KG de maçã deseja comprar? "))

if (morango <= 5) and (morango != 0):
    calculo = morango * 3.50
    print("Valor total a pagar R$: ", round(calculo))
elif morango > 5:
    calculo = morango * 3.20
    if (calculo >= 28) or (morango > 8):
        desconto = calculo * 0.10
        total = calculo - desconto
        print("Valor do Desconto R$: ", round(desconto),
              "\nValor total a pagar R$: ",round(total))
    else:
        print("Valor total a pagar R$: ", round(calculo,2))

if (maca <= 5) and (maca != 0):
    calculo = maca * 2.80
    print("Valor total a pagar R$: ", round(calculo))
elif maca > 5:
    calculo = maca * 2.50
    if (calculo >= 28) or (maca > 8):
        desconto = calculo * 0.10
        total = calculo - desconto
        print("Valor do Desconto R$: ", round(desconto),
              "\nValor total a pagar R$: ",round(total))
    else:
        print("Valor total a pagar R$: ", round(calculo,2))


