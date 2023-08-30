#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

numero1 = float(input('Insira a primeira nota: '))
numero2 = float(input('Insira a segunda nota: '))
media = (numero1+numero2) / 2
print('A média entre as notas {} e {} é: {:.1f}'.format(numero1, numero2, media))

