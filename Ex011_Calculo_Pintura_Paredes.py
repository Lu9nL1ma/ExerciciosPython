#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros
#Calcule a sua área e a quantidade de tinta necessária para pintá-la
#Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Insira a largura da sua parede: '))
altura = float(input('Insira a altura da sua parede: '))
dimensao = largura * altura
tinta = dimensao / 2
print('A dimensão da sua parede é: {:.2f}m²'.format(dimensao))
print('Para pintar sua parede você precisará de {}l de tinta'.format(tinta))
