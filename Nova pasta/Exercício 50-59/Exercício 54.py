from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    yb = int(input(f'Data de nascimento da {c}ª pessoa: '))
    if date.today().year - yb >= 21:
        maior += 1
    elif date.today().year - yb < 21:
        menor += 1
print(f"""Neste grupo existem:
{maior} maior(es) de 18 anos.
{menor} menor(es) de 18 anos.""")
