"""
Ejercicio 1

Tome el ejercicio de cálculo de números pares e impares de lunidad 2 y agréguele un bucle al código de forma de simplificarlo
"""

from sys import argv


def validar_cantidad_argumentos(argv):
    if len(argv) != 4:
        return False
    else:
        return True


def main(argv):
    son_argumentos_validos = validar_cantidad_argumentos(argv)
    if son_argumentos_validos is not True:
        print(
            f"Error, se requieren exactamente 3 argumentos\nUsted ha ingresado: {len(argv) - 1}"
        )
        return

    for indice in range(1, 4):
        print(f"{argv[indice]} es {'par' if int(argv[indice]) % 2 == 0 else 'impar'}")

    return


if __name__ == "__main__":
    main(argv)
