import tkinter as tk
from tkinter import ttk, messagebox, font

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

        self.font = font.Font(size=12)
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(pady=20)

        tk.Button(self.menu_frame, text="Añadir Participante", command=self.añadir_participante, font=self.font).pack(fill=tk.X)
        tk.Button(self.menu_frame, text="Listar Participantes", command=self.listar_participantes, font=self.font).pack(fill=tk.X)
        tk.Button(self.menu_frame, text="Buscar Participante", command=self.buscar_participante, font=self.font).pack(fill=tk.X)
        tk.Button(self.menu_frame, text="Salir", command=self.root.quit, font=self.font).pack(fill=tk.X)

    def añadir_participante(self):
        self.clear_frame()

        tk.Label(self.root, text="ID Competidor", font=self.font).pack()
        competidor_id_entry = tk.Entry(self.root, font=self.font)
        competidor_id_entry.pack()

        tk.Label(self.root, text="Tiempo", font=self.font).pack()
        tiempo_entry = tk.Entry(self.root, font=self.font)
        tiempo_entry.pack()

        tk.Label(self.root, text="ID Carrera", font=self.font).pack()
        carrera_id_entry = tk.Entry(self.root, font=self.font)
        carrera_id_entry.pack()

        def guardar_participante():
            id = len(self.participantes) + 1
            competidor_id = int(competidor_id_entry.get())
            tiempo = tiempo_entry.get()
            carrera_id = int(carrera_id_entry.get())
            participante = Participante(id, competidor_id, tiempo, carrera_id)
            self.participantes.append(participante)
            messagebox.showinfo("Éxito", "Participante añadido exitosamente")
            self.mostrar_menu()

        tk.Button(self.root, text="Guardar", command=guardar_participante, font=self.font).pack()

    def listar_participantes(self):
        self.clear_frame()
        if self.participantes:
            for participante in self.participantes:
                tk.Label(self.root, text=str(participante), font=self.font).pack()
                tk.Button(self.root, text="Editar", command=lambda p=participante: self.editar_participante(p), font=self.font).pack()
                tk.Button(self.root, text="Borrar", command=lambda p=participante: self.borrar_participante(p), font=self.font).pack()
        else:
            tk.Label(self.root, text="No hay participantes registrados", font=self.font).pack()
        tk.Button(self.root, text="Volver", command=self.mostrar_menu, font=self.font).pack()

    def buscar_participante(self):
        self.clear_frame()

        competidor_ids = [participante.competidor_id for participante in self.participantes]
        selected_id = tk.StringVar()
        competidor_combobox = ttk.Combobox(self.root, textvariable=selected_id, values=competidor_ids, font=self.font)
        competidor_combobox.pack()

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

        tk.Button(self.root, text="Buscar", command=buscar, font=self.font).pack()

    def editar_participante(self, participante):
        self.clear_frame()

        tk.Label(self.root, text="ID Competidor", font=self.font).pack()
        competidor_id_entry = tk.Entry(self.root, font=self.font)
        competidor_id_entry.insert(0, participante.competidor_id)
        competidor_id_entry.pack()

        tk.Label(self.root, text="Tiempo", font=self.font).pack()
        tiempo_entry = tk.Entry(self.root, font=self.font)
        tiempo_entry.insert(0, participante.tiempo)
        tiempo_entry.pack()

        tk.Label(self.root, text="ID Carrera", font=self.font).pack()
        carrera_id_entry = tk.Entry(self.root, font=self.font)
        carrera_id_entry.insert(0, participante.carrera_id)
        carrera_id_entry.pack()

        def actualizar_participante():
            participante.competidor_id = int(competidor_id_entry.get())
            participante.tiempo = tiempo_entry.get()
            participante.carrera_id = int(carrera_id_entry.get())
            messagebox.showinfo("Éxito", "Participante actualizado exitosamente")
            self.mostrar_menu()

        tk.Button(self.root, text="Actualizar", command=actualizar_participante, font=self.font).pack()

    def borrar_participante(self, participante):
        self.participantes.remove(participante)
        messagebox.showinfo("Éxito", "Participante borrado exitosamente")
        self.mostrar_menu()

    def mostrar_menu(self):
        self.clear_frame()
        self.menu_frame.pack(pady=20)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

def main():
    root = tk.Tk()
    menu = ParticipanteMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()

           
