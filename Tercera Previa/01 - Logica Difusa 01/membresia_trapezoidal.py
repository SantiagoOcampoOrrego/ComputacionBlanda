"""

    Lógica Difusa 01

    Santiago Ocampo Orrego - Código: 1004679255

    Membresía Trapezoidal

    Cambios:    - He rediseñado el código para tener todos los cambios en un solo archivo
                - He rediseñado todo el apartado gráfico para mostrar todas las funciones juntas
                - He agregado algunos comentarios extra

"""

# Función de membresía trapezoidal

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

# Creamos varias figuras cambiando algunos parametros para visualizar mejor como funciona la librería skfuzzy
fig, axes = plt.subplots(2)

# Le ponemos un titulo a la figura
fig.suptitle('\nCalidad del Servicio en un Restaurante', fontsize=15)

"""
Ahora vamos a graficar las diferentes funciones cambiando los parametros de calidad para ver
como varia la función dependiendo de estos
"""

#**************************************************************************************************************************

# Se define la variable independiente
x = np.arange(0, 11, 1)

# Se define la variable dependiente trapezoidal de membresía
vd_trapezoidal = sk.trapmf(x, [0, 0, 5, 5])

# Se grafica la función de membresía
axes[0].plot(x, vd_trapezoidal, 'b', linewidth=1.5, label='Servicio')

axes[0].set_ylabel('Membresía')
axes[0].set_xlabel('Nivel de Servicio')
axes[0].legend(loc='best', fancybox=True, shadow=True)

#**************************************************************************************************************************

# Se define la variable independiente
x = np.arange(0, 11, 1)

# Se define la variable dependiente trapezoidal de membresía
vd_trapezoidal = sk.trapmf(x, [0, 3, 5, 8])

# Se grafica la función de membresía
axes[1].plot(x, vd_trapezoidal, 'b', linewidth=1.5, label='Servicio')

axes[1].set_ylabel('Membresía')
axes[1].set_xlabel('Nivel de Servicio')
axes[1].legend(loc='best', fancybox=True, shadow=True)

#**************************************************************************************************************************

# Mostramos todas las graficas
plt.show()