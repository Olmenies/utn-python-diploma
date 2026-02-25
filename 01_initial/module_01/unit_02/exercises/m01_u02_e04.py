"""
Ejercicio 4: Refactorización a Funciones

Instrucciones: Toma los cálculos de la Unidad 1 (1 y 3) y reescribrlos de forma que la operación principal ocurra dentro de una función.

Objetivo: El programa principal debe llamar a la función, pasarle los argumentos y mostrar el resultado devuelto.
"""


def calcular_area_cobertura(radio, PI):
    return PI * radio**2


def calcular_longitud(radio, PI):
    return 2 * PI * radio


def main():
    PI = 3.1416
    radio = int(input("Ingresar radio: "))
    area = calcular_area_cobertura(radio, PI)
    longitud = calcular_area_cobertura(radio, PI)

    print(f"Área de cobertura: {area}")
    print(f"Longitud de cobertura: {longitud}")


if __name__ == "__main__":
    main()
