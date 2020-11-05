"""

    Lógica Difusa 01

    Santiago Ocampo Orrego - Código: 1004679255

    Membresía Gaussiana

    Cambios: - He modificado el diseño y la posición de la etiqueta 'Servicio'

"""

# Función de membresía gaussiana

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

# Se define la variable independiente
x = np.arange(0, 11, 0.1)

# Se define la variable dependiente gaussiana de membresía
vd_gaussiana = sk.gaussmf(x, np.mean(x), np.std(x))

# Se grafica la función de membresía
plt.figure()
plt.plot(x, vd_gaussiana, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del Servicio en un Restaurante\n')
plt.ylabel('Membresía')
plt.xlabel('Nivel de Servicio')
plt.legend(loc='upper right', fancybox=True, shadow=True)

plt.show()