import tkinter as tk
from tkinter import ttk
import backend

def actualizar_tiempos(orden=None):
    Carrera_seleccionado = Carreras_combobox.get()
    Carrera_tiempos = backend.get_consultaParticipantes_tiempos(Carrera_seleccionado)
    # Limpiar la tabla antes de actualizarla
    limpiar_tabla()
    # Obtener los tiempos correspondientes al corredor seleccionado
    tiempos = Carrera_tiempos.get(Carrera_seleccionado, [])
    # Obtener los participantes y sus tiempos
    for participante_id, tiempos in Carrera_tiempos.items():
        # Ordenar los tiempos si se especifica el orden
        if orden == "ascendente":
            tiempos = sorted(tiempos)
        elif orden == "descendente":
            tiempos = sorted(tiempos, reverse=True)
        # Insertar los tiempos en la tabla
        for tiempo in tiempos:
            tiempos_table.insert("", "end", values=(Carrera_seleccionado, participante_id, tiempo))

def limpiar_tabla():
    # Limpiar la tabla eliminando todas las filas
    for i in tiempos_table.get_children():
        tiempos_table.delete(i)

def ordenar_ascendente():
    actualizar_tiempos(orden="ascendente")

def ordenar_descendente():
    actualizar_tiempos(orden="descendente")

def consultarCarreras():
    global rootConsulta, Carreras_combobox, tiempos_table, Carrera_tiempos
    rootConsulta = tk.Tk()
    rootConsulta.title("Tiempos por carreras")
    rootConsulta.geometry("854x480")
    cursor_local= backend.get_cursor()
    # Obtener la lista de carreras desde la base de datos
    cursor_local.execute("SELECT DISTINCT id_carrera FROM PARTICIPANTES")
    carreras = cursor_local.fetchall()
    carreras = [carrera[0] for carrera in carreras]

    # ComboBox para seleccionar el número de corredor
    corredor_label = tk.Label(rootConsulta, text="Carrera a seleccionar:", font=("Arial", 14))
    corredor_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    Carreras_combobox = ttk.Combobox(rootConsulta, values=carreras, font=("Arial", 14))
    Carreras_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    Carreras_combobox.current(0)
    Carreras_combobox.bind("<<ComboboxSelected>>", lambda event: actualizar_tiempos())

    # Tabla para mostrar los tiempos
    tiempos_table = ttk.Treeview(rootConsulta, columns=("Carrera", "Participante", "Tiempo"), show="headings")
    tiempos_table.heading("Carrera", text="id_Carrera")
    tiempos_table.heading("Participante", text="id_Participante")
    tiempos_table.heading("Tiempo", text="Tiempo")
    tiempos_table.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    # Configurar que las columnas se expandan con el cambio de tamaño de la ventana
    rootConsulta.grid_columnconfigure(0, weight=1)
    rootConsulta.grid_columnconfigure(1, weight=1)

    # Botones de acción
    boton_frame = tk.Frame(rootConsulta)
    boton_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    # Botón de ordenar ascendente
    ascendente_btn = tk.Button(boton_frame, text="Ordenar Ascendente", command=ordenar_ascendente, font=("Arial", 14))
    ascendente_btn.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

    # Botón de ordenar descendente
    descendente_btn = tk.Button(boton_frame, text="Ordenar Descendente", command=ordenar_descendente, font=("Arial", 14))
    descendente_btn.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    # Botón de salir
    salir_btn = tk.Button(rootConsulta, text="Volver", command=rootConsulta.destroy, font=("Arial", 14))
    salir_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    # Mostrar los tiempos relacionados con la primera carrera por defecto
    actualizar_tiempos()
    rootConsulta.mainloop()

