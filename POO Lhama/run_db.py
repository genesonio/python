from typing import Type
from db.interface import Repository
from db.mongo_repository import MongoRepository
from db.mysql_repository import MySqlRepository


class Usuario:

    def __init__(self, repository: Type[Repository]) -> None:
        self.__repository = repository

    def armazenar_dado(self, dado: any) -> None:
        self.__repository.insert(dado)

    def remover_dado(self, dado: any) -> None:
        self.__repository.delete(dado)


user = Usuario(MySqlRepository())
user.armazenar_dado(23)

user = Usuario(MongoRepository())
user.armazenar_dado(23)
