from zooAnimales.animal import Animal
class Ave(Animal):
    _listado = list()
    halcones = 0
    aguilas = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorPlumas = ""):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
    
    def movimiento(self):
        return "volar"
    
    @staticmethod
    def cantidadAves(cls):
        return len(Ave._listado)
    
    @staticmethod
    def crearHalcon(cls, nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")
    
    @staticmethod
    def crearAguila(cls, nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    
    def getListado(self):
        return Ave._listado
    
    def setListado(self, listado):
        Ave._listado = listado

    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    
