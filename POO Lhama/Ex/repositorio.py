class Repositorio:

    def select(self, db_connection: any) -> None:
        connection = db_connection.connection()
        print(f'Conectei ao banco {connection}')
        print('Fazendo um SELECT * Values....')
        db_connection.disconnection()

    def insert(self, db_connection: any) -> None:
        connection = db_connection.connection()
        print(f'Conectei ao banco {connection}')
        print('Fazendo um INSERT * Values....')
        db_connection.disconnection()
