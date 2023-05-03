from time import sleep
valorcasa = float(input('Qual o valor do imóvel? '))
sal = float(input('Qual o seu salário? '))
ano = int(input('Em quantos anos você deseja pagar o imóvel? '))
parc = valorcasa / (ano * 12)
print("Calculando...")
sleep(2)
if parc >= sal * 0.3:
    print("""Seu empréstimo foi negado,
A parcela excede 30% do seu salário.""")
else:
    print("Seu empréstimo foi aceito, sua parcela é de R$ {:.2f}".format(parc))
print('Obrigado pela preferência.')