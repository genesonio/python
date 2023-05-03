from time import sleep
from datetime import date
ano = int(input("Qual seu ano de nascimento? "))
idade = date.today().year - ano
sleep(1)
print("Categoria: ", end='')
if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade == 20:
    print("Sênior")
else:
    print("Master")