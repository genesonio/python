from interfaces.formas import FormasInterface


class TerrenoRetangulo(FormasInterface):

    def __init__(self, Largura: int, Comprimento: int) -> None:
        self.Largura = Largura
        self.Comprimento = Comprimento

    def get_perimetro(self) -> int:
        perimetro = (self.Comprimento * 2) + (self.Largura * 2)
        return perimetro

    def get_area(self) -> int:
        area = self.Largura * self.Comprimento
        return area
