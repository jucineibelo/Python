'''
10. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
programa que nos dê:
a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''

ganhoHora = float(input("Informe qual o valor da remuneração por hora? "))
horasTrabalhadas = float(input("Informe quantas horas você trabalhou no mês? "))

salarioBruto = ganhoHora * horasTrabalhadas
inss = salarioBruto * (8 / 100)
ir = salarioBruto * (11 / 100)
sindicato = salarioBruto * (5 / 100)
salarioLiquido = salarioBruto - inss - ir - sindicato

print("----------- FOLHA DE PAGAMENTO EMPRESA FULLSTACK NINJA LTDA -----------")
print('\n')
print("Seu salário Bruto é de R$: ",salarioBruto)
print("Foram descontados R$:",inss,"de INSS sob seu salário.")
print("Foram descontados R$:",ir,"de IR sob seu salário.")
print("Foram descontados R$:",sindicato,"de contribuição sindical sob seu salário.")
print("O valor de seu salário liquido é R$:",salarioLiquido, "Aproveite e faça bons gastos")
print(2*'\n')
print("----------- A EMPRESA FULL STACK TEM O PRAZER DE TER VOCÊ COMO COLABORADOR -----------")


