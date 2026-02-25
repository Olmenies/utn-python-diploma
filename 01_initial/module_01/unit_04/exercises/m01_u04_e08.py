"""
Ejercicio 8 - Integración del Módulo 1

Consigna: Cree un programa principal que integre la Lógica de Seguridad (Unidad 3) y el Sistema  de Gestión (Unidad 3), organizandolo todo miedante el Menú Profesional (Unidad 4)

Requerimientos técnicos:
1. Al iniciar, el programa debe solicitar la contraseña.
2. Si el acceso es concedido, debe llamar a la función menu_principal()
3. Según la opción elegida en el menú, el programa debe ejecutar la función correspondiente (alta, baja, consulta o modificación)
4. El sistema debe permitir realizar múltiples operaciones hasta que el usuario elija la opción "Salir"
"""

from uuid import uuid4
import os


def alta(listado_compras):
    producto = input("Ingrese el producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio_unitario = float(input("Ingrese el precio: "))

    listado_compras.append(
        {
            "id": str(uuid4()),
            "producto": producto,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
        }
    )


def baja(listado_compras):
    id_producto = input("Ingrese id del producto: ")
    listado_filtrado = []

    for item in listado_compras:
        if item["id"] != id_producto:
            listado_filtrado.append(item)
        else:
            print("Producto borrado satisfactoriamente")

    return listado_filtrado


def consulta(listado_compras):
    acumulador = 0
    print("--- Productos ---")
    for indice, item in enumerate(
        listado_compras
    ):  # TODO: Averiguar si ya se puede usar enumerate
        acumulador += item["precio_unitario"] * item["cantidad"]
        print(f"--- Producto {indice + 1} ---")
        for propiedad in item:
            print(f"\t{propiedad}: {item[propiedad]}")
    print("--------- Totales ---------")
    print(f"\tCantidad de productos: {len(listado_compras)}")
    print(f"\tTotal gastado: {acumulador}")
    print("--------- o ---------")


def modificar(listado_compras):
    id_producto = input("Ingrese id del producto: ")
    listado_filtrado = []

    for item in listado_compras:
        if item["id"] != id_producto:
            listado_filtrado.append(item)
        else:
            nuevo_item = {"id": item["id"]}

            nuevo_item["producto"] = input(
                f"Ingrese nuevo producto (actualmente {item['producto']}): "
            )
            nuevo_item["cantidad"] = int(
                input(f"Ingrese nueva cantidad (actualmente {item['cantidad']}): ")
            )
            nuevo_item["precio_unitario"] = float(
                input(
                    f"Ingrese nuevo precio_unitario (actualmente {item['precio_unitario']}): "
                )
            )

            listado_filtrado.append(nuevo_item)
    return listado_filtrado


def ingresar_app():
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


def menu_principal():
    os.system("cls" if os.name == "nt" else "clear")
    return input("Ingrese la operación a realizar A/B/M/C/S: ")


def main():
    ingresar_app()
    salir_loop = False
    listado_compras = [
        {
            "id": str(uuid4()),
            "producto": "Betta",
            "cantidad": 1,
            "precio_unitario": 2000,
        }
    ]

    while not salir_loop:
        operacion_seleccionada = menu_principal()
        match operacion_seleccionada.capitalize():
            case "A":
                alta(listado_compras)
            case "B":
                listado_compras = baja(listado_compras)
            case "M":
                listado_compras = modificar(listado_compras)
            case "C":
                consulta(listado_compras)
            case "S":
                salir_loop = True
            case _:
                print("Opción inválida")
        input("Presione enter para continuar...")


if __name__ == "__main__":
    main()
