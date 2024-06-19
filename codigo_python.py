import tkinter as tk
from tkinter import messagebox
import serial

# Configuración de la conexión serie con el Arduino
arduino = serial.Serial('COM4', 9600)   

# Función para convertir un número decimal a binario de 4 bits
def decimal_a_binario(decimal):
    return f"{int(decimal):04b}"

# Función para enviar los datos al Arduino
def enviar_datos(operacion):
    try:
        A = int(entry_A.get())
        B = int(entry_B.get())

        # Convertir los números a binario
        A_bin = decimal_a_binario(A)
        B_bin = decimal_a_binario(B)

        # Preparar el mensaje en el formato operacion + A_bin + B_bin
        mensaje = f"{operacion}{A_bin}{B_bin}\n"

        # Enviar el mensaje al Arduino
        arduino.write(mensaje.encode())

        messagebox.showinfo("Éxito", "Datos enviados correctamente")
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos para A y B")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Practica 2")
ventana.geometry("400x400")
ventana.configure(bg="#f0f0f0")  # Fondo de la ventana

# Centrar los elementos en la ventana
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_rowconfigure(2, weight=1)
ventana.grid_rowconfigure(3, weight=1)
ventana.grid_rowconfigure(4, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# Estilo para las etiquetas
label_style = {"bg": "#f0f0f0", "font": ("Helvetica", 12)}

# Entradas para A y B
tk.Label(ventana, text="Ingrese el valor A:", **label_style).grid(row=0, column=0, pady=10, sticky="e")
entry_A = tk.Entry(ventana, font=("Helvetica", 12))
entry_A.grid(row=0, column=1, pady=10, sticky="w")

tk.Label(ventana, text="Ingrese el valor B:", **label_style).grid(row=1, column=0, pady=10, sticky="e")
entry_B = tk.Entry(ventana, font=("Helvetica", 12))
entry_B.grid(row=1, column=1, pady=10, sticky="w")

# Crear un marco para los botones de operaciones
frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.grid(row=4, column=0, columnspan=2, pady=10)

# Botones de operación
tk.Label(ventana, text="Seleccione operación:", **label_style).grid(row=2, column=0, columnspan=2, pady=10)

# Títulos para las unidades
tk.Label(frame_botones, text="Unidad Aritmética", **label_style).grid(row=0, column=0, pady=5)
tk.Label(frame_botones, text="Unidad Lógica", **label_style).grid(row=0, column=1, pady=5)

# Estilo para los botones
button_style = {"font": ("Helvetica", 12), "bg": "#4CAF50", "fg": "white", "activebackground": "#45a049", "width": 15, "height": 2}

# Lista de operaciones aritméticas y lógicas
operaciones_aritmeticas = [
    ("Suma", "000"),
    ("Resta", "001"),
    ("Multiplicación", "010"),
    ("Potencia", "011")
]

operaciones_logicas = [
    ("XOR", "100"),
    ("OR", "101"),
    ("AND", "110"),
    ("NOT", "111")
]

# Añadir botones de operación aritmética al marco
for i, (text, value) in enumerate(operaciones_aritmeticas):
    tk.Button(frame_botones, text=text, command=lambda val=value: enviar_datos(val), **button_style).grid(row=i+1, column=0, padx=10, pady=5)

# Añadir botones de operación lógica al marco
for i, (text, value) in enumerate(operaciones_logicas):
    tk.Button(frame_botones, text=text, command=lambda val=value: enviar_datos(val), **button_style).grid(row=i+1, column=1, padx=10, pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

