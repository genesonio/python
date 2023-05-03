from time import sleep
a = int(input('Digite sua altura em centimetos: '))/100
p = float(input('Digite seu peso em kg: '))
imc = p / (a ** 2)
print('\033[1mCalculando...\033[m')
sleep(1)
if imc < 18.5:
    print(f'Seu IMC é \033[1;91m{imc:.2f}\033[m e você está abaixo do peso.')
    print('Procure um nutricionista.')
elif imc <= 25:
    print(f'Seu IMC é \033[1;92m{imc:.2f}\033[m e você está no seu peso ideal.')
    print('Parabéns!')
elif imc <= 30:
    print(f'Seu IMC é \033[1;93m{imc:.2f}\033[m e você está com sobrepeso.')
    print('Procure um nutricionista.')
elif imc < 40:
    print(f'Seu IMC é \033[1;91m{imc:.2f}\033[m e você está com obesidade')
    print('Procure seu médico e um nutricionista.')
elif imc >= 40:
    print(f'Seu IMC é \033[7;91m{imc:.2f}\033[m e você está com obesidade mórbida. ')
    print('\033[1mVocê corre um grave risco de vida, procure um médico!!!')
