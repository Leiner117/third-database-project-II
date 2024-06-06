import tkinter as tk
from tkinter import ttk, messagebox, font
from backend import add_participante, get_participantes, delete_participante, update_participante, get_times_by_participant, get_participantes_tiempos, add_tiempo_local, update_tiempo_local, delete_tiempo_local

# Definir los colores
BG_COLOR = "#F0F0F0"  # Color de fondo
FG_COLOR = "#333333"  # Color de texto
ACCENT_COLOR = "#CCCCCC"  # Color de acento

class Participante:
    def __init__(self, id, competidor_id, tiempo, carrera_id, dorsal):
        self.id = id
        self.competidor_id = competidor_id
        self.tiempo = tiempo
        self.carrera_id = carrera_id
        self.dorsal = dorsal

    def __str__(self):
        return f"ID: {self.id}, Competidor ID: {self.competidor_id}, Tiempo: {self.tiempo}, Carrera ID: {self.carrera_id}, Dorsal: {self.dorsal}"

class ParticipanteMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú de Participantes")
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.root.configure(bg=BG_COLOR)

        self.font = font.Font(size=12)
        self.menu_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.menu_frame.pack(pady=20)

        tk.Button(self.menu_frame, text="Añadir Participante", command=self.añadir_participante, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X, padx=20, pady=10)
        tk.Button(self.menu_frame, text="Listar Participantes", command=self.listar_participantes, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X, padx=20, pady=10)
        tk.Button(self.menu_frame, text="Buscar Participante", command=self.buscar_participante, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X, padx=20, pady=10)
        tk.Button(self.menu_frame, text="Salir", command=self.root.destroy, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(fill=tk.X, padx=20, pady=10)

    def obtener_participantes_desde_bd(self):
        participantes_bd = get_participantes()
        participantes = []
        for p in participantes_bd:
            id, competidor_id, carrera_id, dorsal = p
            tiempos = get_times_by_participant(competidor_id)
            tiempo = tiempos[0][3] if tiempos else None
            participantes.append(Participante(id, competidor_id, tiempo, carrera_id, dorsal))
        return participantes

    def añadir_participante(self):
        self.clear_frame()

        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.pack(pady=20)

        tk.Label(frame, text="ID Competidor:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        competidor_id_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        competidor_id_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame, text="Tiempo:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tiempo_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        tiempo_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(frame, text="ID Carrera:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        carrera_id_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        carrera_id_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(frame, text="Dorsal:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=3, column=0, padx=10, pady=10, sticky="e")
        dorsal_entry = tk.Entry(frame, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        dorsal_entry.grid(row=3, column=1, padx=10, pady=10)

        def guardar_participante():
            competidor_id = int(competidor_id_entry.get())
            tiempo = tiempo_entry.get()
            carrera_id = int(carrera_id_entry.get())
            dorsal = int(dorsal_entry.get())
            add_participante(carrera_id, competidor_id, dorsal)
            self.participantes = self.obtener_participantes_desde_bd()
            messagebox.showinfo("Éxito", "Participante añadido correctamente")
            self.mostrar_menu()

        def cancelar():
            self.mostrar_menu()

        tk.Button(frame, text="Guardar", command=guardar_participante, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(frame, text="Cancelar", command=cancelar, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def listar_participantes(self):
        self.clear_frame()
        self.participantes = self.obtener_participantes_desde_bd()

        if self.participantes:
            tree = ttk.Treeview(self.root, columns=("ID", "Competidor ID", "Tiempo", "Carrera ID", "Dorsal"), show="headings", height=len(self.participantes))
            tree.heading("ID", text="ID")
            tree.heading("Competidor ID", text="Competidor ID")
            tree.heading("Tiempo", text="Tiempo")
            tree.heading("Carrera ID", text="Carrera ID")
            tree.heading("Dorsal", text="Dorsal")

            for participante in self.participantes:
                tree.insert("", "end", values=(participante.id, participante.competidor_id, participante.tiempo, participante.carrera_id, participante.dorsal))

            tree.pack(pady=10)

            buttons_frame = tk.Frame(self.root, bg=BG_COLOR)
            buttons_frame.pack()

            tk.Button(buttons_frame, text="Editar", command=lambda: self.editar_participante(tree), font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=0, column=0, padx=(20, 5), pady=10)
            tk.Button(buttons_frame, text="Borrar", command=lambda: self.borrar_participante(tree), font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=0, column=1, padx=(5, 20), pady=10)
        else:
            tk.Label(self.root, text="No hay participantes registrados", font=self.font, bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)
        tk.Button(self.root, text="Volver", command=self.mostrar_menu, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).pack(pady=10)

    def buscar_participante(self):
        self.clear_frame()
        self.participantes = self.obtener_participantes_desde_bd()

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
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Por favor, selecciona un participante para editar.")
            return
        
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Editar Participante")
        edit_window.geometry("300x300")
        edit_window.configure(bg=BG_COLOR)
        
        participante_values = tree.item(selected_item, "values")
        participante_id = participante_values[0]

        tk.Label(edit_window, text="ID Competidor:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        competidor_id_entry = tk.Entry(edit_window, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        competidor_id_entry.grid(row=0, column=1, padx=10, pady=10)
        competidor_id_entry.insert(0, participante_values[1])

        tk.Label(edit_window, text="Tiempo:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tiempo_entry = tk.Entry(edit_window, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        tiempo_entry.grid(row=1, column=1, padx=10, pady=10)
        tiempo_entry.insert(0, participante_values[2])

        tk.Label(edit_window, text="ID Carrera:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        carrera_id_entry = tk.Entry(edit_window, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        carrera_id_entry.grid(row=2, column=1, padx=10, pady=10)
        carrera_id_entry.insert(0, participante_values[3])

        tk.Label(edit_window, text="Dorsal:", font=self.font, fg=FG_COLOR, bg=BG_COLOR).grid(row=3, column=0, padx=10, pady=10, sticky="e")
        dorsal_entry = tk.Entry(edit_window, font=self.font, fg=FG_COLOR, bg=ACCENT_COLOR)
        dorsal_entry.grid(row=3, column=1, padx=10, pady=10)
        dorsal_entry.insert(0, participante_values[4])

        def guardar_cambios():
            nuevo_competidor_id = int(competidor_id_entry.get())
            nuevo_tiempo = tiempo_entry.get()
            nuevo_carrera_id = int(carrera_id_entry.get())
            nuevo_dorsal = int(dorsal_entry.get())
            
            update_participante(nuevo_carrera_id, nuevo_competidor_id, nuevo_dorsal)
            self.participantes = self.obtener_participantes_desde_bd()
            messagebox.showinfo("Éxito", "Participante actualizado correctamente")
            edit_window.destroy()
            self.mostrar_menu()

        tk.Button(edit_window, text="Guardar", command=guardar_cambios, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(edit_window, text="Cancelar", command=edit_window.destroy, font=self.font, bg=ACCENT_COLOR, fg=FG_COLOR).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def borrar_participante(self, tree):
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Por favor, selecciona un participante para borrar.")
            return
        
        participante_values = tree.item(selected_item, "values")
        participante_id = participante_values[0]

        delete_participante(participante_id)
        self.participantes = self.obtener_participantes_desde_bd()
        messagebox.showinfo("Éxito", "Participante borrado correctamente")
        self.mostrar_menu()

    def mostrar_menu(self):
        self.clear_frame()
        self.__init__(self.root)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    global window_height,window_width,position_right,position_top
    root = tk.Tk()
    window_width = 600
    window_height = 400

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    app = ParticipanteMenu(root)
    root.mainloop()