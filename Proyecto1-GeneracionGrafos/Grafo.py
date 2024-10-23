#Importando las clases/librerias necesarias
import Edge as Edge
import Node as Node

# Clase que representa un grafo -> {V,E} -> {Nodos,Aristas}
class Grafo:

    edges = [] # Lista de aristas
    nodes = [] # Lista de nodos
    ordenN = 0 # Numero de nodos (orden del grafo)
    ordenE = 0 # Numero de aristas (tamaño del grafo)

    # Constructor de la clase
    def __init__(self):
        self.edges = []
        self.nodes = []

    # Metodo que agrega un nodo al grafo
    def addNode(self, node):
        self.nodes.append(node)
        self.ordenN += 1

    # Metodo que agrega una arista al grafo
    def addEdge(self, edge):
        self.edges.append(edge)
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
        return self.edges
    
    # Metodo que devuelve el grafo en representacion de conjuntos (Con arreglos)
    def getGraph(self):
        return self.nodes, self.edges

    # Metodo que formatiza el grafo en GV
    def getGraphViz(self):
        gv = "digraph G {\n"
        for e in self.edges:
            gv += str(e.getNode0().getID()) + " -> " + str(e.getNode1().getID()) + "\n"
        gv += "}"
        return gv
    
    # Metodo que guarda el grafo en un archivo .gv
    def saveGraphViz(self, filename):
        file = open(filename, "w") 
        file.write(self.getGraphViz())
        file.close()

