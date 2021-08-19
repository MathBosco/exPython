#Enunciado
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

var = input('Insira algo: ')

print(type(var))
print('É um valor numérico? ' , var.isnumeric())
print('É um valor alpha? ' , var.isalpha())
print('É um valor decimal? ' , var.isdecimal())
print('É um valor composto por espaços? ' , var.isspace())
