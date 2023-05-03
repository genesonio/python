class PostgressDB:
    
    def __init__(self) -> None:
        self.__connection = 'Postgres'
        
    def connection(self) -> str:
        print('Conectando ao banco Postgres...')
        return self.__connection
    
    def disconnection(self) -> str:
        print('Desconectando ao banco Postgres...')
        return self.__connection