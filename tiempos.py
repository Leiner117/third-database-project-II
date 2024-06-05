import tkinter as tk
from tkinter import ttk

def actualizar_tiempos():
    corredor_seleccionado = corredor_combobox.get()
    # Limpiar la tabla antes de actualizarla
    limpiar_tabla()
    # Insertar los tiempos correspondientes al corredor seleccionado en la tabla
    for tiempo in corredores_tiempos.get(corredor_seleccionado, []):
        tiempos_table.insert("", "end", values=(corredor_seleccionado, tiempo))

def limpiar_tabla():
    # Limpiar la tabla eliminando todas las filas
    for i in tiempos_table.get_children():
        tiempos_table.delete(i)

def agregar_tiempo():
    pass

def editar_tiempo():
    pass

def eliminar_tiempo():
    pass

root = tk.Tk()
root.title("Agregar tiempos")
root.geometry("854x480")

# Datos de ejemplo de tiempos relacionados con los corredores
corredores_tiempos = {
    "Corredor 1": ["Tiempo 1", "Tiempo 2"],
    "Corredor 2": ["Tiempo 3", "Tiempo 4"],
    "Corredor 3": ["Tiempo 5", "Tiempo 6"],
    "Corredor 4": ["Tiempo 7", "Tiempo 8"],
    "Corredor 5": ["Tiempo 9", "Tiempo 10"],
}

# ComboBox para seleccionar el número de corredor
corredor_label = tk.Label(root, text="Número de Corredor:", font=("Arial", 14))
corredor_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

corredor_combobox = ttk.Combobox(root, values=list(corredores_tiempos.keys()), font=("Arial", 14))
corredor_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="w")
corredor_combobox.current(0)
corredor_combobox.bind("<<ComboboxSelected>>", lambda event: actualizar_tiempos())

# Tabla para mostrar los tiempos
tiempos_table = ttk.Treeview(root, columns=("Corredor", "Tiempo"), show="headings")
tiempos_table.heading("Corredor", text="Corredor")
tiempos_table.heading("Tiempo", text="Tiempo")
tiempos_table.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
# Configurar que las columnas se expandan con el cambio de tamaño de la ventana
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Botones de acción
boton_frame = tk.Frame(root)
boton_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

agregar_btn = tk.Button(boton_frame, text="Agregar Tiempo", command=agregar_tiempo, font=("Arial", 14))
agregar_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

editar_btn = tk.Button(boton_frame, text="Editar Tiempo", command=editar_tiempo, font=("Arial", 14))
editar_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

eliminar_btn = tk.Button(boton_frame, text="Eliminar Tiempo", command=eliminar_tiempo, font=("Arial", 14))
eliminar_btn.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

# Botón de salir
salir_btn = tk.Button(root, text="Salir", command=root.destroy, font=("Arial", 14))
salir_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Mostrar los tiempos relacionados con el primer corredor por defecto
actualizar_tiempos()

root.mainloop()
