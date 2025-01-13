# Programa que realiza la transformada rapida de fourier con el metodo divide y venceras

# Librerias
import math
import wave

# Constantes
PI = math.pi

# Funcion que realiza la FFT
def fft(n, a):
    """
    Funcion que realiza la FFT
    :param n: Tamaño del arreglo
    :param a: Arreglo de numeros
    """
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
    y = []

    # for k in range(n):
    #     # Se calcula la raiz de la unidad
    #     # w[k] = complex(math.cos(2*PI*k/n), math.sin(2*PI*k/n))
    #     w.append(complex(math.cos(2*PI*k/n), math.sin(2*PI*k/n)))
    #     # w[k] = math.cos(2*PI*k/n), 1j*math.sin(2*PI*k/n)

    # Se realiza la FFT
    for k in range((n//2)):
        # Se calcula la raiz de la unidad
        # w[k] = complex(math.cos(2*PI*k/n), math.sin(2*PI*k/n))
        w.insert(k, complex(math.cos(-2*PI*k/n), math.sin(-2*PI*k/n)))

        # Unimos los pares e impares (Combinar resultados)
        y.insert(k, even[k] + w[k]*odd[k]) # y[k] = even[k] + w[k]*odd[k]
        y.insert(k + n//2, even[k] - w[k]*odd[k]) #y[k + n//2] = even[k] - w[k]*odd[k]

    return y

# Funcion que lee archivo de audio
def readAudioFile(file):
    """
    Funcion que lee un archivo de audio
    :param file: Archivo de audio
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

# Prueba

# a = [1, 2, 3, 4]
# n = len(a)
# b = fft(n, a)
# print("---------------------------------------------")
# for B in b:
#     print(B)

# Se lee el archivo de audio
audio = readAudioFile('./Sonidos/acoustic.wav')
print(audio)