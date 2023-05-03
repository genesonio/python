class Circo:

    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()


class Malabarista:

    def apresentar_show(self):
        print('Apresentando o malabarista')


class Palhaco:

    def apresentar_show(self):
        print('Apresentando o palhaço')


class Domador:

    def apresentar_show(self):
        print('Apresentando o domador')


circo = Circo()
circo.apresentar(Palhaco())
malabarista = Malabarista()
Circo().apresentar(malabarista)
Circo().apresentar(Domador())
