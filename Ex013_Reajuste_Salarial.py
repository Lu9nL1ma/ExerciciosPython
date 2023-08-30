#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário
#E mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário atual: R$ '))
novo_salario = salario + (salario * 15 / 100)

print('O salário atual de R$ {:.2f} com 15 por cento de aumento ficará: R$ {:.2f}'.format(salario, novo_salario))

