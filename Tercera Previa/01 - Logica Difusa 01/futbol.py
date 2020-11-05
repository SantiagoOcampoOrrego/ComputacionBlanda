"""

    Lógica Difusa 01

    Santiago Ocampo Orrego - Código: 1004679255

    Ejemplo Futbol

    Cambios: - He modificado el diseño y la posición de las etiquetas

"""

# Paquetes requeridos

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

# Definiendo los rangos de velocidad de 0 a 80
x = np.arange(30, 80, 0.1)

# Definiendo las funciones de miembro triangulares
lento = sk.trimf(x, [30, 30, 50])
medio = sk.trimf(x, [30, 50, 70])
medio_rapido = sk.trimf(x, [50, 60, 80])
rapido = sk.trimf(x, [60, 80, 80])

# Dibujando las funciones de membresía
plt.figure()
plt.plot(x, rapido, 'b', linewidth=1.5, label='Rápido')
plt.plot(x, medio_rapido, 'k', linewidth=1.5, label='Medio-Rápido')
plt.plot(x, medio, 'm', linewidth=1.5, label='Medio')
plt.plot(x, lento, 'r', linewidth=1.5, label='Lento')
plt.title('Penalti Difuso')
plt.ylabel('Membresía')
plt.xlabel('Velocidad (Kilometros Por Hora)')
plt.legend(loc='best', fancybox=True, shadow=True)

plt.show()