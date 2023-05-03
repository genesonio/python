f = str(input('Digite uma frase: ')).strip().upper()
print(f'Contém ',f.count('A'),' letras A')
print(f'O primeiro A aparece na posição: ',f.find('A')+1)
print(f'O último A aparece na posição: ',f.rfind('A')+1)