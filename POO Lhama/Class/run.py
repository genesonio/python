class DatabaseConn:

    def __init__(self) -> None:
        self.__database = 'Postgres'
        self._conn = '//connection_string'
        self.user = 'Lhama'

    def get_database(self) -> None:
        print(self.__database)

    def _testing_connection(self) -> None:
        print('Connection Ok!')

class Repository(DatabaseConn):
    
    def __init__(self) -> None:
        super().__init__()
        # print(self.user)
        # print(self.__database) # Error
        # print(self._conn)

    def select(self) -> None:
        self._testing_connection()
        print(f'connecting to {self._conn}')
        print(f'SELECT * FROM table')

repo = Repository()
repo.select()
