"""
Ejercicio 7

A partir del ejercicio 5, cree un programa que vaya agregando en un diccionario las compras realizadas.
"""


def main():
    salir_loop = False
    diccionario_compras = {}
    acumulador = 0

    while not salir_loop:
        producto = input("Ingrese el producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        precio_unitario = float(input("Ingrese el precio: "))

        precio = cantidad * precio_unitario

        diccionario_compras[producto] = precio
        acumulador += precio

        quiere_salir = input("¿Quiere salir del programa? S/N: ")
        if quiere_salir.capitalize() == "S":
            salir_loop = True

    print("Listado de compras: ", diccionario_compras, sep="\n")
    print(f"El total acumulado es: ${acumulador}")


if __name__ == "__main__":
    main()
