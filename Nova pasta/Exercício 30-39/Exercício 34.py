sal = float(input('Digite seu salário: R$'))
if sal >= 1250:
    print(f'Seu novo salário é \033[1;32m{sal*1.1:.2f}\033[m')
else:
    print(f'Seu novo salário é \033[1;32m{sal*1.15:.2f}\033[m')