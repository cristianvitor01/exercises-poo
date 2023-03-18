"""
6-Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene em uma lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""

notas = []
cont = 0

for i in range(10):
    aluno = []
    for j in range(4):
        aluno.append(float(input('Informe a {}ª nota do {}º aluno: '.format(j+1, i+1))))

    
    media = sum(aluno) / len(aluno)
    notas.append(media)

    if aluno[j] >= 7.0:
        cont += 1

print(f'Número de alunos com média maior ou igual a 7.0: {cont}')
