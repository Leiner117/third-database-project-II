import tkinter as tk
from tkinter import ttk, messagebox, font
from backend import (
    get_competidores, add_competidor, update_competidor, delete_competidor,
    get_participantes, get_times_by_participant, delete_tiempo_local
)
import agregar_tiempo_participante
import editar_tiempo_participante

# Definir los colores
BG_COLOR = "#F0F0F0"
FG_COLOR = "#333333"
ACCENT_COLOR = "#CCCCCC"

class Competidor:
    def __init__(self, id, nombre, edad, sexo, carrera_id, condicion):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.carrera_id = carrera_id
        self.condicion = condicion

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}, Carrera ID: {self.carrera_id}, Condición: {self.condicion}"

class CompetidorMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú de Competidores")
        self.root.geometry("600x400")
        self.root.configure(bg=BG_COLOR)

        self.font = font.Font(size=12)
        self.menu_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.menu_frame.pack(pady=20)

        tk.Button(self.menu_frame, text="Añadir Competidor", command=self.añadir_competidor, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X)
        tk.Button(self.menu_frame, text="Listar Competidores", command=self.listar_competidores, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X)
        tk.Button(self.menu_frame, text="Buscar Competidor", command=self.buscar_competidor, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X)
        tk.Button(self.menu_frame, text="Salir", command=self.root.quit, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X)

    def añadir_competidor(self):
        self.clear_frame()

        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.pack(pady=20)

        tk.Label(frame, text="ID:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        id_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        id_entry.grid(row=0, column=1, padx=10, pady=10)
        id_entry.insert(0, "Ingrese el ID del competidor")

        tk.Label(frame, text="Nombre:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        nombre_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        nombre_entry.grid(row=1, column=1, padx=10, pady=10)
        nombre_entry.insert(0, "Ingrese el nombre del competidor")

        tk.Label(frame, text="Edad:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        edad_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        edad_entry.grid(row=2, column=1, padx=10, pady=10)
        edad_entry.insert(0, "Ingrese la edad del competidor")

        tk.Label(frame, text="Sexo:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=3, column=0, padx=10, pady=10, sticky="e")
        sexo_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        sexo_entry.grid(row=3, column=1, padx=10, pady=10)
        sexo_entry.insert(0, "Ingrese el sexo del competidor")

        tk.Label(frame, text="Carrera ID:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=4, column=0, padx=10, pady=10, sticky="e")
        carrera_id_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        carrera_id_entry.grid(row=4, column=1, padx=10, pady=10)
        carrera_id_entry.insert(0, "Ingrese el ID de la carrera")

        tk.Label(frame, text="Condición:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=5, column=0, padx=10, pady=10, sticky="e")
        condicion_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        condicion_entry.grid(row=5, column=1, padx=10, pady=10)
        condicion_entry.insert(0, "Ingrese la condición del competidor")

        def guardar_competidor():
            id = int(id_entry.get())
            nombre = nombre_entry.get()
            edad = int(edad_entry.get())
            sexo = sexo_entry.get()
            carrera_id = int(carrera_id_entry.get())
            condicion = condicion_entry.get()

            if add_competidor(id, nombre, edad, sexo, carrera_id, condicion):
                messagebox.showinfo("Éxito", "Competidor añadido exitosamente")
                self.mostrar_menu()
            else:
                messagebox.showerror("Error", "No se pudo añadir el competidor")

        tk.Button(frame, text="Guardar", command=guardar_competidor, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(frame, text="Cancelar", command=self.mostrar_menu, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def listar_competidores(self):
        self.clear_frame()

        competidores = get_competidores()
        if competidores:
            tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Edad", "Sexo", "Carrera ID", "Condición"), show="headings")
            tree.heading("ID", text="ID")
            tree.heading("Nombre", text="Nombre")
            tree.heading("Edad", text="Edad")
            tree.heading("Sexo", text="Sexo")
            tree.heading("Carrera ID", text="Carrera ID")
            tree.heading("Condición", text="Condición")

            for competidor in competidores:
                tree.insert("", "end", values=(competidor.id, competidor.nombre, competidor.edad, competidor.sexo, competidor.carrera_id, competidor.condicion))

            tree.pack(pady=10)

            buttons_frame = tk.Frame(self.root, bg=BG_COLOR)
            buttons_frame.pack()

            def editar_seleccionado():
                seleccion = tree.selection()
                if seleccion:
                    item = tree.item(seleccion)
                    values = item['values']
                    id_seleccionado = values[0]
                    competidor_seleccionado = next((c for c in competidores if c.id == id_seleccionado), None)
                    if competidor_seleccionado:
                        self.editar_competidor(competidor_seleccionado)

            edit_button = tk.Button(buttons_frame, text="Editar", command=editar_seleccionado, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR)
            edit_button.grid(row=0, column=0, padx=(20, 5), pady=10)

            def borrar_seleccionado():
                seleccion = tree.selection()
                if seleccion:
                    item = tree.item(seleccion)
                    values = item['values']
                    id_seleccionado = values[0]
                    competidor_seleccionado = next((c for c in competidores if c.id == id_seleccionado), None)
                    if competidor_seleccionado:
                        self.borrar_competidor(competidor_seleccionado)

            delete_button = tk.Button(buttons_frame, text="Borrar", command=borrar_seleccionado, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR)
            delete_button.grid(row=0, column=1, padx=(5, 20), pady=10)
        else:
            tk.Label(self.root, text="No hay competidores registrados", font=self.font, bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.mostrar_menu, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(pady=5)

    def buscar_competidor(self):
        self.clear_frame()

        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.pack(pady=20)

        tk.Label(frame, text="ID del Competidor:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        id_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        def buscar():
            id = int(id_entry.get())
            competidor = next((c for c in get_competidores() if c.id == id), None)
            if competidor:
                self.editar_competidor(competidor)
            else:
                messagebox.showerror("Error", "Competidor no encontrado")

        tk.Button(frame, text="Buscar", command=buscar, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(frame, text="Cancelar", command=self.mostrar_menu, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def editar_competidor(self, competidor):
        self.clear_frame()

        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.pack(pady=20)

        tk.Label(frame, text="ID:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        id_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        id_entry.grid(row=0, column=1, padx=10, pady=10)
        id_entry.insert(0, competidor.id)
        id_entry.config(state='readonly')

        tk.Label(frame, text="Nombre:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        nombre_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        nombre_entry.grid(row=1, column=1, padx=10, pady=10)
        nombre_entry.insert(0, competidor.nombre)

        tk.Label(frame, text="Edad:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        edad_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        edad_entry.grid(row=2, column=1, padx=10, pady=10)
        edad_entry.insert(0, competidor.edad)

        tk.Label(frame, text="Sexo:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=3, column=0, padx=10, pady=10, sticky="e")
        sexo_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        sexo_entry.grid(row=3, column=1, padx=10, pady=10)
        sexo_entry.insert(0, competidor.sexo)

        tk.Label(frame, text="Carrera ID:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=4, column=0, padx=10, pady=10, sticky="e")
        carrera_id_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        carrera_id_entry.grid(row=4, column=1, padx=10, pady=10)
        carrera_id_entry.insert(0, competidor.carrera_id)

        tk.Label(frame, text="Condición:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=5, column=0, padx=10, pady=10, sticky="e")
        condicion_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        condicion_entry.grid(row=5, column=1, padx=10, pady=10)
        condicion_entry.insert(0, competidor.condicion)

        def guardar_cambios():
            competidor.nombre = nombre_entry.get()
            competidor.edad = int(edad_entry.get())
            competidor.sexo = sexo_entry.get()
            competidor.carrera_id = int(carrera_id_entry.get())
            competidor.condicion = condicion_entry.get()

            if update_competidor(competidor):
                messagebox.showinfo("Éxito", "Competidor actualizado exitosamente")
                self.mostrar_menu()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el competidor")

        tk.Button(frame, text="Guardar", command=guardar_cambios, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(frame, text="Cancelar", command=self.mostrar_menu, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def borrar_competidor(self, competidor):
        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este competidor?"):
            if delete_competidor(competidor.id):
                messagebox.showinfo("Éxito", "Competidor eliminado exitosamente")
                self.mostrar_menu()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el competidor")

    def mostrar_menu(self):
        self.clear_frame()
        self.__init__(self.root)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CompetidorMenu(root)
    root.mainloop()
