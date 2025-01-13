# Clase que representa una arista en un grafo -> {u,v} 
class Edge:

    # Constructor de la clase
    def __init__(self, origen, destino, id):
        self.node0 = origen
        self.node1 = destino
        self.id = id

    # Metodo que sobre escribe el metodo str
    def __str__(self):
        return str(self.id)

    # Metodo para agregar una arista al grafo
    # def addEdge(self, edge):
    #     self.edges.append(edge)
    def addEdge(self, x, y):
        self.node0 = x
        self.node1 = y

    # Metodo que obtiene el nodo origen de la arista
    def getNode0(self):
        return self.node0
    
    # Metodo que obtiene el nodo destino de la arista
    def getNode1(self):
        return self.node1
    
    # Metodo que obtiene el id de la arista
    def getID(self):
        return self.id