"""
Ejercicio 4

Escriba un programa que solicite la edad de la persona e imprima todos los años que la persona ha cumplido
"""


def main():
    ANIO = 2026
    edad_ingresada = int(input("Ingrese su edad: "))
    for anio in range(ANIO - 1, ANIO - edad_ingresada - 1, -1):
        print(anio)


if __name__ == "__main__":
    main()
