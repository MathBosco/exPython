#Enunciado
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input('Qual o valor que você possui na sua carteira? R$ '))

dolares = dinheiro / 5.41
euro = dinheiro / 6.60


print('Com o valor de R${:.2f} você poderá comprar U${:.2f}'.format(dinheiro , dolares)
print('Com o valor de R${:;2f} você poderá comprar €{:.2f}'.format(dinheiro, euro))
