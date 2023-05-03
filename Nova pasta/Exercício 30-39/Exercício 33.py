n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite um terceiro número: '))
lt = [n1, n2, n3]
print (f'O maior número é \033[1;32m{max(lt)}\033[m e o menor é \033[1;31m{min(lt)}\033[m')