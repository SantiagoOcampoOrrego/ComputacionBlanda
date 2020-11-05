"""

    Lógica Difusa 01

    Santiago Ocampo Orrego - Código: 1004679255

    Membresía Sigmoide

    Cambios: - He modificado el diseño y la posición de la etiqueta 'Servicio'

"""

# Función de membresía sigmoide

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

# Se define la variable independiente
x = np.arange(-11, 11, 1)

# Se define la variable dependiente sigmoide de membresía
vd_sigmoide = sk.sigmf(x, 0, 1)

# Se grafica la función de membresía
plt.figure()
plt.plot(x, vd_sigmoide, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del Servicio en un Restaurante\n')
plt.ylabel('Membresía')
plt.xlabel('Nivel de Servicio')
plt.legend(loc='upper left', fancybox=True, shadow=True)

plt.show()