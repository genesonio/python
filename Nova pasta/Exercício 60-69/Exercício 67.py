while True:
    n = int(input('De qual número você deseja saber a tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        x = c * n
        print(f'{c} x {n} = {x}')
