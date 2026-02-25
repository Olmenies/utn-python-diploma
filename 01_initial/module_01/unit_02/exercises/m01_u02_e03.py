"""
Ejercicio 3: Automatización de RRHH

Instrucciones: Realice un programa que consulte la edad del usuario.

Lógica: Si el valor ingresado supera la edad de jubilación (usar 65 años como referencia), presente el mensaje "Ya está en edad de jubilarse". En caso contrario, mostrar "Aún está en edad de trabajar".
"""


def main():
    edad = int(input("Ingrese su edad: "))
    if edad >= 65:
        "Ya está en edad de jubilarse"
    else:
        "Aún está en edad de trabajar"

    return


if __name__ == "__main__":
    main()
