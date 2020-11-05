"""

    Lógica Difusa 01

    Santiago Ocampo Orrego - Código: 1004679255

    Membresía Gaussiana Bell

    Cambios: - He modificado el diseño y la posición de la etiqueta 'Servicio'

"""

# Función de membresía gaussiana BELL

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

# Se define la variable independiente
x = np.arange(0, 11, 0.6)

# Se define la variable dependiente gaussiana de membresía
vd_gaussiana_bell = sk.gbellmf(x, 2, 3, 5)

# Se grafica la función de membresía
plt.figure()
plt.plot(x, vd_gaussiana_bell, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del Servicio en un Restaurante\n')
plt.ylabel('Membresía')
plt.xlabel('Nivel de Servicio')
plt.legend(loc='best', fancybox=True, shadow=True)

plt.show()