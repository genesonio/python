class MysqlDB:

    def __init__(self) -> None:
        self.__connection = 'Mysql'

    def connection(self) -> str:
        print('Conectando ao banco Mysql...')
        return self.__connection

    def disconnection(self) -> str:
        print('Desconectando ao banco Mysql...')
        return self.__connection
