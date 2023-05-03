from produto import Produto
from carrinho import Carrinho

car = Carrinho()
mon = Produto('Monitor', 1000)
cerv = Produto('Cerveja', 5)
tv = Produto('TV', 2800)

car.adicionar_produto(cerv)
car.adicionar_produto(mon)
car.adicionar_produto(cerv)
car.adicionar_produto(tv)

car.finalizar()
