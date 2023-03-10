"""
Faça um programa para ler o horário (hora, minuto e segundo) de inicio e a duração,
em segundos, de uma experiência biológica. O programa deve informar o horário (hora, minuto e segundo) de termino da mesma
"""

hora_inicio = int(input('Digite a hora de início da experiência (0-23): '))
minuto_inicio = int(input('Digite o minuto de início da experiência (0-59): '))
segundo_inicio = int(input('Digite o segundo de início da experiência (0-59): '))

duracao = int(input('Digite a duração da experiência em segundos: '))

# Calcula o horário de término
total_segundos = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio + duracao

hora_termino = total_segundos // 3600 % 24
minuto_termino = total_segundos % 3600 // 60
segundo_termino = total_segundos % 60

print(f'A experiência termina às {hora_termino:02d}:{minuto_termino:02d}:{segundo_termino:02d}')
