class PessoaA:

    def se_apresentar(self) -> None:
        print('Ola, sou a pessoa A')


class PessoaB(PessoaA):

    def __init__(self) -> None:
        super().__init__()

    def se_apresentar(self) -> None:
        # Quebra do príncípio de Liskov (1988)
        print('Estou alterando esse metodo')


class PessoaC(PessoaB):

    def __init__(self) -> None:
        super().__init__()


pessoa = PessoaA()
pessoa.se_apresentar()  # -> Olá, sou a pessoa A

pessoa2 = PessoaB()
pessoa2.se_apresentar()  # -> Estou alterando esse método
# -> A alteração aqui cria um poliformismo

pessoa3 = PessoaC()
pessoa3.se_apresentar()  # -> Estou alterando esse método ->
# -> Aqui a PessoaC por ter herdado a PessoaB, herda também o polimorfismo
