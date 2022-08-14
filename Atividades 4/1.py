salario = float(input("Informe qual seu salário? "))
if salario <= 500:
    valorAumento20 = salario * 0.20
    novoSalario20 = valorAumento20 + salario
    print(" Salario antes do reajuste",salario,
          "\n Percentual de aumento: 20%."
          "\n Valor do aumento",valorAumento20,
          "\n Novo Salário", novoSalario20)
elif (salario > 500) and (salario <= 800):
    valorAumento15 = salario * 0.15
    novoSalario15 = valorAumento15 + salario
    print(" Salario antes do reajuste",salario,
          "\n Percentual de aumento: 15%."
          "\n Valor do aumento",valorAumento15,
          "\n Novo Salário", novoSalario15)
elif (salario > 800) and (salario <= 1500):
    valorAumento10 = salario * 0.10
    novoSalario10 = valorAumento10 + salario
    print(" Salario antes do reajuste",salario,
          "\n Percentual de aumento: 10%."
          "\n Valor do aumento",valorAumento10,
          "\n Novo Salário", novoSalario10)
elif salario > 1500:
    valorAumento5 = salario * 0.05
    novoSalario5 = valorAumento5 + salario
    print(" Salario antes do reajuste",salario,
          "\n Percentual de aumento: 5%."
          "\n Valor do aumento",valorAumento5,
          "\n Novo Salário", novoSalario5)
else:
    print("Valor Invalido")