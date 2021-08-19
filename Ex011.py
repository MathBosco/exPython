#Enunciado:
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Insira o valor da largura da parede em metros: '))
altura = float(input('Insira o valor da altura da parede em metros: '))
area = altura * largura
litros = area / 2

print('Para pintar uma area de {:.2f} metros será necessário {} litros de tinta'.format(area , litros))
