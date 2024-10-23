from Grafo import Grafo 
from Node import Node
from Edge import Edge


# Modelo Gm,n de malla. 
def grafoMalla(m, n, dirigido = False):
    """
    Genera grafo de malla
    :param m: número de columnas (> 1)
    :param n: número de filas (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    G = Grafo() # Crear un grafo vacio

    # Crear nodos
    # Crear m*n nodos
    # for i in range(m*n):
    #   G.addNode(Node(i))

    # V = G.getNodes() # Obtener los nodos del grafo

    # Crear aristas
    # Para el nodo ni,j crear una arista con el nodo ni+1,j y otra con el nodo ni,j+1, para i<m y j<n
    for i in range(m):
      for j in range(n):
        # Creamos un nuevo nodo
        node = Node(i)
        G.addNode(node)
        # Creamos la arista con el nodo ni+1,j
        if i < m-1:
          edge = Edge(V[i], V[(i + 1) * n + j], i)
          G.addEdge(edge)

        # Creamos la arista con el nodo ni,j+1
        if j < n-1:
          edge = Edge(V[i], V[i * n + j + 1], j)
          G.addEdge(edge)
    
    return G

