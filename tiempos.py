import tkinter as tk
from tkinter import ttk
from backend import get_participantes, get_times_by_participant, delete_tiempo_local
import agregar_tiempo_participante
import editar_tiempo_participante
def actualizar_tiempos():
    corredor_seleccionado = corredor_combobox.get()
    limpiar_tabla()
    tiempos = get_times_by_participant(corredor_seleccionado)
    for tiempo in tiempos:
        tiempos_table.insert("", "end", values=tiempo)

def limpiar_tabla():
    for i in tiempos_table.get_children():
        tiempos_table.delete(i)

def agregar_tiempo():
    agregar_tiempo_participante.main()

def editar_tiempo():
    selected = tiempos_table.selection()
    if selected:
        tiempo_seleccionado = tiempos_table.item(selected[0])["values"]
        id_carrera, id_trayecto, id_competidor, tiempo = tiempo_seleccionado[:4]
        editar_tiempo_participante.open_editar_tiempo_window(id_carrera, id_trayecto, id_competidor, tiempo)
        actualizar_tiempos()

def eliminar_tiempo():
    selected = tiempos_table.selection()
    if selected:
        tiempo_seleccionado = tiempos_table.item(selected[0])["values"]
        id_carrera, id_trayecto, id_competidor = tiempo_seleccionado[:3]
        delete_tiempo_local(id_carrera, id_competidor, id_trayecto)
        actualizar_tiempos()

def habilitar_botones(event):
    selected = tiempos_table.selection()
    if selected:
        editar_btn.config(state=tk.NORMAL)
        eliminar_btn.config(state=tk.NORMAL)
    else:
        editar_btn.config(state=tk.DISABLED)
        eliminar_btn.config(state=tk.DISABLED)

def main():
    global root, corredor_combobox, tiempos_table, editar_btn, eliminar_btn

    root = tk.Tk()
    root.title("Agregar tiempos")
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
    
    participantes = get_participantes()
    ids_competidores = [p[2] for p in participantes]

    corredor_label = tk.Label(root, text="ID de Corredor:", font=("Arial", 14))
    corredor_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    corredor_combobox = ttk.Combobox(root, values=ids_competidores, font=("Arial", 14))
    corredor_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    corredor_combobox.current(0)
    corredor_combobox.bind("<<ComboboxSelected>>", lambda event: actualizar_tiempos())

    tiempos_table = ttk.Treeview(root, columns=("id_carrera", "id_trayecto", "id_competidor", "tiempo"), show="headings")
    tiempos_table.heading("id_carrera", text="ID Carrera")
    tiempos_table.heading("id_trayecto", text="ID Trayecto")
    tiempos_table.heading("id_competidor", text="ID Competidor")
    tiempos_table.heading("tiempo", text="Tiempo")
    tiempos_table.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    tiempos_table.bind("<<TreeviewSelect>>", habilitar_botones)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    boton_frame = tk.Frame(root)
    boton_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    agregar_btn = tk.Button(boton_frame, text="Agregar Tiempo", command=agregar_tiempo, font=("Arial", 14))
    agregar_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    editar_btn = tk.Button(boton_frame, text="Editar Tiempo", command=editar_tiempo, font=("Arial", 14), state=tk.DISABLED)
    editar_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    eliminar_btn = tk.Button(boton_frame, text="Eliminar Tiempo", command=eliminar_tiempo, font=("Arial", 14), state=tk.DISABLED)
    eliminar_btn.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    salir_btn = tk.Button(root, text="Salir", command=root.destroy, font=("Arial", 14))
    salir_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    actualizar_tiempos()

    root.mainloop()

