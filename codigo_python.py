import tkinter as tk
from tkinter import messagebox
import serial
import pygame


# Configuración de la conexión serie con el Arduino
arduino = serial.Serial('COM4', 9600)

# Inicializar pygame para la reproducción de audio
pygame.init()

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

       
        arduino.write(mensaje.encode())

        # Reproducir el sonido al enviar datos
        pygame.mixer.music.load('sonidopika.mp3')  
        pygame.mixer.music.play()


        messagebox.showinfo("Éxito", "Datos enviados correctamente")
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos para A y B")
    except pygame.error:
        messagebox.showerror("Error", "Error al cargar/reproducir el archivo de sonido MP3")
        
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Práctica 2")
ventana.geometry("850x500")  # Aumentamos el ancho de la ventana
ventana.configure(bg="#f0f0f0")  # Fondo de la ventana

# Centrar los elementos principales en la ventana
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_rowconfigure(2, weight=1)
ventana.grid_rowconfigure(3, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)

# Estilo para las etiquetas y botones
label_style = {"bg": "#f0f0f0", "font": ("Helvetica", 12)}
button_style = {"font": ("Helvetica", 12), "bg": "#4CAF50", "fg": "white", "activebackground": "#45a049", "width": 15, "height": 2}

# Título de la aplicación
tk.Label(ventana, text="LOGIC CALC", font=("Helvetica", 24, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=3, pady=(20, 10))

# Marco para la imagen de Pikachu y el título ALU
frame_pikachu = tk.Frame(ventana, bg="#f0f0f0")
frame_pikachu.grid(row=1, column=2, rowspan=3, padx=20, pady=(20, 0))

# Imagen de Pikachu con título "ALU"
try:
    imagen_alu = tk.PhotoImage(file="pikachu.png").subsample(2, 2)  # Reducimos el tamaño de la imagen
    label_alu = tk.Label(frame_pikachu, image=imagen_alu, bg="#f0f0f0")
    label_alu.grid(row=0, column=0, padx=20, pady=(0, 10), sticky="n")
    tk.Label(frame_pikachu, text="ALU", font=("Helvetica", 16, "bold"), bg="#f0f0f0").grid(row=1, column=0, padx=20, sticky="n")
except tk.TclError:
    # Manejo de error si no se puede cargar la imagen
    tk.Label(frame_pikachu, text="No se pudo cargar la imagen de Pikachu", **label_style, fg="red").grid(row=0, column=0, padx=20, pady=(20, 0), sticky="n")

# Entradas para A y B
tk.Label(ventana, text="Ingrese el valor A:", **label_style).grid(row=1, column=0, pady=10, sticky="e")
entry_A = tk.Entry(ventana, font=("Helvetica", 12))
entry_A.grid(row=1, column=1, pady=10, sticky="w")

tk.Label(ventana, text="Ingrese el valor B:", **label_style).grid(row=2, column=0, pady=10, sticky="e")
entry_B = tk.Entry(ventana, font=("Helvetica", 12))
entry_B.grid(row=2, column=1, pady=10, sticky="w")

# Marco para los botones de operaciones aritméticas y lógicas
frame_botones_aritmetica = tk.Frame(ventana, bg="#f0f0f0")
frame_botones_aritmetica.grid(row=3, column=0, padx=20, pady=(10, 20))

frame_botones_logica = tk.Frame(ventana, bg="#f0f0f0")
frame_botones_logica.grid(row=3, column=1, padx=20, pady=(10, 20))

# Botones de operación aritmética
tk.Label(frame_botones_aritmetica, text="Operaciones Aritméticas", **label_style).grid(row=0, column=0, pady=5, padx=10, sticky="w")
operaciones_aritmeticas = [
    ("Suma", "000"),
    ("Resta", "001"),
    ("Multiplicación", "010"),
    ("Potencia", "011")
]

for i, (text, value) in enumerate(operaciones_aritmeticas):
    tk.Button(frame_botones_aritmetica, text=text, command=lambda val=value: enviar_datos(val), **button_style).grid(row=i+1, column=0, padx=10, pady=5)

# Botones de operación lógica
tk.Label(frame_botones_logica, text="Operaciones Lógicas", **label_style).grid(row=0, column=0, pady=5, padx=10, sticky="w")
operaciones_logicas = [
    ("XOR", "100"),
    ("OR", "101"),
    ("AND", "110"),
    ("NOT", "111")
]

for i, (text, value) in enumerate(operaciones_logicas):
    tk.Button(frame_botones_logica, text=text, command=lambda val=value: enviar_datos(val), **button_style).grid(row=i+1, column=0, padx=10, pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
