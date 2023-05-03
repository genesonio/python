class Produto:

    def __init__(self, prod_nome: str, prod_val: int) -> None:
        self.__prod_nome = prod_nome
        self.__prod_val = prod_val

    def inf_prod(self) -> None:
        print(f'Produto: {self.__prod_nome} / Valor: {self.__prod_val}')
