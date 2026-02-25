"""
Ejercicio 2 - Dificultad media

Crear una función lambda que sea equivalente a la siguiente función

def multiplicar_por_tres(valor):
    res = 3 * valor
    return res
"""


def main():
    multiplicar_por_tres = lambda valor: 3 * valor
    print(multiplicar_por_tres(3))


if __name__ == "__main__":
    main()
