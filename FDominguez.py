# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

# Función principal de la calculadora
def calculadora():
    print("Calculadora Simple")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    # Solicitar al usuario que seleccione una operación
    operacion = input("Por favor, seleccione una operación (1/2/3/4): ")
    
    # Solicitar al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    # Realizar la operación seleccionada
    if operacion == '1':
        print("Resultado: ", sumar(num1, num2))
    elif operacion == '2':
        print("Resultado: ", restar(num1, num2))
    elif operacion == '3':
        print("Resultado: ", multiplicar(num1, num2))
    elif operacion == '4':
        print("Resultado: ", dividir(num1, num2))
    else:
        print("Operación no válida. Por favor, seleccione una operación válida.")

# Llamar a la función principal de la calculadora
calculadora()
