class DatabaseConn:
    
    def __init__(self) -> None:
        self.__database = 'Postgres'
        self._conn = '//connection_string'
        self.user = 'Genésio'
        
    def get_database(self) -> None:
        print(self.__database)
    
    def _testing_connection(self) -> None:
        print('Connection Ok!')
        
class Repository(DatabaseConn):
    
    def __init__(self) -> None:
        super().__init__() # -> Super define herança
        print(self.user) # -> Genésio
        # print(self.__database) # -> Error
        # print(self._conn) # -> "Foda-se a convenção de protegido (Usar mesmo assim)" -> //connection_string
        
    def select(self) -> None:
        self._testing_connection()
        print(f'Connecting to {self._conn}')    
        print('SELECT * From table')
    
db = DatabaseConn()

print(db.user) # -> Genésio
# print(db.__database) # -> Error
print(db._conn) # -> "Foda-se a convenção de protegido (Usar mesmo assim)" -> //connection_string

repo = Repository()

repo.select() # Acessa tudo normalmente, incluindo _conn(_protegido), não acessa __database(__privado)
