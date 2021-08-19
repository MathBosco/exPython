#Enunciado
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

aluno1 = str(input('Insira o nome do Aluno 1: '))
aluno2 = str(input('Insira o nome do Aluno 2: '))
aluno3 = str(input('Insira o nome do Aluno 3: '))
aluno4 = str(input('Insira o nome do Aluno 4: '))

lista = [aluno1 , aluno2 , aluno3 , aluno4]
escolhido = random.choice(lista)

print('O Aluno escolhido foi o: {}'.format(escolhido))
