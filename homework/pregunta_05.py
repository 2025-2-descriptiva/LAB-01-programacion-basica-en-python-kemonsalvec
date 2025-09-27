"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    min_max = {}
    with open ("files/input/data.csv", "r") as file:
        for line in file:
            parts = line.split("\t")
            letter = parts[0]
            number = int(parts[1])
            if letter in min_max:
                current_min, current_max = min_max[letter]
                min_max[letter] = (min(current_min, number), max(current_max, number))
            else:
                min_max[letter] = (number, number) 
    result = [(letter, max_min[1], max_min[0]) for letter, max_min in sorted(min_max.items())]
    return result
    