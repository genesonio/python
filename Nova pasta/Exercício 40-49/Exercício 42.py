r1 = float(input('Digite a 1ª reta: '))
r2 = float(input('Digite a 2ª reta: '))
r3 = float(input('Digite a 3ª reta: '))
l = [r1, r2, r3]
if (r1+r2+r3-(max(l))) <= max(l):
    print('Não é possível de se fazer um triângulo com estas retas')
else:
    print('As retas acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print("equilátero")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('isóceles')
    else:
        print('escaleno')
