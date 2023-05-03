from db.interface import Repository


class MySqlRepository(Repository):

    def insert(self, data) -> None:
        print(f'Inserting {data} on DB MySql')

    def delete(self, data) -> None:
        print(f'Deleting {data} on DB MySql')
