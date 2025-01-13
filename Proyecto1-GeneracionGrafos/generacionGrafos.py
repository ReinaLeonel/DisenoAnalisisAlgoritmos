from Grafo import Grafo
from Algoritmos import *

# def  __init__ ():

# g = grafoMalla(3, 3)
# g = g.saveGraphViz("./grafoMalla.gv")


g = grafoErdosRenyi(3, 3)
g = g.saveGraphViz("grafoErdosRenyi.gv")