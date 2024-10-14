#Importando las clases/librerias necesarias
import Edge as Edge
import Node as Node

# Clase que representa un grafo -> {V,E} -> {Nodos,Aristas}
class Grafo:

    edge = [] # Lista de aristas
    nodes = [] # Lista de nodos
    ordenN = 0 # Numero de nodos (orden del grafo)
    ordenE = 0 # Numero de aristas (tamaño del grafo)

    # Constructor de la clase
    def __init__(self):
        self.edge = []
        self.nodes = []

    # Metodo que agrega un nodo al grafo
    def addNode(self, node):
        self.nodes.append(node)
        self.ordenN += 1

    # Metodo que agrega una arista al grafo
    def addEdge(self, edge):
        self.edge.append(edge)
        self.ordenE += 1

    # Metodo que obtiene el numero de nodos del grafo
    def getOrdenN(self):
        return self.ordenN
    
    # Metodo que obtiene el numero de aristas del grafo
    def getOrdenE(self):
        return self.ordenE
    
    # Metodo que obtiene la lista de nodos del grafo
    def getNodes(self):
        return self.nodes
    
    # Metodo que obtiene la lista de aristas del grafo
    def getEdges(self):
        return self.edge
    
    # Metodo que devuelve el grafo en representacion de conjuntos (Con arreglos)
    def getGraph(self):
        return self.nodes, self.edge
