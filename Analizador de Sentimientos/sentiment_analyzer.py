'''
    Santiago Ocampo Orrego - 1004679255
    Maria Valentina Rojas Pulgarin - 1088346280

    Instalacion:

    Se deben ejecutar los siguientes comandos para instalar las librerias 
    necesarias para el funcionamiento del programa y descargar el corpora

    - pip install nltk
    - pip install textblob
    - pip install matplotlib
    - python -m textblob.download_corpora

    Advertencia:

    El consumo de memoria RAM del programa es de 2gb, el consumo alto se
    debe a la carga de las palabras en memoria

'''

# Importamos las librerias para crear el clasificador
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

""" 
Importamos matplotlib para mostrar en pantalla los
resultados 
"""
import matplotlib.pyplot as plt

""" 
Esta funcion se encarga de almacenar en memoria las palabras para entrenar
el clasificador 
"""
def load_words():
    """ 
    Definimos la ruta de las palabras para entrenar el  clasificador e
    inicializamos la lista para almacenar la informacion
    """
    negative = 'negative_words_es.txt'
    positive = 'positive_words_es.txt'
    train = list()

    # Leemos y cargamos las palabras positivas en memoria
    with open(positive, 'r') as f:
        words = f.read().split()
    
    """ 
    Agregamos las palabras positivas con su respectiva
    calificacion en la lista de entrenamiento
    """
    for word in words:
        train.append((word, 'Positiva'))

    # Leemos y cargamos las palabras negativas en memoria
    with open(negative, 'r') as f:
        words = f.read().split()

    """ 
    Agregamos las palabras negativas con su respectiva
    calificacion en la lista de entrenamiento
    """
    for word in words:
        train.append((word, 'Negativa'))

    return train

def classifier():
    """ 
    Entrenamos el clasificador con las palabras positivas y
    negativas y devolvemos el clasificador
    """
    return NaiveBayesClassifier(load_words())

if __name__ == '__main__':
    """ 
    Creamos el clasificador y una lista para determinar el
    sentimiento medio de la frase 
    """
    cl = classifier()
    sentiments = list()

    # Leemos las frases de prueba
    with open('prueba.txt', 'r') as f:
        sentences = f.read().splitlines()

    """ 
    Clasificamos todas las frases de prueba y almacenamos el
    resultado para establecer un estadistico 
    """
    for sentence in sentences:
        result = cl.classify(sentence)
        sentiments.append(result)
        print(f'{sentence} : {result}')

    # Graficamos los resultados
    x = range(1, len(sentiments) + 1)
    labels = 'Positivas', 'Negativas'
    sizes = [sentiments.count('Positiva'), sentiments.count('Negativa')]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    if sizes[0] > sizes[1]:
        maximum = 'Positivo'
    else:
        maximum = 'Negativo'
    ax.set_title(f'Analisis de sentimientos\nSentimiento más repetido: {maximum} Positivas: {sizes[0]} Negativas: {sizes[1]}')

    plt.show()
