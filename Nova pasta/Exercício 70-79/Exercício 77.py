tupla = ('Elefante', 'Abobora', 'Jaca', 'Linguagem', 'Python', 'Curso', 'Banana')
for pal in tupla:
    print(f'\nNa palavra {pal.upper()} temos ', end='')
    for l in pal:
        if l.lower() in 'aeiou':
            print(f"{l.lower()} ", end='')