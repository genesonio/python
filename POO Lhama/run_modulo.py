from modulos import *

casa_da_ana = Casa()
ana = Pessoa('Ana')

ana.set_local(casa_da_ana)
casa_da_ana.set_proprietario(ana) # Aqui a casa entende quem é seu proprietário

proprietario = casa_da_ana.get_proprietario()
proprietario.se_apresentar() # Casa sabe quem é o proprietário

ana.apresentar_local()
