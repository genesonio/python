from repositorio import Repositorio
from databases import PostgressDB, MysqlDB

db_conn_post = PostgressDB()  # Instanciando
db_conn_mysql = MysqlDB()
repo = Repositorio()

repo.insert(db_conn_post)
print('-'*30)
repo.select(db_conn_mysql)
