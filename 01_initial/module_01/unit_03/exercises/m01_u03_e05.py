"""
Ejercicio 5

Suponga que tiene una verdulería y carga la cantidad y el precio de lo comprado por un cliente. Realice un programa que tome de a uno la cantidad y el precio comprado por el cliente y, al finalizar la compra, retorne el monto total gastado.
"""


def main():
    salir_loop = False
    acumulador = 0

    while not salir_loop:
        cantidad = int(input("Ingrese la cantidad: "))
        precio_unitario = float(input("Ingrese el precio: "))

        acumulador += cantidad * precio_unitario
        quiere_salir = input("¿Quiere salir del programa? S/N: ")
        if quiere_salir.capitalize() == "S":
            salir_loop = True

    print(f"El total acumulado es: ${acumulador}")


if __name__ == "__main__":
    main()
