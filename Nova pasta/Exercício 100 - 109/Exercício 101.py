def voto(ano):
    from datetime import date # Importa só durante a função
    age = date.today().year - ano
    if age < 16:
        return f'Com {age} anos: NÃO VOTA'
    elif age >= 65 or age < 18:
        return f'Com {age} anos: VOTO OPCIONAL'
    else:
        return f'Com {age} anos: VOTO OBRIGATÓRIO'

 # Programa Principal
print(voto(int(input('Em que ano você nasceu? '))))