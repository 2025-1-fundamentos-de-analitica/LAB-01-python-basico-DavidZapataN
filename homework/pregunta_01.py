def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0
    with open("files/input/data.csv", "r") as f:
        for linea in f:
            columnas = linea.strip().split("\t")
            suma += int(columnas[1])
    return suma