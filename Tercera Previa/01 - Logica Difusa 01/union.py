"""

    Lógica Difusa 01

    Santiago Ocampo Orrego - Código: 1004679255

    Ejemplo Unión

    Cambios: - He modificado el diseño y la posición de las etiquetas

"""

# Unión

import skfuzzy as sk
import numpy as np
import matplotlib.pyplot as plt

# Definición de arreglo para calidad
x = np.arange(0, 11, 1)

# Definiendo funciones triangulares
bajo = sk.trimf(x, [0, 0, 5])
medio = sk.trimf(x, [0, 5, 10])

# Graficación
plt.figure()
plt.plot(x, bajo, 'b', linewidth=1.5, label='Bajo')
plt.plot(x, medio, 'r', linewidth=1.5, label='Medio')

# Ajustes gráfico
plt.title('Función Unión (máximo)')
plt.ylabel('Membresía')
plt.xlabel('Velocidad (Kilometros por hora)')
plt.legend(loc='best', fancybox=True, shadow=True)

for i in range(0, 11):
    plt.axvline(x=i, ymin=0, ymax=10, color='g', linestyle='-.')

plt.plot(0, 1, marker='o', markersize=10, color='g')
plt.plot(1, 0.8, marker='o', markersize=10, color='g')
plt.plot(2, 0.6, marker='o', markersize=10, color='g')
plt.plot(3, 0.6, marker='o', markersize=10, color='g')
plt.plot(4, 0.8, marker='o', markersize=10, color='g')
plt.plot(5, 1, marker='o', markersize=10, color='g')

plt.plot(6, 0.8, marker='o', markersize=10, color='g')
plt.plot(7, 0.6, marker='o', markersize=10, color='g')
plt.plot(8, 0.4, marker='o', markersize=10, color='g')
plt.plot(9, 0.2, marker='o', markersize=10, color='g')
plt.plot(10, 0, marker='o', markersize=10, color='g')

plt.show()

# Encontrando el máximo (Fuzzy OR)
print(sk.fuzzy_or(x, bajo, x, medio))