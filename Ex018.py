#Enunciado:
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
a = float(input('Digite um Ângulo: '))
se = math.sin(math.radians(a))
co = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print('Seno: {:.2f}  \nCosseno: {:.2f} \nTangente: {:.2f}'.format(se , co , tan)) 
