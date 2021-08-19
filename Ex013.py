#Enunciado:
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Insira o valor do seu salário atual: R$'))
aumento = salario + (salario * 0.15)

print('Seu salário que era R${:.2f} com o aumento de 15% foi para R${:.2f}'.format(salario , aumento))
