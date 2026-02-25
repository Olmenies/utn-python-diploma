"""
Ejercicio 8

A partir del ejercicio 6, cree un programa con 4 funciones:

alta() para dar el alta de la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada
"""

from uuid import uuid4


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

    print(listado_filtrado)
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


def main():
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
        operacion_seleccionada = input("Ingrese la operación a realizar A/B/M/C/S: ")

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


if __name__ == "__main__":
    main()
