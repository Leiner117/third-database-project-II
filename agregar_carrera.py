import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def agregar_carrera():
    nombre = entry_nombre.get()
    fecha = entry_fecha.get()
    max_competidores = entry_max_competidores.get()
    lugar = entry_lugar.get()
    hora_salida = entry_hora_salida.get()

    # Validación simple de los campos
    if not nombre or not fecha or not max_competidores or not lugar or not hora_salida:
        messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos")
        return

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        datetime.strptime(hora_salida, "%H:%M")
        int(max_competidores)
    except ValueError:
        messagebox.showwarning("Datos inválidos", "Por favor, ingrese datos válidos (Fecha: YYYY-MM-DD, Hora: HH:MM, Máximo Competidores: Número)")
        return

    messagebox.showinfo("Registro exitoso", f"Carrera '{nombre}' registrada correctamente")
    root.destroy()

root = tk.Tk()
root.title("Registrar Carrera")
root.geometry("854x480")

# Etiquetas y entradas para los campos de la carrera
labels = [
    tk.Label(root, text="Nombre:", font=("Arial", 14)),
    tk.Label(root, text="Fecha (YYYY-MM-DD):", font=("Arial", 14)),
    tk.Label(root, text="Máximo Competidores:", font=("Arial", 14)),
    tk.Label(root, text="Lugar:", font=("Arial", 14)),
    tk.Label(root, text="Hora de Salida (HH:MM):", font=("Arial", 14))
]

entries = [
    tk.Entry(root),
    tk.Entry(root),
    tk.Entry(root),
    tk.Entry(root),
    tk.Entry(root)
]

# Empaquetar etiquetas usando grid
for i, label in enumerate(labels):
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

# Empaquetar entradas usando grid
for i, entry in enumerate(entries):
    entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")

# Botones para registrar y salir
btn_registrar = tk.Button(root, text="Registrar Carrera", command="", font=("Arial", 18))
btn_salir = tk.Button(root, text="Salir", command=root.destroy, font=("Arial", 18))

btn_registrar.grid(row=len(labels)+1, column=0, columnspan=2, pady=10)
btn_salir.grid(row=len(labels)+2, column=0, columnspan=2, pady=5)

root.mainloop()

if __name__ == "__main__":
    agregar_carrera()
