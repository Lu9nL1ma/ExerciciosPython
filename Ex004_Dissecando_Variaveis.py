# Exercício Python 4: Faça um programa que leia algo pelo teclado
# E mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

valor = input('Digite algo:')

print('O tipo primitivo é: ', type(valor))
print('É numérico:', valor.isnumeric())
print('É alfabeto:', valor.isalpha())
print('É alfanumérico:', valor.isalnum())
print('Está em maiúsculas:', valor.isupper())
print('Está em minúsculas:', valor.islower())
print('Está capitalizada:', valor.istitle())
