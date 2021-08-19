#Enunciado
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))
hi = (co ** 2  + ca ** 2) ** (1/2)

print('Valor da Hipotenusa = {:.2f}'.format(hi))
