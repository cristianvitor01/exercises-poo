"""
Receba a altura do degrau de uma escada e a altura que o usuário
deseja alcançar subindo a escada. Calcule e mostre quantos degraus
o usuário deverá subir para atingir seu objetivo.
"""
alt_degrau = float(input('Digite a altura do degrau em centímetros: '))
alt_desej = float(input('Digite a altura que deseja alcançar em centímetros: '))

qtt_degraus = alt_desej / alt_degrau

print(f'Precisará subir {qtt_degraus:.0f} degraus para atingir seu objetivo.')
