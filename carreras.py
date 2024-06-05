import tkinter as tk
from tkinter import ttk, messagebox

def agregar_carrera():
    messagebox.showinfo("Agregar Carrera", "Función para agregar una nueva carrera")

def editar_carrera():
    selected_item = tree.selection()
    if selected_item:
        messagebox.showinfo("Editar Carrera", "Función para editar la carrera seleccionada")

def eliminar_carrera():
    selected_item = tree.selection()
    if selected_item:
        messagebox.showinfo("Eliminar Carrera", "Función para eliminar la carrera seleccionada")

def salir():
    root.destroy()

def on_tree_select(event):
    selected_item = tree.selection()
    if selected_item:
        btn_editar.config(state=tk.NORMAL)
        btn_eliminar.config(state=tk.NORMAL)
    else:
        btn_editar.config(state=tk.DISABLED)
        btn_eliminar.config(state=tk.DISABLED)

def main():
    global root, tree, btn_editar, btn_eliminar

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Gestión de Carreras")

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

    # Crear el marco principal
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    # Crear la tabla
    columns = ("ID", "Nombre", "Fecha", "Máximo Competidores", "Lugar", "Hora de Salida")
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    # Configurar las columnas
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor=tk.CENTER)

    tree.pack(fill=tk.BOTH, expand=True)

    # Datos inventados
    carreras = [
        {"ID": 1, "Nombre": "Carrera 1", "Fecha": "2024-06-15", "Máximo Competidores": 100, "Lugar": "Madrid", "Hora de Salida": "09:00"},
        {"ID": 2, "Nombre": "Carrera 2", "Fecha": "2024-06-22", "Máximo Competidores": 150, "Lugar": "Barcelona", "Hora de Salida": "10:00"},
        {"ID": 3, "Nombre": "Carrera 3", "Fecha": "2024-07-01", "Máximo Competidores": 200, "Lugar": "Valencia", "Hora de Salida": "08:00"},
        {"ID": 4, "Nombre": "Carrera 4", "Fecha": "2024-07-10", "Máximo Competidores": 250, "Lugar": "Sevilla", "Hora de Salida": "07:30"},
        {"ID": 5, "Nombre": "Carrera 5", "Fecha": "2024-07-20", "Máximo Competidores": 300, "Lugar": "Bilbao", "Hora de Salida": "09:30"}
    ]

    # Insertar los datos en la tabla
    for carrera in carreras:
        tree.insert('', tk.END, values=(carrera["ID"], carrera["Nombre"], carrera["Fecha"], carrera["Máximo Competidores"], carrera["Lugar"], carrera["Hora de Salida"]))

    # Botones
    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.X, pady=10)

    btn_agregar = tk.Button(button_frame, text="Agregar Carrera", command=agregar_carrera, font=("Arial", 18))
    btn_editar = tk.Button(button_frame, text="Editar Carrera", command=editar_carrera, font=("Arial", 18), state=tk.DISABLED)
    btn_eliminar = tk.Button(button_frame, text="Eliminar Carrera", command=eliminar_carrera, font=("Arial", 18), state=tk.DISABLED)
    btn_salir = tk.Button(button_frame, text="Salir", command=salir, font=("Arial", 18))

    btn_agregar.pack(side=tk.LEFT, padx=10)
    btn_editar.pack(side=tk.LEFT, padx=10)
    btn_eliminar.pack(side=tk.LEFT, padx=10)
    btn_salir.pack(side=tk.RIGHT, padx=10)

    tree.bind("<<TreeviewSelect>>", on_tree_select)

    # Iniciar el bucle principal de la ventana
    root.mainloop()

