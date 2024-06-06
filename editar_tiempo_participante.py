import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from backend import update_tiempo_local

def open_editar_tiempo_window(id_carrera, id_trayecto, id_competidor, current_time):
    def editar_tiempo():
        new_time = entry_tiempo.get()

        if not new_time:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos")
            return

        try:
            datetime.strptime(new_time, "%H:%M:%S")
        except ValueError:
            messagebox.showwarning("Datos inválidos", "Por favor, ingrese un tiempo válido (HH:MM:SS)")
            return
        
        update_tiempo_local(id_carrera, id_trayecto, id_competidor, new_time)
        messagebox.showinfo("Actualización exitosa", f"Tiempo actualizado a '{new_time}' para el competidor '{id_competidor}' en la carrera '{id_carrera}' trayecto '{id_trayecto}'")
        root.destroy()

    root = tk.Tk()
    root.title("Editar Tiempo del Participante")
    root.geometry("854x240")

    # Etiquetas y entradas para los campos de tiempo
    labels = [
        tk.Label(root, text="ID Carrera:", font=("Arial", 14)),
        tk.Label(root, text="ID Trayecto:", font=("Arial", 14)),
        tk.Label(root, text="ID Competidor:", font=("Arial", 14)),
        tk.Label(root, text="Tiempo (HH:MM:SS):", font=("Arial", 14))
    ]

    global entry_tiempo

    entry_tiempo = tk.Entry(root, font=("Arial", 14))

    # Preseleccionar los valores actuales (no editables)
    label_carrera = tk.Label(root, text=id_carrera, font=("Arial", 14))
    label_trayecto = tk.Label(root, text=id_trayecto, font=("Arial", 14))
    label_competidor = tk.Label(root, text=id_competidor, font=("Arial", 14))
    entry_tiempo.insert(0, current_time)

    # Empaquetar etiquetas y entradas usando grid
    widgets = [label_carrera, label_trayecto, label_competidor, entry_tiempo]
    for i, (label, widget) in enumerate(zip(labels, widgets)):
        label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
        widget.grid(row=i, column=1, padx=10, pady=5, sticky="w")

    # Botones para registrar y salir
    btn_registrar = tk.Button(root, text="Actualizar Tiempo", command=editar_tiempo, font=("Arial", 18))
    btn_salir = tk.Button(root, text="Salir", command=root.destroy, font=("Arial", 18))

    btn_registrar.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)
    btn_salir.grid(row=len(labels) + 2, column=0, columnspan=2, pady=5)

    root.mainloop()
