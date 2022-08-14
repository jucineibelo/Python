ano = int(input("Informe um ano para saber se ele é bissexto:"))

if (ano % 4 == 0) or (ano % 100 == 0) and (ano % 400 != 0):
    print("O ano",ano," é Bissexto")
else:
    print("O ano",ano,"Não é bissexto")
