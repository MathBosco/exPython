#Enunciado:
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Insira a temperatura em grau Celsius: '))
fahrenheit = (celsius * 9/5) + 32 

print('A temperatura em Fahrenheit é: {} °F'.format(fahrenheit))
