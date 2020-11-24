'''
    Santiago Ocampo Orrego - 1004679255

    Control Difuso API

'''

# Elimina las advertencias que pueden generar las librerias
import warnings
warnings.filterwarnings('ignore')

# Importa el resto de librerias
import numpy as np
import skfuzzy as sk
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

'''
    Se crean los objetos antecedentes y consecuentes a partir de las
    variables del universo y las funciones de membresía
'''
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'Calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'Servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'Propina')

'''
    La población de la función de membresía automática es posible con .automf (3, 5 o 7)
    El 3, 5 o 7 es la cantidad de funciones de membresia que podemos tener
'''
calidad.automf(3)
servicio.automf(3)

'''
    Las funciones de membresía personalizadas se pueden construir interactivamente con la
    API Pythonic
'''
propina['bajo'] = sk.trimf(propina.universe, [0, 0, 13])
propina['medio'] = sk.trimf(propina.universe, [0, 13, 25])
propina['alto'] = sk.trimf(propina.universe, [13, 25, 25])

# Visualización con .view()
calidad['average'].view()
servicio.view()
propina.view()

# Creación de las reglas
regla1 = ctrl.Rule(calidad['poor'] | servicio['poor'], propina['bajo'])
regla2 = ctrl.Rule(servicio['average'], propina['medio'])
regla3 = ctrl.Rule(calidad['good'] | servicio['good'], propina['alto'])

# Visualización de la regla 1
regla1.view()

# Generación del simulador
control_propina = ctrl.ControlSystem([regla1, regla2, regla3])
asignacion_propina = ctrl.ControlSystemSimulation(control_propina)

'''
    Pasar las entradas al ControlSystem usando etiquetas 'Antecedent' con Pythonic API
    Nota: Si se quiere pasar muchas entradas a la vez, usar .inputs(dict_of_data)
'''
asignacion_propina.input['Calidad'] = 6.5
asignacion_propina.input['Servicio'] = 9.8

# Se obtiene el resultado
asignacion_propina.compute()

# Imprime el resultado obtenido
print('Valor de la propina: ')
print(asignacion_propina.output['Propina'])

# Se muestra la curva de asignación de propina
propina.view(sim=asignacion_propina)

plt.show()