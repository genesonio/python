l = [float(input(f'Qual o peso da {c}ª pessoa: ')) for c in range(1, 6)]
print(f'O maior peso é {max(l):.2f} e o menor peso {min(l):.2f}')
