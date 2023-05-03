n = str(input('Qual seu nome? '))
r = str(input('Qual seu sexo? ')).strip().upper()[0]
while r not in 'MmFf':
    r = str(input('Dados inválidos, informe seu sexo: ')).strip().upper()[0]
print(f'{n}, sexo registrado com sucesso!')