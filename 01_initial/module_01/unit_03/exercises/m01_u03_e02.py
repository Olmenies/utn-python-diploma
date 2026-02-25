"""
Ejercicio 2

Escriba un programa que consulte al usuario por una oración y comente al usuario cuántas veces aparece la letra "a"
"""


def main():
    oracion_ingresada = input("Ingrese una oración: ")
    cantidad_a = oracion_ingresada.count("a")
    print(f"Su oración tiene {cantidad_a} letra{'' if cantidad_a == 1 else 's'} 'a'.")


if __name__ == "__main__":
    main()
