""" Funções part 2 """
# 1- Interactive Help
# 2- Docstrings
# 3- Argumentos opcionais
# 4- Escopo de variáveis
# 5- Retorno de resultados

 
            # Interactive Help
# help() <- função

 
            # Docstring
# def contador(i, f, p):
#     """ Conta os números:
#     i = inicio
#     f = final
#     p = passo
#     sem return"""
#     c = i
#     while c <= f:
#         print(f'{c} ', end='')
#         c+=p
#     print('Fim!')

# contador(2, 10, 2)

# help(contador) # contador(i, f, p)
               # Conta os números:
               # i = inicio
               # f = final
               # p = passo
               # sem return

            # Argumentos Opcionais
# def somar(a, b, c=0):
#   """soma a, b e c
#      e printa na tela
#      sem retorno"""
#   s = a + b + c
#   print(f'A soma vale {s}')
#
# 
# somar(3, 2) -> c fica em 0 por default 




#           Escopo de variáveis
# def teste(b): 
#   global a <- Força a substituição da variável global sendo a qualquer variável
#   a = 8
#   b += 4
#   c = 2
#   print(f'A dentro vale {a}') -> A dentro vale 8
#   print(f'B dentro vale {b}') -> B dentro vale 12
#   print(f'C dentro vale {c}') -> C dentro vale 2
#
#
# a = 5 <- Perde o valor devido ao "global [x]"
# print(a) -> 8
# teste(a)
# Se tentar printar b ou c, irá retornar erro pois são variáveis locais, da função teste(b)

#           Retorno de Resultados
# def somar(a=0, b=0, c=0):
#   s = a+b+c
#   return s -> Vai retornar um valor, 
#               então posso por uma variável para receber e armazenar para printar
# 
# 
# r1 = somar(3, 2, 5) -> 10
# r2 = somar(1, 7) -> 8
# r3 = somar(4) -> 4
# print(f'Meus cálculos deram {r1}, {r2} e {r3}')
# Meus cálculos deram 10, 8 e 4

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f1, f2, f3)