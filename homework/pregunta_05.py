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
    valores = {}
    with open("files/input/data.csv", "r") as f:
        for linea in f:
            partes = linea.strip().split("\t")
            letra = partes[0]
            valor = int(partes[1])
            if letra not in valores:
                valores[letra] = []
            valores[letra].append(valor)
    resultado = []
    for letra in sorted(valores.keys()):
        resultado.append((letra, max(valores[letra]), min(valores[letra])))
    return resultado
