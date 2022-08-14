'''

8. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos).

'''

tamanhoArquivo = float(input("Qual o tamanho do arquivo você quer baixar em MB? "))
velocidadeInternet = float(input("Qual a velocidade de sua internet em Mbps? "))


calculo = ((tamanhoArquivo * 8) / velocidadeInternet) / 60

print("O tempo de download estimado é ", round(calculo,2), "em minutos")

