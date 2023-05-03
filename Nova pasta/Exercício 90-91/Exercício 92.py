from datetime import date
dados = {'Nome': '', 'Idade': '', 'CTPS': '',
         'Contratação': '', 'Salário': '', 'Aposentadoria': ''}
dados['Nome'] = str(input('Nome: ')).strip().capitalize()
ano = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - ano
dados['CTPS'] = int(input('Carteira de Trabalho [0 não tem]: '))
if dados['CTPS'] > 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Aposentadoria'] = (dados['Contratação'] + 35) - ano
    dados['Salário'] = float(input('Salário: R$ '))
    print(f'{f"Dados da aposentadoria":=^40}')
    for k, v in dados.items():
        print(f'{f" {k} = {v} |":_<40}')
else:
    print(f'''O {dados['Nome']}, tem {dados['Idade']} anos,
E não possui CTPS.''')
