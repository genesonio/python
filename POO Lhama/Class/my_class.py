class MyClass:

    # static = 'Genesio'  # Variável de Classe

    def __init__(self, estado) -> None:
        self.estado = estado
        # Melhor mexer com elementos estáticos, dentro de um atributo ou estado
        self.static = 'Genésio'

    def static_print(self) -> None:
        # aqui funciona pq o self da o contexto ex: (self).static -> (obj1).static
        print(self.static)

    @classmethod
    def static_change(cls):
        # aqui pega o contexto e muda a var na classe, dessa maneira muda para todos os obj ex: (cls).static -> (MyClass).static
        cls.static = 'Programador'


# self define o contexto


obj1 = MyClass(True)
obj2 = MyClass(False)

obj1.static_change()

obj1.static_print()
obj2.static_print()
