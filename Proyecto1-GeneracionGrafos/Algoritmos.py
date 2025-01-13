from Grafo import Grafo 
from Node import Node
from Edge import Edge
import random


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

    V = G.getNodes() # Obtener los nodos del grafo

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


# Modelo Gn,m de Erdös y Rényi. Crear n nodos y elegir uniformemente al azar m distintos pares de distintos vértices.
def grafoErdosRenyi(n, m, dirigido = False):
  """
  Genera grafo aleatorio con el modelo Erdos-Renyi
  :param n: número de nodos (> 0)
  :param m: número de aristas (>= n-1)
  :param dirigido: el grafo es dirigido?
  :return: grafo generado
  """
  G = Grafo("ER") # Crear un grafo vacio

  # Crear n nodos
  for i in range(n):
    G.addNode(i)

  V = G.nodes # Obtener los nodos del grafo

  # Crear m aristas al azar
  print(m)
  for i in range(m):
    # Seleccionar al azar dos nodos
    x = random.randrange(0, n)
    y = random.randrange(0, n)
    print(x, y)
    if x == y:
      y = (y + 1) % n
    # Crear arista
    name = "E" + str(i) + ": " + str(x) + "- " + str(y)
    edge = Edge(V[x], V[y], name)
    G.addEdge(edge)
    
  return G  
