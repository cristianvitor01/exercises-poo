"""
leia um valor inteiro em segundos e imprima-o em hora, minutos e segundos.
"""
segundos = int(input('Digite um valor inteiro em segundos: '))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(f'{segundos} segundos correspondem a {horas} horas, {minutos} minutos e {segundos_restantes} segundos.')
