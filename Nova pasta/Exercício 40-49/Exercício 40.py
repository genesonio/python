from time import sleep
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
m = ( n1 + n2 ) / 2
sleep(1)
if m >= 7.0:
    print(f'Média: {m}')
    print("Parabéns você foi aprovado!")
    print("Aproveite suas férias!")
elif m <= 5.0:
    print(f'Média: {m}')
    print("Você foi reprovado.")
    print("Estude mais no próximo ano!")
else:
    print(f'Média: {m}')
    print("Você está de recuperação.")
    print("Estude para não repetir o ano!")
