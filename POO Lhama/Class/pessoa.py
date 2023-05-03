class Pessoa:  # Substantivo

    def __init__(self, nome: str, idade: int) -> None:
        self.name = nome    # Substantivo
        self.idade = idade  # Substantivo

    def dirigir(self, veiculo: str) -> None:     # Verbos
        print(f'Dirigindo um(a): {veiculo}')

    def cantar(self) -> None:   # Verbos
        print('lalalala')

    def apr_idade(self) -> int:    # Verbos
        return self.idade
