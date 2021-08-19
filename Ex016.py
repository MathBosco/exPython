#Enunciado:
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

n = float(input('Insira um valor: '))

trunc = trunc(n)

print('O valor é {} sua parte inteira é: {}'.format(n , trunc))
