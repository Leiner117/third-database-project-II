import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from backend import get_carrera_by_id, update_carrera

def editar_carrera_ventana(carrera_id):
    carrera = get_carrera_by_id(carrera_id)
    if not carrera:
        messagebox.showerror("Error", "Carrera no encontrada")
        return

    def actualizar_carrera():
        nombre = entry_nombre.get()
        fecha = entry_fecha.get()
        max_competidores = entry_max_competidores.get()
        lugar = entry_lugar.get()
        hora_salida = entry_hora_salida.get()

        if not nombre or not fecha or not max_competidores or not lugar or not hora_salida:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos")
            return

        try:
            datetime.strptime(fecha, "%d-%m-%Y")
            datetime.strptime(hora_salida, "%H:%M")
            int(max_competidores)
        except ValueError:
            messagebox.showwarning("Datos inválidos", "Por favor, ingrese datos válidos (Fecha: DD-MM-YYYY, Hora: HH:MM, Máximo Competidores: Número)")
            return

        update_carrera(carrera_id, nombre, fecha, max_competidores, lugar, hora_salida)
        messagebox.showinfo("Actualización exitosa", f"Carrera '{nombre}' actualizada correctamente")
        editar_carrera_root.destroy()

    editar_carrera_root = tk.Toplevel()
    editar_carrera_root.title("Editar Carrera")
    editar_carrera_root.geometry("854x480")

    # Etiquetas y entradas para los campos de la carrera
    labels = [
        tk.Label(editar_carrera_root, text="Nombre:", font=("Arial", 14)),
        tk.Label(editar_carrera_root, text="Fecha (DD-MM-YYYY):", font=("Arial", 14)),
        tk.Label(editar_carrera_root, text="Máximo Competidores:", font=("Arial", 14)),
        tk.Label(editar_carrera_root, text="Lugar:", font=("Arial", 14)),
        tk.Label(editar_carrera_root, text="Hora de Salida (HH:MM):", font=("Arial", 14))
    ]

    entries = [
        tk.Entry(editar_carrera_root),
        tk.Entry(editar_carrera_root),
        tk.Entry(editar_carrera_root),
        tk.Entry(editar_carrera_root),
        tk.Entry(editar_carrera_root)
    ]

    # Pre-llenar los campos con los datos de la carrera
    entries[0].insert(0, carrera[1])
    entries[1].insert(0, carrera[2])
    entries[2].insert(0, carrera[3])
    entries[3].insert(0, carrera[4])
    entries[4].insert(0, carrera[5])

    # Empaquetar etiquetas usando grid
    for i, label in enumerate(labels):
        label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

    # Empaquetar entradas usando grid
    for i, entry in enumerate(entries):
        entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")

    global entry_nombre, entry_fecha, entry_max_competidores, entry_lugar, entry_hora_salida
    entry_nombre, entry_fecha, entry_max_competidores, entry_lugar, entry_hora_salida = entries

    # Botones para actualizar y salir
    btn_actualizar = tk.Button(editar_carrera_root, text="Actualizar Carrera", command=actualizar_carrera, font=("Arial", 14))
    btn_salir = tk.Button(editar_carrera_root, text="Salir", command=editar_carrera_root.destroy, font=("Arial", 14))

    btn_actualizar.grid(row=len(labels)+1, column=0, columnspan=2, pady=10)
    btn_salir.grid(row=len(labels)+2, column=0, columnspan=2, pady=5)

    editar_carrera_root.mainloop()
