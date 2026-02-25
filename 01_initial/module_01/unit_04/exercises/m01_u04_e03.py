"""
Ejercicio 4 - Dificultad media

Crear una función lambda que sea equivalente a la siguiente función:

def sumar(valor01, valor02):
    res = valor01 + valor02
    return res
"""


def main():
    sumar_valores = lambda valor01, valor02: valor01 + valor02
    print(sumar_valores(1, 2))


if __name__ == "__main__":
    main()
