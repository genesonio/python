f = str(input('Digite uma frase: ')).strip().upper()
if f.replace(' ', '') == f.replace(' ', '')[::-1]:
    print(f'''A frase:
"{f}"
"{f[::-1]}"
É um palíndromo''')
else:
    print(f'''A frase:
"{f}"
"{f[::-1]}"
não é um palíndromo''')
