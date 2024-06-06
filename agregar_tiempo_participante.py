import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from backend import get_carreras, get_trayectos, get_participantes, add_tiempo_local

def main():
    def agregar_tiempo():
        carrera = combobox_carrera.get()
        trayecto = combobox_trayecto.get()
        competidor = combobox_competidor.get()
        tiempo = entry_tiempo.get()

        # Validación simple de los campos
        if not carrera or not trayecto or not competidor or not tiempo:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos")
            return

        try:
            datetime.strptime(tiempo, "%H:%M:%S")
        except ValueError:
            messagebox.showwarning("Datos inválidos", "Por favor, ingrese un tiempo válido (HH:MM:SS)")
            return
        
        add_tiempo_local(carrera, competidor,trayecto,tiempo)
        messagebox.showinfo("Registro exitoso", f"Tiempo '{tiempo}' registrado correctamente para el competidor '{competidor}' en la carrera '{carrera}' trayecto '{trayecto}'")
        root.destroy()

    root = tk.Tk()
    root.title("Agregar Tiempo a Participante")
    root.geometry("854x480")

    # Etiquetas y entradas para los campos de tiempo
    labels = [
        tk.Label(root, text="Carrera:", font=("Arial", 14)),
        tk.Label(root, text="Trayecto:", font=("Arial", 14)),
        tk.Label(root, text="Competidor:", font=("Arial", 14)),
        tk.Label(root, text="Tiempo (HH:MM:SS):", font=("Arial", 14))
    ]

    # Obtener datos para los combobox
    carreras = [c[0] for c in get_carreras()]
    trayectos = [t[0] for t in get_trayectos()]
    competidores = [p[1] for p in get_participantes()]

    global combobox_carrera, combobox_trayecto, combobox_competidor, entry_tiempo

    combobox_carrera = ttk.Combobox(root, values=carreras, font=("Arial", 14))
    combobox_trayecto = ttk.Combobox(root, values=trayectos, font=("Arial", 14))
    combobox_competidor = ttk.Combobox(root, values=competidores, font=("Arial", 14))
    entry_tiempo = tk.Entry(root, font=("Arial", 14))

    # Empaquetar etiquetas y entradas usando grid
    widgets = [combobox_carrera, combobox_trayecto, combobox_competidor, entry_tiempo]
    for i, (label, widget) in enumerate(zip(labels, widgets)):
        label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
        widget.grid(row=i, column=1, padx=10, pady=5, sticky="w")

    # Botones para registrar y salir
    btn_registrar = tk.Button(root, text="Agregar Tiempo", command=agregar_tiempo, font=("Arial", 18))
    btn_salir = tk.Button(root, text="Salir", command=root.destroy, font=("Arial", 18))

    btn_registrar.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)
    btn_salir.grid(row=len(labels) + 2, column=0, columnspan=2, pady=5)

    root.mainloop()
