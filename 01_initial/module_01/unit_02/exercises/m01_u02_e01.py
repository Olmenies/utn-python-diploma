"""
Ejercicio 1: El validador de parámetros

Contexto: Un script profesional debe validar que los datos recibidos sean correctos antes de procesarlos.

Instrucciones: Retoma el script de la unidad uno que recibía 3 parámetros por terminal usando el módulo sys.

Requerimiento técnico: Utiliza la estructura if/else para verificar si cada número es par o impar

Mejora profesional: Si el usuario no ingresa exactamente tres parámetros, el programa debe mostrar un mensaje de error que diga "Error: Se requieren exactamente 3 argumentos."
"""

from sys import argv


def main(argv: list[str]):
    if len(argv) != 4:
        print(
            f"Error, se requieren exactamente 3 argumentos\nUsted ha ingresado: {len(argv) - 1}"
        )
        return
    else:
        is_value_01_even = int(argv[1]) % 2 == 0
        print(f"{argv[1]} es {'par' if is_value_01_even else 'impar'}")

        is_value_02_even = int(argv[2]) % 2 == 0
        print(f"{argv[2]} es {'par' if is_value_02_even else 'impar'}")

        is_value_03_even = int(argv[3]) % 2 == 0
        print(f"{argv[3]} es {'par' if is_value_03_even else 'impar'}")


if __name__ == "__main__":
    main(argv)
