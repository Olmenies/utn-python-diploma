"""
Ejercicio 10

Escriba un programa que guarde en una variable una contraseña y consulte al usuario por la contraseña hasta que sea correcta. El programa debe informal al usuario si la contraseña fue correcta o no.
"""

from uuid import uuid4


def main():
    lista_usuarios = [
        {"id": str(uuid4()), "usuario": "olmenies", "contrasenia": "platense1234"}
    ]
    esta_autenticado = False

    while not esta_autenticado:
        intento_usuario = input("Introduzca su usuario: ")
        intento_contrasenia = input("Introduzca su contraseña: ")

        for usuario_registrado in lista_usuarios:
            if (
                usuario_registrado["usuario"] == intento_usuario
                and usuario_registrado["contrasenia"] == intento_contrasenia
            ):
                esta_autenticado = True
                print(f"Bienvenido, {usuario_registrado['usuario']}")
            else:
                print("Error: Contraseña incorrecta")

    return


if __name__ == "__main__":
    main()
