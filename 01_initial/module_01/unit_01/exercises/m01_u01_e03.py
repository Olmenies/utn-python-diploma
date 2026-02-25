"""
Ejercicio 3: Validador de Insumos

Contexto: Necesitas calcular el área de cobertura de un sensor circular para un sistema de seguridad.

Instrucciones: Escribe un programa que solicite el radio de alcance del sensor.

Cálculo: Provee tanto el perímetro de cobertura como el área total protegida.

Fórmulas a usar:
L = 2 * pi * r
A = pi * r^(2)

Dato técnico:
L = Longitud de perímetro
A = Área
r = Radio
Define pi como una constante 3.1416 dentro de tu código
"""


def main():
    PI = 3.1416
    radio = int(input("Ingresar radio: "))
    length = 2 * PI * radio
    area = PI * radio**2

    print(f"Área de cobertura: {area}")
    print(f"Longitud de cobertura: {length}")


if __name__ == "__main__":
    main()
