# TRATAMENTO DE ERROS
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Você não pode dividir por zero!')
except KeyboardInterrupt:
    print('O usuário preferiou não informar os dados!')
except Exception as error:
    print(f'O erro foi {error.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Obrigado')
