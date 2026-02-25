"""
Ejercicio 4 - Dificultad alta

Crear una función lambda que tome como parámetro una frase y la escriba al revés.
"""


def main():
    frase = "ab"

    revertir_frase = lambda x: x[::-1]
    print(revertir_frase(frase))


if __name__ == "__main__":
    main()
