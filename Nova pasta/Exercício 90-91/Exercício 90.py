aluno = {'Nome': '','Média': '' ,'Situação':'Aprovado'}
aluno['Nome'] = str(input('Nome: ')).capitalize().strip()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação']= 'Recuperação'
print('-'*15)
for k, v in aluno.items():
    print(f'{k} é {v}')
print('-'*15)
