"""

    Lógica Difusa 01

    Santiago Ocampo Orrego - Código: 1004679255

    Membresía Triangular

    Cambios:    - He rediseñado el código para tener todos los cambios en un solo archivo
                - He rediseñado todo el apartado gráfico para mostrar todas las funciones juntas
                - He agregado algunos comentarios extra

"""

# Función de membresía triangular

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

# Creamos varias figuras cambiando algunos parametros para visualizar mejor como funciona la librería skfuzzy
fig, axes = plt.subplots(3, 2)

# Le ponemos un titulo a la figura
fig.suptitle('\nCalidad del Servicio en un Restaurante', fontsize=15)

# Se define un array x para el manejo del factor de calidad en un restaurante
x = np.arange(0, 11, 1)

"""
Ahora vamos a graficar las diferentes funciones cambiando los parametros de calidad para ver
como varia la función dependiendo de estos
"""

#**************************************************************************************************************************

# Se define un array para la función de un miembro de tipo triangular
calidad = sk.trimf(x, [0, 0, 0])

# Se grafica la función de membresía
axes[0, 0].plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

axes[0, 0].set_ylabel('Membresía')
axes[0, 0].set_xlabel('Nivel de Servicio')
axes[0, 0].legend(loc='best', fancybox=True, shadow=True)

#**************************************************************************************************************************

# Se define un array para la función de un miembro de tipo triangular
calidad = sk.trimf(x, [0, 0, 5])

# Se grafica la función de membresía
axes[0, 1].plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

axes[0, 1].set_ylabel('Membresía')
axes[0, 1].set_xlabel('Nivel de Servicio')
axes[0, 1].legend(loc='best', fancybox=True, shadow=True)

#**************************************************************************************************************************

# Se define un array para la función de un miembro de tipo triangular
calidad = sk.trimf(x, [0, 5, 10])

# Se grafica la función de membresía
axes[1, 0].plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

axes[1, 0].set_ylabel('Membresía')
axes[1, 0].set_xlabel('Nivel de Servicio')
axes[1, 0].legend(loc='best', fancybox=True, shadow=True)

#**************************************************************************************************************************

# Se define un array para la función de un miembro de tipo triangular
calidad = sk.trimf(x, [9, 9, 10])

# Se grafica la función de membresía
axes[1, 1].plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

axes[1, 1].set_ylabel('Membresía')
axes[1, 1].set_xlabel('Nivel de Servicio')
axes[1, 1].legend(loc='best', fancybox=True, shadow=True)

#**************************************************************************************************************************

# Se define un array para la función de un miembro de tipo triangular
calidad = sk.trimf(x, [10, 10, 10])

# Se grafica la función de membresía
axes[2, 0].plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

axes[2, 0].set_ylabel('Membresía')
axes[2, 0].set_xlabel('Nivel de Servicio')
axes[2, 0].legend(loc='best', fancybox=True, shadow=True)

#**************************************************************************************************************************

# Esta linea borra la ultima gráfica vacia
fig.delaxes(ax=axes[2,1])

# Mostramos todas las graficas
plt.show()