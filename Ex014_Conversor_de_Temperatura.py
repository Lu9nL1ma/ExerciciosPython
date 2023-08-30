#Exercício Python 14: Escreva um programa que converta uma temperatura
#Digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Qual a temperatura atual em Celsius: '))
conv_fahrenheit = temp * 9 / 5 + 32

print('A temperatura de {:.1f}C, corresponde a {:.1f}F'.format(temp, conv_fahrenheit))
