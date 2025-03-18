# App de calculadora

from adicional.operaciones import suma, resta, multiplicacion, division
from adicional.interacciones import saludo, despedida, menu

saludo()

while True:
    menu()
    operaciones = input("Que operacion desea hacer: ")
    if operaciones in ("salir", "5"):
        break

    try:
        num1 = int(input("Ingrese su primer numero: "))
        num2 = int(input("Ingrese su segundo numero: "))
    except ValueError:
        print("Erro, ingrese solo numeros")

    if operaciones in ("suma", "sumar", "+", "1"):
        print(" - - - - - - - - - - - - - - - - - - - -")
        print("Su resultado es: ", suma(num1, num2))
    elif operaciones in ("resta", "restar", "-", "2"):
        print(" - - - - - - - - - - - - - - - - - - - -")
        print("Su resultado es: ", resta(num1, num2))
    elif operaciones in ("multiplicacion", "multiplicar", "*", "3"):
        print(" - - - - - - - - - - - - - - - - - - - -")
        print("Su resultado es: ", multiplicacion(num1, num2))
    elif operaciones in ("division", "dividir", "/", "4"):
        print(" - - - - - - - - - - - - - - - - - - - -")
        print("Su resultado es: ", division(num1, num2))

despedida()
