# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias_alugados = int(input('Quantos dias o carro foi alugado? '))
km_percorrido = float(input('Quantos Km foram rodados nesse período? '))
pagar = (dias_alugados * 60) + (km_percorrido * 0.15)

print('O total a pagar é de R$ {}'.format(pagar))
