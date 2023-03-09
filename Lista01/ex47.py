"""
implemente um programa que calcule o ano de nascimento de uma pessoa apartir de sua idade e o ano atual
"""
ano_atual = int(input('Digite o ano atual: '))
idade = int(input('Digite a idade da pessoa: '))

ano_nascimento = ano_atual - idade

print('A pessoa nasceu em', ano_nascimento)
