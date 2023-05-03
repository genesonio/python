def notas(*num, sit=False):
    """-> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas do aluno (aceita várias);
    :param sit: Valor opcional, indicado se deve ou não mostrar a situação do aluno;
    :return: Dicionário com todas as informações do aluno."""
    dic = {}
    dic['total'] = len(num)
    dic['maior'] = max(num)
    dic['menor'] = min(num)
    dic['média'] = sum(num) / len(num)
    if sit:
        if dic['média'] >= 7:
            dic['situação'] = 'Aprovado'
        elif dic['média'] >= 5:
            dic['situação'] = 'Recuperação'
        else:   
            dic['situação'] = 'Reprovado'
        return dic
    else:
        return dic

# Programa Principal
resp = notas(7, 5, 6, 10, 10, 3, 10, sit=True)
print(resp)