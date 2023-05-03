r1 = float(input('Digite a 1ª reta: '))
r2 = float(input('Digite a 2ª reta: '))
r3 = float(input('Digite a 3ª reta: '))
l = [r1, r2, r3]
if (r1+r2+r3-(max(l))) <= max(l):
    print('Não é possível de se fazer um triângulo com estas retas')
else:
    print('É possível de se fazer um triângulo com estas retas')