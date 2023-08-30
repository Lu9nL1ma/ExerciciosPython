#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print('Analisando o número digitado, o dobro de {} é {}'.format(numero, dobro))
print('O triplo é: {}'.format(triplo))
print('E sua raiz quadrada é: {:.2f}'.format(raiz))