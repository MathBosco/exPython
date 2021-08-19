#Enunciado
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Insira o valor em metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print('{} metros equivalem a {} centimetros'.format(metros , centimetros))
print('{} metros equivlem a {} milimetros'.format(metros , milimetros))
