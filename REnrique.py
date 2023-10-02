import tkinter as tk

# Función para realizar cálculos
def calcular():
    try:
        resultado.set(eval(entrada.get()))
    except:
        resultado.set("Error")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Variable para mostrar el resultado
resultado = tk.StringVar()

# Crear una entrada de texto
entrada = tk.Entry(ventana, textvariable=resultado, font=("Arial", 20))
entrada.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Crear botones para los números y operadores
botones = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", "C", "=", "/"
]

fila = 1
columna = 0

for boton_texto in botones:
    tk.Button(ventana, text=boton_texto, font=("Arial", 20), width=5, height=2, command=lambda b=boton_texto: entrada.insert(tk.END, b) if b != "=" else calcular()).grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Iniciar la aplicación
ventana.mainloop()
