import tkinter as tk
from tkinter import messagebox

# Funciones de los botones
def registro_competidores():
    messagebox.showinfo("Registro de Competidores", "Función de Registro de Competidores")

def gestion_carreras():
    messagebox.showinfo("Gestión de Carreras", "Función de Gestión de Carreras")

def registro_participantes_tiempos():
    messagebox.showinfo("Registro de Participantes y Tiempos", "Función de Registro de Participantes y Tiempos")

def consultas_reportes():
    messagebox.showinfo("Consultas y Reportes", "Función de Consultas y Reportes")

def salir():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Carreras Atléticas")

# Establecer el tamaño de la ventana
window_width = 854
window_height = 480

# Obtener el tamaño de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular la posición centrada
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Establecer la geometría de la ventana
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Configuración de los botones
button_font = ("Arial", 18)
button_width = 25  # Ajusta este valor según sea necesario

# Crear los botones
btn_registro_competidores = tk.Button(root, text="Registro de Competidores", command=registro_competidores, font=button_font, width=button_width)
btn_gestion_carreras = tk.Button(root, text="Gestión de Carreras", command=gestion_carreras, font=button_font, width=button_width)
btn_registro_participantes = tk.Button(root, text="Registro de Participantes", command=registro_participantes_tiempos, font=button_font, width=button_width)
btn_registro_tiempos = tk.Button(root, text="Registro de Tiempos", command=registro_participantes_tiempos, font=button_font, width=button_width)
btn_consultas_reportes = tk.Button(root, text="Consultas y Reportes", command=consultas_reportes, font=button_font, width=button_width)
btn_salir = tk.Button(root, text="Salir", command=salir, font=button_font, width=button_width)

# Organizar los botones en la ventana
btn_registro_competidores.pack(pady=10)
btn_gestion_carreras.pack(pady=10)
btn_registro_participantes.pack(pady=10)
btn_registro_tiempos.pack(pady=10)
btn_consultas_reportes.pack(pady=10)
btn_salir.pack(pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()
