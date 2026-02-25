"""
Ejercicio 3

Escriba un programa que consulte al usuario por una oración y comente al usuario cuántas veces aparecen todas las vocales considerando minúsculas, mayúsculas y acentos
"""


def main():
    lista_vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    oracion_ingresada = input("Ingrese una oración: ").lower()
    # TODO: Averiguar si se pude hacer así o si se esperaba el uso de un for-loop
    oracion_filtrada = [item for item in oracion_ingresada if item in lista_vocales]
    cantidad_vocales = len(oracion_filtrada)
    print(cantidad_vocales)


if __name__ == "__main__":
    main()
