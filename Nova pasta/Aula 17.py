num = [2, 5, 9, 1]
num[2] = 3
num.append(2)
num.insert(2, 0) # y pos x inserido
num.pop() #pop vazio = ultimo x = key
num.sort(reverse=True) # Reverse faz na ordem decresc
num.remove(2) # remove só o primeiro x
print(num)
print(len(num))

valores =[5, 9, 4]
for v in valores:
    print(f'{v} ', end='')

a = [2, 3, 4, 5]
b = a # faz uma ligação
b = a[:] # cria uma cópia ai só (b) recebe 8
b[2] = 8
print(a)
print(b)
"""[2, 3, 8, 5]
[2, 3, 8, 5]"""