# Importacion de librerias/Clases
import random

# Clase que representa un nodo/vertice en un grafo -> {v} 
class Node:

    # Constructor de la clase
    def __init__(self, id):
        self.id = id # Identificador del nodo
        self.position = [random.random(), random.random()] # Posicion del nodo en el plano [x,y]
        self.neighbors = [] # Lista de nodos vecinos (Adyacentes)
        self.degV = 0 # Grado del nodo (numero de aristas que estan conectadas al nodo)

    # Metodo que sobre escribe el metodo str
    def __str__(self):
        return str(self.id)

    # # Metodo que agrega una arista al nodo
    # def addEdge(self, edge):
    #     self.edges.append(edge)
    #     self.degV += 1

    # # Metodo que obtiene el grado del nodo
    # def getDegV(self):
    #     return self.degV
    
    # # Metodo que obtiene el id del nodo
    # def getID(self):
    #     id = self.id
    #     return id
    
    # # Metodo que obtiene la posicion del nodo
    # def getPosition(self):
    #     return self.position
