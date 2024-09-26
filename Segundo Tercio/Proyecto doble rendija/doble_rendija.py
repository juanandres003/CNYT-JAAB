import numpy as np

import matplotlib.pyplot as plt

# Parámetros del experimento
num_rendijas = 2
num_detectores = 1000
amplitud_onda = 1
longitud_onda = 1
distancia_rendijas = 1
distancia_pantalla = 100

# Posiciones de las rendijas
posiciones_rendijas = np.linspace(-distancia_rendijas / 2, distancia_rendijas / 2, num_rendijas)

# Posiciones de los detectores en la pantalla
posiciones_detectores = np.linspace(-50, 50, num_detectores)

# Función para calcular la amplitud en un punto de la pantalla
def calcular_amplitud(x):
    amplitud_total = 0
    for rendija in posiciones_rendijas:
        distancia = np.sqrt((x - rendija) ** 2 + distancia_pantalla ** 2)
        fase = (2 * np.pi / longitud_onda) * distancia
        amplitud_total += amplitud_onda * np.cos(fase)
    return amplitud_total

# Calcular la intensidad en cada punto de la pantalla
intensidades = [calcular_amplitud(x) ** 2 for x in posiciones_detectores]

# Graficar los resultados
plt.plot(posiciones_detectores, intensidades)
plt.title('Experimento de la Doble Rendija')
plt.xlabel('Posición en la pantalla')
plt.ylabel('Intensidad')
plt.show()