#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um numero inteiro: '))
sucessor = numero +1
antecessor = numero -1

print('O sucessor desse número é: {}, e o antecessor é {}'.format(sucessor, antecessor))
