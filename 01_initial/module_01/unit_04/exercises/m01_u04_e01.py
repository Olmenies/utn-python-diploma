"""
Ejercicio 1 - Dificultad Baja

Cree una función lambda que compruebe si un número es par o impar
"""


def main():
    es_par = lambda numero: "Es par" if numero % 2 == 0 else "Es impar"
    print(es_par(3))


if __name__ == "__main__":
    main()
