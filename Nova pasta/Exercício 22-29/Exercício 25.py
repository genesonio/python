n = str(input('Digite seu nome: ')).strip()
nl = n.title().split()
if 'Silva' in nl:
    print ('{}{}{} contém Silva no seu nome'.format('\033[1;32m', nl[0], '\033[m'))
else:
    print('{}{}{} não contém Silva no seu nome'.format('\033[1;31m', nl[0], '\033[m'))