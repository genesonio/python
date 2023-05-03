n = int(input("Digite o número inteiro: "))
o = int(input("""Escolha uma opção:
1 - Binário
2 - Octal
3 - Hexadecimal
"""))
if o == 1:
    print("{} em binário é {}".format(n,bin(n)[2:]))
elif o == 2:
    print("{} em octal é {}".format(n, oct(n)[2:]))
elif o == 3:
    print("{} em hexadecimal é {}".format(n, hex(n)[2:]))
else:
    print('Opção invállida, tente novamente.')