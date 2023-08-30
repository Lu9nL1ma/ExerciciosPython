#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#E mostre quantos dólares e euros ela pode comprar.

money = float(input('Quanto em R$ você tem: '))
dolar = money / 5
euro = money / 6

print('Com R$ {:.2f}, você pode comprar US$ {:.2f}'.format(money, dolar))
print('Com R$ {:.2f}, você pode comprar €$ {:.2f}'.format(money, euro))
