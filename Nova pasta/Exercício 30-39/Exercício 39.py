from datetime import date 
nasc = int(input("Em qual ano você nasceu? "))
anoatual = date.today().year
idade = anoatual - nasc
if idade == 18:
    print('Está na hora de você se alistar no exército.')
elif idade > 18:
    saldo = idade - 18
    print("Já se passaram {} anos desde seu alistamento.".format(saldo))
    ano = anoatual - saldo
    print('Seu alistamento foi em {}'.format(ano))
else:
    saldo = 18 - idade
    print("Você ainda vai se alistar, faltam {} anos para você se alistar".format(saldo))
    ano = anoatual + saldo
    print('Seu alistamento será em {}'.format(ano))