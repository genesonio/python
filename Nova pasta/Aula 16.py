lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas ^ são imutáveis.
for comida in lanche:
    print(comida)
# ^ maneira mais simples.
for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida}, na posição {pos}')
    if pos == 1:
        print('OI')
# ^v são o mesmo código escritos de maneira diferente.
for comida in range(0, len(lanche)): # as vezes só esse método funciona.
    print(f'Eu comi {lanche[comida]}, na posição {comida}')
print('Comi pra caramba')
print(sorted(lanche))
print(lanche)

a =  (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(a)
print(b)
print(c)
print(len(c))
print(c.count(5)) # conta quantos (x) tem
print(c.index(8)) # pega o primeiro (x, y) procura o x após y

pessoa = ('Genésio', 23, 'M', 86.30)
# del(tupla) posso deletar a tupla inteira, mas não um item só.
