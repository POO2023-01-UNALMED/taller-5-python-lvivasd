from Animal import Animal
class Reptil(Animal):
    _listado = list()
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorEscamas = "", largoCola = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)
    
    def movimiento(self):
        return "reptar"
    
    @staticmethod
    def cantidadReptiles(cls):
        return len(Reptil._listado)
    
    @staticmethod
    def crearIguana(cls, nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)
    
    @staticmethod
    def crearSerpiente(cls, nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    
    def getListado(self):
        return Reptil._listado
    
    def setListado(self, listado):
        Reptil._listado = listado

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
    