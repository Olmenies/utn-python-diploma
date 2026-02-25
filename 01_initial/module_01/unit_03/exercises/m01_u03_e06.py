"""
Ejercicio 6

A partir del ejercicio 5, cree un programa que vaya agregando en una lista las compras realizadas.
"""


def main():
    salir_loop = False
    lista_compras = []
    acumulador = 0

    while not salir_loop:
        cantidad = int(input("Ingrese la cantidad: "))
        precio_unitario = float(input("Ingrese el precio: "))

        precio = cantidad * precio_unitario

        lista_compras.append([cantidad, precio_unitario, precio])
        acumulador += precio

        quiere_salir = input("¿Quiere salir del programa? S/N: ")
        if quiere_salir.capitalize() == "S":
            salir_loop = True

    print("Listado de compras: ", lista_compras, sep="\n")
    print(f"El total acumulado es: ${acumulador}")


if __name__ == "__main__":
    main()
