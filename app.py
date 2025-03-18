# App de calculadora

from adicional.operaciones import suma, resta, multiplicacion, division
from adicional.interacciones import saludo, despedida, menu

saludo()

while True:
    menu()
    operaciones = input("Que operacion desea hacer: ")
    if operaciones in ("salir", "5"):
        break

    num1 = int(input("Ingrese su primer numero: "))
    num2 = int(input("Ingrese su segundo numero: "))

    if operaciones == "suma":
        print(suma())
    elif operaciones == "resta":
        print(resta())
    elif operaciones == "multiplicacion":
        print(multiplicacion())
    elif operaciones == "division":
        print(division())
