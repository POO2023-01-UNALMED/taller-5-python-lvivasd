from gestion import Mamifero
from gestion import Ave
from gestion import Anfibio
from gestion import Pez
from gestion import Reptil
class Animal:
    _totalAnimales = 0
    _zona = None
    def __init__(self, nombre = "", edad = 0, habitat = "", genero = ""):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero

    @staticmethod
    def totalPorTipo(cls):
        return "Mamiferos: " + Mamifero.cantidadMamiferos() + "\nAves: " + Ave.cantidadAves() + "\nReptiles: " + Reptil.cantidadReptiles() + "\nPeces: " + Pez.cantidadPeces() + "\nAnfibios: " + Anfibio.cantidadAnfibios()
    
    def __str__(self):
        datos = "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero
        if self._zona != None:
            datos += ", la zona en la que me ubico es " + self._zona + ", en el " + self._zona.getZoo()
        
        return datos
    
    def movimiento(self):
        return "desplazarse"
    
    def getTotalAnimales(self):
        return self._totalAnimales
    
    def setTotalAnimales(self, totalAnimales):
        self._totalAnimales = totalAnimales
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona
    
    def setZona(self, zona):
        self._zona = zona
