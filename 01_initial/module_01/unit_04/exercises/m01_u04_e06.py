"""
Ejercicio 6 - Dificultad alta

Cree una función que tome la siguiente lista y reordene de menor a mayor sus componentes:

[7, 3, 44, 21, 78, 5, 56, 9]
"""


def main():
    lista = [7, 3, 44, 21, 78, 5, 56, 9]

    # Ordenamiento por bubujeo
    for _ in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    print(lista)


if __name__ == "__main__":
    main()
