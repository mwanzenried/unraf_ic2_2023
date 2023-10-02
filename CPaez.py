import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

while True:
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Raíz cuadrada")
    print("6. Elevar al cuadrado")
    print("7. Salir")

    opcion = int(input("Seleccione una operación (1/2/3/4/5/6/7): "))

    if opcion == 7:
        break

    if opcion in [1, 2, 3, 4, 5, 6]:
        if opcion == 5:
            num1 = float(input("Ingrese el número: "))
            if num1 >= 0:
                print("La raíz cuadrada es:", math.sqrt(num1))
            else:
                print("No se puede calcular la raíz cuadrada de un número negativo.")
        elif opcion == 6:
            num1 = float(input("Ingrese el número: "))
            print("El resultado de elevar al cuadrado es:", num1 ** 2)
        else:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == 1:
                print("El resultado de la suma es:", suma(num1, num2))
            elif opcion == 2:
                print("El resultado de la resta es:", resta(num1, num2))
            elif opcion == 3:
                print("El resultado de la multiplicación es:", multiplicacion(num1, num2))
            elif opcion == 4:
                print("El resultado de la división es:", division(num1, num2))
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

