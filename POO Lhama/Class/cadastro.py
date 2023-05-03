class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verify(nome, idade):
            self.__save_user(nome, idade)
        else:
            self.__erro()

    def __verify(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False

    def __save_user(self, nome: str, idade: int) -> None:
        print(f'Cadastrando o Usuário: {nome}, Idade: {idade}')

    def __erro(self) -> None:
        print('Dados inválidos!')


   