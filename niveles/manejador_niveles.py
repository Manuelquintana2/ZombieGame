from pygame.locals import *
from niveles.nivel_uno import NivelUno
from niveles.nivel_dos import NivelDos
from niveles.nivel_tres import NivelTres
# from niveles.lores import LoreInicio, LoreEnd


class ManejadorNiveles:
    def __init__(self,pantalla):
        self._slave = pantalla
        self.niveles = {"nivel_uno": NivelUno, "nivel_dos": NivelDos, "nivel_tres": NivelTres
                        # "lore_inicio":LoreInicio, "lore_end":LoreEnd
                        }
           
        
    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)
        
        
        
        
        
        
        