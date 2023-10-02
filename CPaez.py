# Función para realizar una suma
def suma(a, b):
    return a + b

# Función para realizar una resta
def resta(a, b):
    return a - b

# Función para realizar una multiplicación
def multiplicacion(a, b):
    return a * b

# Función para realizar una división
def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

# Menú de opciones
print("Selecciona una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Solicitar la selección del usuario
opcion = input("Ingresa el número de la operación deseada: ")

# Solicitar los números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Realizar la operación seleccionada
if opcion == '1':
    resultado = suma(num1, num2)
    operacion = "suma"
elif opcion == '2':
    resultado = resta(num1, num2)
    operacion = "resta"
elif opcion == '3':
    resultado = multiplicacion(num1, num2)
    operacion = "multiplicación"
elif opcion == '4':
    resultado = division(num1, num2)
    operacion = "división"
else:
    print("Opción no válida")
    resultado = None

# Mostrar el resultado
if resultado is not None:
    print(f"El resultado de la {operacion} es: {resultado}")

#Milei2023
