import tkinter as tk
from tkinter import ttk, messagebox, font

# Definir los colores
BG_COLOR = "#F0F0F0"  # Color de fondo
FG_COLOR = "#333333"  # Color de texto
ACCENT_COLOR = "#CCCCCC"  # Color de acento

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
        self.competidores = [
            Competidor(1, "Juan Pérez", 30, "M", 101, "M30-39"),
            Competidor(2, "Ana Gómez", 35, "F", 102, "F30-39")
        ]
        
        self.root = root
        self.root.title("Menú de Competidores")
        self.root.geometry("600x400")
        self.root.configure(bg=BG_COLOR)  # Establecer el color de fondo de la ventana principal

        self.font = font.Font(size=12)
        self.menu_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.menu_frame.pack(pady=20)

        tk.Button(self.menu_frame, text="Añadir Competidor", command=self.añadir_competidor, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X)
        tk.Button(self.menu_frame, text="Listar Competidores", command=self.listar_competidores, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X)
        tk.Button(self.menu_frame, text="Buscar Competidor", command=self.buscar_competidor, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X)
        tk.Button(self.menu_frame, text="Salir", command=self.root.quit, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X)

    def añadir_competidor(self):
        self.clear_frame()

        frame = tk.Frame(self.root, bg=BG_COLOR)  # Establecer el color de fondo para el nuevo frame
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
            # Obtener los datos del competidor desde las entradas
            id = int(id_entry.get())
            nombre = nombre_entry.get()
            edad = int(edad_entry.get())
            sexo = sexo_entry.get()
            carrera_id = int(carrera_id_entry.get())
            condicion = condicion_entry.get()

            # Verificar que el ID no esté repetido
            id_repetido = False
            for competidor in self.competidores:
                if competidor.id == id:
                    id_repetido = True
                    break

            if id_repetido:
                messagebox.showerror("Error", "El ID ingresado ya está en uso")
            else:
                # Crear el nuevo competidor y agregarlo a la lista
                competidor = Competidor(id, nombre, edad, sexo, carrera_id, condicion)
                self.competidores.append(competidor)
                messagebox.showinfo("Éxito", "Competidor añadido exitosamente")
                self.mostrar_menu()

        def cancelar():
            self.mostrar_menu()

        tk.Button(frame, text="Guardar", command=guardar_competidor, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(frame, text="Cancelar", command=cancelar, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def listar_competidores(self):
        self.clear_frame()

        if self.competidores:
            # Crear Treeview para mostrar la lista de competidores como tabla
            tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Edad", "Sexo", "Carrera ID", "Condición"), show="headings", height=len(self.competidores))
            tree.heading("ID", text="ID")
            tree.heading("Nombre", text="Nombre")
            tree.heading("Edad", text="Edad")
            tree.heading("Sexo", text="Sexo")
            tree.heading("Carrera ID", text="Carrera ID")
            tree.heading("Condición", text="Condición")

            for competidor in self.competidores:
                tree.insert("", "end", values=(competidor.id, competidor.nombre, competidor.edad, competidor.sexo, competidor.carrera_id, competidor.condicion))

            tree.pack(pady=10)

            # Botones de Editar y Borrar
            buttons_frame = tk.Frame(self.root, bg=BG_COLOR)
            buttons_frame.pack()

            def editar_seleccionado():
                # Obtener el competidor seleccionado
                seleccion = tree.selection()
                if seleccion:
                    item = tree.item(seleccion)
                    values = item['values']
                    id_seleccionado = values[0]
                    competidor_seleccionado = None
                    for competidor in self.competidores:
                        if competidor.id == id_seleccionado:
                            competidor_seleccionado = competidor
                            break
                    if competidor_seleccionado:
                        self.editar_competidor(competidor_seleccionado)

            edit_button = tk.Button(buttons_frame, text="Editar", command=editar_seleccionado, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR)
            edit_button.grid(row=0, column=0, padx=(20, 5), pady=10)

            def borrar_seleccionado():
                # Obtener el competidor seleccionado
                seleccion = tree.selection()
                if seleccion:
                    item = tree.item(seleccion)
                    values = item['values']
                    id_seleccionado = values[0]
                    competidor_seleccionado = None
                    for competidor in self.competidores:
                        if competidor.id == id_seleccionado:
                            competidor_seleccionado = competidor
                            break
                    if competidor_seleccionado:
                        self.borrar_competidor(competidor_seleccionado)

            delete_button = tk.Button(buttons_frame, text="Borrar", command=borrar_seleccionado, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR)
            delete_button.grid(row=0, column=1, padx=(5, 20), pady=10)

        else:
            tk.Label(self.root, text="No hay competidores registrados", font=self.font, bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.mostrar_menu, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(pady=10)

    def buscar_competidor(self):
        self.clear_frame()

        tk.Label(self.root, text="Seleccionar Competidor:", font=self.font, bg=BG_COLOR, fg=FG_COLOR).pack()

        # Crear un Combobox
        competidor_combo = ttk.Combobox(self.root, font=self.font, state="readonly", width=30)
        competidor_combo.pack()

        # Obtener los nombres y los IDs de los competidores
        competidor_nombres = [competidor.nombre for competidor in self.competidores]
        competidor_ids = [competidor.id for competidor in self.competidores]

        # Crear una lista de etiquetas de competidores (Nombre - ID)
        competidores_labels = [f"{nombre} - {id}" for nombre, id in zip(competidor_nombres, competidor_ids)]

        # Agregar la lista de etiquetas al Combobox
        competidor_combo["values"] = competidores_labels

        def buscar():
            seleccion = competidor_combo.get()  # Obtener la selección del usuario
            nombre_seleccionado, id_seleccionado = seleccion.split(" - ")  # Separar el nombre del ID
            id_buscar = int(id_seleccionado)
            encontrado = False
            for competidor in self.competidores:
                if competidor.id == id_buscar:
                    messagebox.showinfo("Competidor Encontrado", str(competidor))
                    encontrado = True
                    break
            if not encontrado:
                messagebox.showinfo("No Encontrado", "Competidor no encontrado")
            self.mostrar_menu()

        tk.Button(self.root, text="Buscar", command=buscar, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack()

    def editar_competidor(self, competidor):
        self.clear_frame()

        frame = tk.Frame(self.root, bg=BG_COLOR)  # Establecer el color de fondo para el nuevo frame
        frame.pack(pady=20)

        tk.Label(frame, text="ID:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        id_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        id_entry.grid(row=0, column=1, padx=10, pady=10)
        id_entry.insert(0, competidor.id)

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

        def actualizar_competidor():
            competidor.id = int(id_entry.get())
            competidor.nombre = nombre_entry.get()
            competidor.edad = int(edad_entry.get())
            competidor.sexo = sexo_entry.get()
            competidor.carrera_id = int(carrera_id_entry.get())
            competidor.condicion = condicion_entry.get()
            messagebox.showinfo("Éxito", "Competidor actualizado exitosamente")
            self.mostrar_menu()

        tk.Button(frame, text="Actualizar", command=actualizar_competidor, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def borrar_competidor(self, competidor):
        self.competidores.remove(competidor)
        messagebox.showinfo("Éxito", "Competidor borrado exitosamente")
        self.mostrar_menu()

    def mostrar_menu(self):
        self.clear_frame()
        self.menu_frame.pack(pady=20)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

def main():
    root = tk.Tk()
    root.configure(bg=BG_COLOR)  # Establecer el color de fondo de la ventana principal
    menu = CompetidorMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
