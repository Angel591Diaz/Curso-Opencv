import math
import matplotlib.pyplot as plt

def media(array):
    sum = 0
    for i in array:
        sum += i
    return sum / len(array)

def mediana(array):
    array.sort()
    if len(array) % 2 == 0: # pair
        return (array[len(array) // 2] + array[len(array) // 2 + 1]) / 2
    else: # odd
        return array[len(array) + 1] / 2

def varianza(array):
    m = media(array)
    n = len(array) - 1
    variance = sum(((x - m) ** 2 ) / n for x in array)
    return variance

def desviacionEstandar(array):
    return math.sqrt(varianza(array))


array = [2.2, 4.1, 3.5, 4.5, 3.2, 3.7, 3.0, 2.6, 3.4, 1.6, 3.1, 3.3, 3.8, 3.1, 4.7, 3.7, 2.5, 4.3, 3.4, 3.6, 2.9, 3.3, 3.9, 3.1, 3.3, 3.1, 3.7, 4.4, 3.2, 4.1, 1.9, 3.4, 4.7, 3.8, 3.2, 2.6, 3.9, 3.9, 4.2, 3.5]
array.sort()

print("Media: ", media(array))
print("Mediana: ", mediana(array))
print("Varianza: ", varianza(array))
print("Desviación estándar: ", desviacionEstandar(array))


plt.hist(array, bins=7, range=(1.5, 4.9))
plt.show()