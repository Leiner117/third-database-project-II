import tkinter as tk
from tkinter import ttk, messagebox, font

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

        self.font = font.Font(size=12)
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(pady=20)

        tk.Button(self.menu_frame, text="Añadir Competidor", command=self.añadir_competidor, font=self.font).pack(fill=tk.X)
        tk.Button(self.menu_frame, text="Listar Competidores", command=self.listar_competidores, font=self.font).pack(fill=tk.X)
        tk.Button(self.menu_frame, text="Buscar Competidor", command=self.buscar_competidor, font=self.font).pack(fill=tk.X)
        tk.Button(self.menu_frame, text="Salir", command=self.root.quit, font=self.font).pack(fill=tk.X)

    def añadir_competidor(self):
        self.clear_frame()

        tk.Label(self.root, text="ID", font=self.font).pack()
        id_entry = tk.Entry(self.root, font=self.font)
        id_entry.pack()

        tk.Label(self.root, text="Nombre", font=self.font).pack()
        nombre_entry = tk.Entry(self.root, font=self.font)
        nombre_entry.pack()

        tk.Label(self.root, text="Edad", font=self.font).pack()
        edad_entry = tk.Entry(self.root, font=self.font)
        edad_entry.pack()

        tk.Label(self.root, text="Sexo", font=self.font).pack()
        sexo_entry = tk.Entry(self.root, font=self.font)
        sexo_entry.pack()

        tk.Label(self.root, text="Carrera ID", font=self.font).pack()
        carrera_id_entry = tk.Entry(self.root, font=self.font)
        carrera_id_entry.pack()

        tk.Label(self.root, text="Condición Género Edad Trayecto", font=self.font).pack()
        condicion_entry = tk.Entry(self.root, font=self.font)
        condicion_entry.pack()

        def guardar_competidor():
            id = int(id_entry.get())
            nombre = nombre_entry.get()
            edad = int(edad_entry.get())
            sexo = sexo_entry.get()
            carrera_id = int(carrera_id_entry.get())
            condicion = condicion_entry.get()
            competidor = Competidor(id, nombre, edad, sexo, carrera_id, condicion)
            self.competidores.append(competidor)
            messagebox.showinfo("Éxito", "Competidor añadido exitosamente")
            self.mostrar_menu()

        tk.Button(self.root, text="Guardar", command=guardar_competidor, font=self.font).pack()

    def listar_competidores(self):
        self.clear_frame()
        if self.competidores:
            for competidor in self.competidores:
                tk.Label(self.root, text=str(competidor), font=self.font).pack()
                tk.Button(self.root, text="Editar", command=lambda c=competidor: self.editar_competidor(c), font=self.font).pack()
                tk.Button(self.root, text="Borrar", command=lambda c=competidor: self.borrar_competidor(c), font=self.font).pack()
        else:
            tk.Label(self.root, text="No hay competidores registrados", font=self.font).pack()
        tk.Button(self.root, text="Volver", command=self.mostrar_menu, font=self.font).pack()

    def buscar_competidor(self):
        self.clear_frame()

        tk.Label(self.root, text="Seleccionar Competidor:", font=self.font).pack()

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

        tk.Button(self.root, text="Buscar", command=buscar, font=self.font).pack()

    def editar_competidor(self, competidor):
        self.clear_frame()

        tk.Label(self.root, text="ID", font=self.font).pack()
        id_entry = tk.Entry(self.root, font=self.font)
        id_entry.insert(0, competidor.id)
        id_entry.pack()

        tk.Label(self.root, text="Nombre", font=self.font).pack()
        nombre_entry = tk.Entry(self.root, font=self.font)
        nombre_entry.insert(0, competidor.nombre)
        nombre_entry.pack()

        tk.Label(self.root, text="Edad", font=self.font).pack()
        edad_entry = tk.Entry(self.root, font=self.font)
        edad_entry.insert(0, competidor.edad)
        edad_entry.pack()

        tk.Label(self.root, text="Sexo", font=self.font).pack()
        sexo_entry = tk.Entry(self.root, font=self.font)
        sexo_entry.insert(0, competidor.sexo)
        sexo_entry.pack()

        tk.Label(self.root, text="Carrera ID", font=self.font).pack()
        carrera_id_entry = tk.Entry(self.root, font=self.font)
        carrera_id_entry.insert(0, competidor.carrera_id)
        carrera_id_entry.pack()

        tk.Label(self.root, text="Condición Género Edad Trayecto", font=self.font).pack()
        condicion_entry = tk.Entry(self.root, font=self.font)
        condicion_entry.insert(0, competidor.condicion)
        condicion_entry.pack()

        def actualizar_competidor():
            competidor.id = int(id_entry.get())
            competidor.nombre = nombre_entry.get()
            competidor.edad = int(edad_entry.get())
            competidor.sexo = sexo_entry.get()
            competidor.carrera_id = int(carrera_id_entry.get())
            competidor.condicion = condicion_entry.get()
            messagebox.showinfo("Éxito", "Competidor actualizado exitosamente")
            self.mostrar_menu()

        tk.Button(self.root, text="Actualizar", command=actualizar_competidor, font=self.font).pack()

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
    menu = CompetidorMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()

