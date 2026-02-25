"""
Ejercicio 01: El calculador de presupuestos.

Contexto: Trabajás en una empresa de servicios y necesitás un script para calcular el costo total de un proyecto incluyendo impuestos

Requerimiento técnico: El programa debe multiplicar los dos primeros. sumar el tercero y, al resultado final, aplicarle un icremento del 10% en concepto de gastos administrativos.

Salida esperada: "El presupuesto total final es: $[resultado]"

Estructuras permitidas:
"""


def main():
    value_01 = 10
    value_02 = 50
    value_03 = 100

    result = (value_01 * value_02 + value_03) * 1.1
    print("El presupuesto total final es:", result)


if __name__ == "__main__":
    main()
