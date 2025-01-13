# Programa que realiza la transformada rapida de fourier con el metodo divide y venceras

# Librerias
import math

# Constantes
PI = math.pi

def fft(n, a):
    """
    Funcion que realiza la FFT
    :param n: Tamaño del arreglo
    :param a: Arreglo de numeros
    """
    # Caso base
    if n <= 1:
        return a

    #inicializando variables
    even = []
    odd = []
    
    # Se divide el arreglo, en pares e impares
    even = fft(n//2, a[0::2]) # Pares
    odd = fft(n//2, a[1::2]) # Impares

    print(even)
    print(odd)

    # Inicializando w y y
    w = []
    y = []

    # for k in range(n):
    #     # Se calcula la raiz de la unidad
    #     # w[k] = complex(math.cos(2*PI*k/n), math.sin(2*PI*k/n))
    #     w.append(complex(math.cos(2*PI*k/n), math.sin(2*PI*k/n)))
    #     # w[k] = math.cos(2*PI*k/n), 1j*math.sin(2*PI*k/n)

    # Se realiza la FFT
    for k in range((n//2)-1):
        # Se calcula la raiz de la unidad
        # w[k] = complex(math.cos(2*PI*k/n), math.sin(2*PI*k/n))
        w.insert(k, complex(math.cos(2*PI*k/n), math.sin(2*PI*k/n)))

        # Unimos los pares e impares (Combinar resultados)
        y.insert(k, even[k] + w[k]*odd[k]) # y[k] = even[k] + w[k]*odd[k]
        y.insert(k + n//2, even[k] - w[k]*odd[k]) #y[k + n//2] = even[k] - w[k]*odd[k]

    return y

# Prueba

a = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(a)
b = fft(n, a)
for B in b:
    print(B)