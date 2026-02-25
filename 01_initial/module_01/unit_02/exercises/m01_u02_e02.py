"""
Ejercicio 2: Registro de Costos en Listas

Instrucciones: Creá un programa que solicite dos valores numéricos por consola (Por ejemplo: Costo Base y Costo de Envío).

Requerimiento técnico: Debes guardar los datos en una lista siguiendo este orden estructo:
[valor_01, valor_02, la_suma_de_los_valores].

Salida: Presenta la lista resultante en la terminal y una oración que concatene los elementos para darle sentido profesional al reporte.
"""


def main():
    valor_01 = int(input("Ingresar un entero: "))
    valor_02 = int(input("Ingresar otro entero: "))

    lista_resultado = [valor_01, valor_02, valor_01 + valor_02]

    print("[valor_01, valor_02, resultado]", lista_resultado, sep="\n")
    return


if __name__ == "__main__":
    main()
