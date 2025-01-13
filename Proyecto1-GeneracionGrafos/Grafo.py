#Importando las clases/librerias necesarias
# import Edge as Edge
from Node import Node 

# Clase que representa un grafo -> {V,E} -> {Nodos,Aristas}
class Grafo:

    # Constructor de la clase
    def __init__(self, nombre, dirigido = False):
        self.id = nombre
        self.edges = [] # Lista de aristas
        self.nodes = [] # Lista de nodos
        self.ordenN = 0 # Numero de nodos (orden del grafo)
        self.ordenE = 0 # Numero de aristas (tamaño del grafo)
        self.dirigido = dirigido

    # Metodo que agrega un nodo al grafo
    def addNode(self, node):
        """
            Agregar un nodo al grafo
            :param node: nodo a agregar
        """
        # Creamos el nodo si no existe
        if not node in self.nodes:
            nodo = Node(node)
            self.nodes.append(nodo)
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
        conector = " -> " if self.dirigido else " -- " # Asignamos el conector de acuerdo a si es dirigido o no
        gv = "digraph G {\n"
        for e in self.edges:
            gv += str(e.getNode0().id) + conector + str(e.getNode1().id) + "\n"
        gv += "}"
        return gv
    
    # Metodo que guarda el grafo en un archivo .gv
    def saveGraphViz(self, filename):
        ruta = "./GrafosGV/" + filename
        file = open(ruta, "w") 
        file.write(self.getGraphViz())
        file.close()

