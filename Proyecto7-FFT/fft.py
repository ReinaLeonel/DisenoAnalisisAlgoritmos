# Programa que realiza la transformada rapida de fourier con el metodo divide y venceras

# Librerias
import math # Libreria matematica (Para uso de PI, cos, sin)
import wave # Libreria de audio
import matplotlib.pyplot as plt # Libreria para graficar

# Constantes
PI = math.pi

# Funcion que realiza la FFT
# def fft(n, a):
#     """
#     Funcion que realiza la FFT
#     :param n: Tamaño del arreglo
#     :param a: Arreglo de numeros
#     """
#     # Caso base
#     if n == 1:
#         return [a[0]]
    
#     # Se divide el arreglo, en pares e impares
#     even = fft(n//2, a[0::2]) # Pares
#     odd = fft(n//2, a[1::2]) # Impares

#     print(even)
#     print(odd)

#     # Inicializando w y y
#     w = []
#     y = []

#     # for k in range(n):
#     #     # Se calcula la raiz de la unidad
#     #     # w[k] = complex(math.cos(2*PI*k/n), math.sin(2*PI*k/n))
#     #     w.append(complex(math.cos(2*PI*k/n), math.sin(2*PI*k/n)))
#     #     # w[k] = math.cos(2*PI*k/n), 1j*math.sin(2*PI*k/n)

#     for k in range(n):
#         w.insert(k, complex(math.cos(-2*PI*k/n), math.sin(-2*PI*k/n)))

#     # Se realiza la FFT
#     for k in range((n//2)):
#         # Se calcula la raiz de la unidad
#         # w[k] = complex(math.cos(2*PI*k/n), math.sin(2*PI*k/n))
#         # w.insert(k, complex(math.cos(-2*PI*k/n), math.sin(-2*PI*k/n)))

#         # Unimos los pares e impares (Combinar resultados)
#         y.insert(k, even[k] + w[k]*odd[k]) # y[k] = even[k] + w[k]*odd[k]
#         y.insert(k + n//2, even[k] - w[k]*odd[k]) #y[k + n//2] = even[k] - w[k]*odd[k]

#     return y

def fft(n, a):
    # Caso base
    if n == 1:
        return [a[0]]
    
    # Se divide el arreglo, en pares e impares
    even = fft(n//2, a[0::2]) # Pares
    odd = fft(n//2, a[1::2]) # Impares

    print(even)
    print(odd)

    # Inicializando w y y
    w = []
    y = [0]*n

    # Se realiza la FFT
    for k in range((n//2)):
        # Se calcula la raiz de la unidad
        w.append(complex(math.cos(-2*PI*k/n), math.sin(-2*PI*k/n)))
        # Unimos los pares e impares (Combinar resultados)
        y[k] = even[k] + w[k]*odd[k]
        y[k + n//2] = even[k] - w[k]*odd[k]

    return y

# Funcion que lee archivo de audio
def readAudioFile(file):
    """
    Funcion que lee un archivo de audio
    :param file: Archivo de audio
    :return: Arreglo de frames
    """
    # Se abre el archivo
    audio = wave.open(file, 'r')

    # Se obtienen los parametros del archivo
    params = audio.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]

    # Se lee el archivo
    frames = audio.readframes(nframes * nchannels)
    out = []

    # Se obtienen los valores de los frames
    for i in range(0, len(frames), 2):
        low = frames[i]
        high = frames[i + 1]
        value = (high * 256) + low # Es 256 porque es 2^8 para hacer un desplazamiento de 8 bits a la izquierda
        out.append(value)

    return out

# Funcion para obtener las frecuencias
def getFrequencies(audio):
    """
    Funcion que obtiene las frecuencias
    :param audio: Audio
    """
    n = len(audio)
    print("n: ", n)
    trf = fft(n, audio)
    abFFT = abs(trf)
    absFFT = abFFT[:n//2] # Se toma la mitad de los valores
    return absFFT

# Funcion para graficar las frecuencias
def plotFrequencies(frames, frequencies):
    """
    Funcion que grafica las frecuencias
    :param frequencies: Frecuencias
    """
    F = (frames/len(frames))
    fig, ax = plt.subplots()
    plt.plot(F, frequencies)
    plt.xlabel('Frecuencia(Hz)', frozenset = '14')
    plt.ylabel('Amplitud FFT', frozenset = '14')
    plt.show()

# Prueba

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
# n = len(a)
# print(n)
# b = fft(n, a)

# print("---------------------------------------------")
# for B in b:
#     print(B)

# Se lee el archivo de audio
audioFrames = readAudioFile('./Sonidos/swipe.wav')
transformada = fft(len(audioFrames), audioFrames)
# frecuencias = getFrequencies(audioFrames)
# plotFrequencies(audioFrames, frequencies)



# print(audioFrames)
# print(frecuencias)
print(transformada)


