import tkinter as tk
from tkinter import ttk, messagebox
from backend import get_carreras
from agregar_carrera import main as agregar_carrera_func
from backend import delete_carrera
import editar_carrera as editar_carrera_func
def actualizar_tabla():
    for i in tree.get_children():
        tree.delete(i)

    carreras = get_carreras()
    for carrera in carreras:
        tree.insert('', tk.END, values=carrera)

def agregar_carrera():
    agregar_carrera_func()
    actualizar_tabla()

def editar_carrera():
    selected_item = tree.selection()
    if selected_item:
        carrera_id = tree.item(selected_item[0])['values'][0]
        editar_carrera_func.editar_carrera_ventana(carrera_id)
        messagebox.showinfo("Editar Carrera", f"Función para editar la carrera con ID {carrera_id}")
        #actualizar_tabla()

def eliminar_carrera():
    selected_item = tree.selection()
    if selected_item:
        carrera_id = tree.item(selected_item[0])['values'][0]
        delete_carrera(carrera_id)
        messagebox.showinfo("La carrera ", f"{carrera_id} se eliminó correctamente")
        actualizar_tabla()

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

    root = tk.Tk()
    root.title("Gestión de Carreras")

    window_width = 1280
    window_height = 480

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    # Crear la tabla
    tree = ttk.Treeview(root, columns=('ID', 'Nombre', 'Fecha', 'Máximo Competidores', 'Lugar', 'Hora de Salida'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Nombre', text='Nombre')
    tree.heading('Fecha', text='Fecha')
    tree.heading('Máximo Competidores', text='Máximo Competidores')
    tree.heading('Lugar', text='Lugar')
    tree.heading('Hora de Salida', text='Hora de Salida')
    tree.bind('<<TreeviewSelect>>', on_tree_select)
    tree.pack(pady=20)

    # Configuración de los botones
    button_font = ("Arial", 14)
    button_width = 20  # Ajusta este valor según sea necesario
    button_height = 2  # Ajusta este valor para hacer los botones más altos

    # Crear los botones
    btn_agregar = tk.Button(root, text='Agregar', command=agregar_carrera, font=button_font, width=button_width, height=button_height)
    btn_agregar.pack(side=tk.LEFT, padx=10, pady=10)

    btn_editar = tk.Button(root, text='Editar', command=editar_carrera, font=button_font, width=button_width, height=button_height, state=tk.DISABLED)
    btn_editar.pack(side=tk.LEFT, padx=10, pady=10)

    btn_eliminar = tk.Button(root, text='Eliminar', command=eliminar_carrera, font=button_font, width=button_width, height=button_height, state=tk.DISABLED)
    btn_eliminar.pack(side=tk.LEFT, padx=10, pady=10)

    btn_salir = tk.Button(root, text='Salir', command=salir, font=button_font, width=button_width, height=button_height)
    btn_salir.pack(side=tk.RIGHT, padx=10, pady=10)

    # Llenar la tabla con los datos de las carreras
    actualizar_tabla()

    root.mainloop()
