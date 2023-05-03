pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
ra = pt +  (10 - 1) * r
for c in range(pt, ra + r, r):
    print(c, end=' > ')
print('Acabou')
