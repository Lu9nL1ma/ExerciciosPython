#Exercício Python 8: Escreva um programa que leia um valor em metros
#E o exiba convertido em centímetros e milímetros.

medida = float(input('Insira a medida em metros (m): '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('O valor de {}m em Kilometros é: {}km'.format(medida, km))
print('O valor de {}m em Hectometro é: {}hm'.format(medida, hm))
print('O valor de {}m em Decametro é: {}dam'.format(medida, dam))
print('O valor de {}m em Decimetros é: {:.0f}dm'.format(medida, dm))
print('O valor de {}m em Centimetros é: {:.0f}cm'.format(medida, cm))
print('O valor de {}m em Milimetros é: {:.0f}mm'.format(medida, mm))
