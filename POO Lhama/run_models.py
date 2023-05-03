from Models import *

class RepositorioFaker(Repositorio):
    
    def __init__(self) -> None:
        super().__init__()
        
    def select(self, name: int) -> None:
        return None

repo = RepositorioFaker()
inser = Insersor(repo)

data = inser.inserir_dado('Genésio', 23)
print(data)
