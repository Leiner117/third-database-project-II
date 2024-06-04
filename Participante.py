import tkinter as tk
from tkinter import ttk, messagebox, font

# Definir los colores
BG_COLOR = "#F0F0F0"  # Color de fondo
FG_COLOR = "#333333"  # Color de texto
ACCENT_COLOR = "#CCCCCC"  # Color de acento

class Participante:
    def __init__(self, id, competidor_id, tiempo, carrera_id):
        self.id = id
        self.competidor_id = competidor_id
        self.tiempo = tiempo
        self.carrera_id = carrera_id

    def __str__(self):
        return f"ID: {self.id}, Competidor ID: {self.competidor_id}, Tiempo: {self.tiempo}, Carrera ID: {self.carrera_id}"

class ParticipanteMenu:
    def __init__(self, root):
        self.participantes = [
            Participante(1, 1, "1:30:15", 101),
            Participante(2, 2, "1:45:20", 101)
        ]
        
        self.root = root
        self.root.title("Menú de Participantes")
        self.root.geometry("600x400")
        self.root.configure(bg=BG_COLOR)  # Establecer el color de fondo de la ventana principal

        self.font = font.Font(size=12)
        self.menu_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.menu_frame.pack(pady=20)

        tk.Button(self.menu_frame, text="Añadir Participante", command=self.añadir_participante, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X, padx=20, pady=10)
        tk.Button(self.menu_frame, text="Listar Participantes", command=self.listar_participantes, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X, padx=20, pady=10)
        tk.Button(self.menu_frame, text="Buscar Participante", command=self.buscar_participante, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X, padx=20, pady=10)
        tk.Button(self.menu_frame, text="Salir", command=self.root.quit, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X, padx=20, pady=10)

    def añadir_participante(self):
        self.clear_frame()

        frame = tk.Frame(self.root, bg=BG_COLOR)  # Establecer el color de fondo para el nuevo frame
        frame.pack(pady=20)

        tk.Label(frame, text="ID Competidor:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        competidor_id_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        competidor_id_entry.grid(row=0, column=1, padx=10, pady=10)
        competidor_id_entry.insert(0, "Ingrese el ID del competidor")

        tk.Label(frame, text="Tiempo:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tiempo_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        tiempo_entry.grid(row=1, column=1, padx=10, pady=10)
        tiempo_entry.insert(0, "Ingrese el tiempo en formato HH:MM:SS")

        tk.Label(frame, text="ID Carrera:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        carrera_id_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        carrera_id_entry.grid(row=2, column=1, padx=10, pady=10)
        carrera_id_entry.insert(0, "Ingrese el ID de la carrera")

        def guardar_participante():
            competidor_id = int(competidor_id_entry.get())
            # Validar que el ID de competidor no esté repetido
            competidor_ids = [participante.competidor_id for participante in self.participantes]
            if competidor_id in competidor_ids:
                messagebox.showerror("Error", "El ID de competidor ya está en uso")
                return
            id = len(self.participantes) + 1
            tiempo = tiempo_entry.get()
            carrera_id = int(carrera_id_entry.get())
            participante = Participante(id, competidor_id, tiempo, carrera_id)
            self.participantes.append(participante)
            messagebox.showinfo("Éxito", "Participante añadido correctamente")
            self.mostrar_menu()

        def cancelar():
            self.mostrar_menu()

        tk.Button(frame, text="Guardar", command=guardar_participante, font=self.font).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(frame, text="Cancelar", command=cancelar, font=self.font).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def listar_participantes(self):
        self.clear_frame()

        if self.participantes:
            # Crear Treeview para mostrar la lista de participantes como tabla
            tree = ttk.Treeview(self.root, columns=("ID", "Competidor ID", "Tiempo", "Carrera ID"), show="headings", height=len(self.participantes))
            tree.heading("ID", text="ID")
            tree.heading("Competidor ID", text="Competidor ID")
            tree.heading("Tiempo", text="Tiempo")
            tree.heading("Carrera ID", text="Carrera ID")

            for participante in self.participantes:
                tree.insert("", "end", values=(participante.id, participante.competidor_id, participante.tiempo, participante.carrera_id))

            tree.pack(pady=10)

            # Botones de Editar y Borrar
            buttons_frame = tk.Frame(self.root, bg=BG_COLOR)
            buttons_frame.pack()

            edit_button = tk.Button(buttons_frame, text="Editar", command=lambda: self.editar_participante(tree), font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR)
            edit_button.grid(row=0, column=0, padx=(20, 5), pady=10)

            delete_button = tk.Button(buttons_frame, text="Borrar", command=lambda: self.borrar_participante(tree), font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR)
            delete_button.grid(row=0, column=1, padx=(5, 20), pady=10)

        else:
            tk.Label(self.root, text="No hay participantes registrados", font=self.font, bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.mostrar_menu, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(pady=10)

    def buscar_participante(self):
        self.clear_frame()

        competidor_ids = [participante.competidor_id for participante in self.participantes]
        selected_id = tk.StringVar()
        competidor_combobox = ttk.Combobox(self.root, textvariable=selected_id, values=competidor_ids, font=self.font)
        competidor_combobox.pack(pady=10)

        def buscar():
            competidor_id = int(selected_id.get())
            encontrado = False
            for participante in self.participantes:
                if participante.competidor_id == competidor_id:
                    messagebox.showinfo("Participante Encontrado", str(participante))
                    encontrado = True
                    break

            if not encontrado:
                messagebox.showinfo("No Encontrado", "Participante no encontrado")
            self.mostrar_menu()

        tk.Button(self.root, text="Buscar", command=buscar, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.mostrar_menu, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(pady=5)

    def editar_participante(self, tree):
        # Obtener la fila seleccionada
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Por favor, selecciona un participante para editar.")
            return
        
        # Crear ventana de edición
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Editar Participante")
        edit_window.geometry("300x200")
        edit_window.configure(bg=BG_COLOR)

        tk.Label(edit_window, text="ID Competidor", font=self.font, bg=BG_COLOR).pack()
        competidor_id_entry = tk.Entry(edit_window, font=self.font)
        competidor_id_entry.pack()

        tk.Label(edit_window, text="Tiempo", font=self.font, bg=BG_COLOR).pack()
        tiempo_entry = tk.Entry(edit_window, font=self.font)
        tiempo_entry.pack()

        tk.Label(edit_window, text="ID Carrera", font=self.font, bg=BG_COLOR).pack()
        carrera_id_entry = tk.Entry(edit_window, font=self.font)
        carrera_id_entry.pack()

        # Obtener los valores de la fila seleccionada
        values = tree.item(selected_item, "values")
        competidor_id_entry.insert(0, values[1])
        tiempo_entry.insert(0, values[2])
        carrera_id_entry.insert(0, values[3])

        def actualizar_participante():
            # Obtener los nuevos valores
            nuevo_competidor_id = int(competidor_id_entry.get())
            nuevo_tiempo = tiempo_entry.get()
            nuevo_carrera_id = int(carrera_id_entry.get())

            # Actualizar los valores en el Treeview
            tree.item(selected_item, values=(values[0], nuevo_competidor_id, nuevo_tiempo, nuevo_carrera_id))
            
            messagebox.showinfo("Éxito", "Participante actualizado correctamente")
            edit_window.destroy()

        tk.Button(edit_window, text="Actualizar", command=actualizar_participante, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack()

    def borrar_participante(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Por favor, selecciona un participante para borrar.")
            return

        # Obtener el ID del participante seleccionado
        participante_id = int(tree.item(selected_item, "values")[0])

        # Encontrar y eliminar el participante de la lista
        for participante in self.participantes:
            if participante.id == participante_id:
                self.participantes.remove(participante)
                break

        # Actualizar la lista de participantes
        self.listar_participantes()

        messagebox.showinfo("Éxito", "Participante borrado correctamente")

    def mostrar_menu(self):
        self.clear_frame()
        self.menu_frame.pack(pady=20)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()


def main():
    root = tk.Tk()
    root.configure(bg=BG_COLOR)  # Establecer el color de fondo de la ventana principal
    menu = ParticipanteMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
