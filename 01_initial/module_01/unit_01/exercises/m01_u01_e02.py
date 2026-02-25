"""
Ejercicio 2: Automatización con parámetros del sistema

Contexto: Los administradores de sistemas suelen ejecutar scripts pasando datos directamente desde la terminal para ahorrar tiempo.

Requerimiento técnico: Al ejecutar el script desde la terminal, se le deben pasar tres números como parámtros.

Lógica: El programa debe tomar esos parámetros e informar en la terminal cuáles de ellos son múltiplos de dos (números pares).

Desafío profesional: Asegúrate de que tu código siga las normas de estilo PEP8 (espaciado correcto, nombres de variables claros, etc).
"""

from sys import argv


def main(argv):
    is_value_01_even = int(argv[1]) % 2 == 0
    # TODO: CONFIRM IF THIS IS TAUGHT
    print(f"{argv[1]} es {'par' if is_value_01_even else 'impar'}")

    is_value_02_even = int(argv[2]) % 2 == 0
    print(f"{argv[2]} es {'par' if is_value_02_even else 'impar'}")

    is_value_03_even = int(argv[3]) % 2 == 0
    print(f"{argv[3]} es {'par' if is_value_03_even else 'impar'}")


if __name__ == "__main__":
    main(argv)
