#Enunciado:
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Insira a quantiadade de dias em que alugou o carro: '))
km = float(input('Insira quantos KM foram percorridos com o carro alugado: '))

preco = dias * 60 + km * 0.15

print('O valor total do carro ficou em: R${}'.format(preco))
