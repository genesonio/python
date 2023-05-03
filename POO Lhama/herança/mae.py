class Mae:

    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.sobrenome = 'Silva'

    def comer(self) -> None:
        print('Estou comendo!')

    def estudar(self) -> None:
        print('Estou estudando!')


class Mae2:

    def __init__(self, something) -> None:
        self.something = something


class Filha(Mae):  # -> Classe filha herda classe Mae

    def __init__(self, endereco) -> None:
        super().__init__(endereco)  # -> Super puxa o __init__ da Mae

    def brincar(self, brinquedo: str) -> None:
        print(f'Estou brincando com {brinquedo}.')


class Neta(Filha):  # -> Herda classe Filha, que herda classe mãe, Neta contém Mae e Filha

    def __init__(self, endereco) -> None:
        super().__init__(endereco)


ana = Mae('Rua Elvira')
clara = Filha('Rua do Bolo')

clara.brincar('Boneca')  # -> Estou brincando com Boneca

clara.estudar()  # -> Estou estudando
print(clara.endereco)  # -> Rua do Bolo
print(ana.endereco)  # -> Rua Elvira


class Filha(Mae2):

    def __init__(self) -> None:
        super().__init__('Olá mundo')


print(clara.something)  # -> Olá mundo
