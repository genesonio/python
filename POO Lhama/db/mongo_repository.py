from db.interface import Repository


class MongoRepository(Repository):

    def insert(self, data) -> None:
        print(f'Inserting {data} on DB Mongo')

    def delete(self, data) -> None:
        print(f'Deleting {data} on DB Mongo')