def actualizar_tiempos_trayecto(orden=None):
    Carrera_trayecto_seleccionado = Carreras_combobox.get().split("-")
    id_carrera = int(Carrera_trayecto_seleccionado[0].strip())
    id_trayecto = int(Carrera_trayecto_seleccionado[1].strip())
    tiempos = backend.get_participantes_tiempos_por_trayecto(id_carrera, id_trayecto)
    # Limpiar la tabla antes de actualizarla
    limpiar_tabla()
    # Ordenar los tiempos si se especifica el orden
    if orden == "ascendente":
        tiempos = sorted(tiempos, key=lambda x: x[1])
    elif orden == "descendente":
        tiempos = sorted(tiempos, key=lambda x: x[1], reverse=True)
    # Insertar los tiempos en la tabla
    for tiempo in tiempos:
        tiempos_table.insert("", "end", values=(id_carrera, tiempo[0], tiempo[1]))

def consultarTrayectoCarrera():
    global rootTrayectoCarrera, Carreras_combobox, tiempos_table
    rootTrayectoCarrera = tk.Tk()
    rootTrayectoCarrera.title("Tiempos por trayecto de carrera")
    rootTrayectoCarrera.geometry("854x480")
    cursor_local= backend.get_cursor()
    # Obtener la lista de carreras y trayectos desde la base de datos
    cursor_local.execute("SELECT DISTINCT id_carrera, id_trayecto FROM tiempos_participantes")
    carreras_trayectos = cursor_local.fetchall()
    carreras_trayectos = [f"{carrera[0]} - {carrera[1]}" for carrera in carreras_trayectos]

    # ComboBox para seleccionar el trayecto de carrera
    carrera_label = tk.Label(rootTrayectoCarrera, text="Trayecto de carrera a seleccionar:", font=("Arial", 14))
    carrera_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    Carreras_combobox = ttk.Combobox(rootTrayectoCarrera, values=carreras_trayectos, font=("Arial", 14))
    Carreras_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    Carreras_combobox.current(0)
    Carreras_combobox.bind("<<ComboboxSelected>>", lambda event: actualizar_tiempos_trayecto())

    # Tabla para mostrar los tiempos
    tiempos_table = ttk.Treeview(rootTrayectoCarrera, columns=("Carrera", "Participante", "Tiempo"), show="headings")
    tiempos_table.heading("Carrera", text="id_Carrera")
    tiempos_table.heading("Participante", text="id_Participante")
    tiempos_table.heading("Tiempo", text="Tiempo")
    tiempos_table.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    # Configurar que las columnas se expandan con el cambio de tamaño de la ventana
    rootTrayectoCarrera.grid_columnconfigure(0, weight=1)
    rootTrayectoCarrera.grid_columnconfigure(1, weight=1)

    # Botones de acción
    boton_frame = tk.Frame(rootTrayectoCarrera)
    boton_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    # Botón de ordenar ascendente
    ascendente_btn = tk.Button(boton_frame, text="Ordenar Ascendente", command=lambda: actualizar_tiempos_trayecto("ascendente"), font=("Arial", 14))
    ascendente_btn.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

    # Botón de ordenar descendente
    descendente_btn = tk.Button(boton_frame, text="Ordenar Descendente", command=lambda: actualizar_tiempos_trayecto("descendente"), font=("Arial", 14))
    descendente_btn.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    # Botón de salir
    salir_btn = tk.Button(rootTrayectoCarrera, text="Volver", command=rootTrayectoCarrera.destroy, font=("Arial", 14))
    salir_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    # Mostrar los tiempos relacionados con el primer trayecto por defecto
    actualizar_tiempos_trayecto()
    rootTrayectoCarrera.mainloop()


def main():
    root = tk.Tk()
    root.title("Consultas")
    # Establecer el tamaño de la ventana
    window_width = 600
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
    btn_ConsultasCarrera = tk.Button(root, text="Tiempos por Carrera", command=consultarCarreras, font=button_font, width=button_width)
    btn_ConsultasTiemposPorTrayecto = tk.Button(root, text="Tiempos por Trayecto", command=consultarTrayectoCarrera, font=button_font, width=button_width)
    btn_salir = tk.Button(root, text="Salir", command=root.destroy, font=button_font, width=button_width)

    # Organizar los botones en la ventana
    btn_ConsultasCarrera.pack(pady=10)
    btn_ConsultasTiemposPorTrayecto.pack(pady=10)
    btn_salir.pack(pady=10)
