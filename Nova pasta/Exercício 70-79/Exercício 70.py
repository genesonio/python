from time import sleep
tot_gast = prod_caro = cont = prod_barato = 0
nom_prod_bar = ''
while True:
    produto = str(input('Qual o nome do produto: ')).strip().lower()
    preço = float(input('Qual o preço do produto: '))
    cont += 1
    tot_gast += preço
    if cont == 1 or preço < prod_barato:
        prod_barato = preço
        nom_prod_bar = produto
    if preço > 1000:
        prod_caro += 1
    perg = str(input('Deseja continuar [S/N]? ')).strip().lower()
    while perg not in 'sn':
        perg = str(input('Deseja continuar [S/N]? ')).strip().lower()
    if perg == 'n':
            break
print(f"""Quantidade de produtos: {cont}
Produto mais barato: {nom_prod_bar} R${prod_barato:.2f}
Produtos acima de RS 1.000,00: {prod_caro:.2f}
Total gasto: R${tot_gast:.2f}""")