from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangulo import TerrenoRetangulo
from engenheiro import Engenheiro

eng = Engenheiro('Geraldo')
terrQuad = TerrenoQuadrado(4)
terrRet = TerrenoRetangulo(2, 3)

eng.medir_area(terrQuad)
eng.medir_area(terrRet)

eng.medir_perimetro(terrQuad)
eng.medir_perimetro(terrRet)
