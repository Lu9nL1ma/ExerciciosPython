#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

produto = float(input('Digite o valor do produto: R$ '))
desc = produto * 5 / 100
novo_valor = produto - desc
print('O valor do produto com 5 por cento de desconto é de: R$ {:.2f}'.format(novo_valor))
