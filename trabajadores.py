import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import os

# Conectar a la base de datos
def connect_db():
    current_dir = os.getcwd()
    db_folder = "Database_Clientes_Yuvana"
    db_filename = "Database_Constructoras.db"
    DB_PATH = os.path.join(current_dir, db_folder, db_filename)
    return sqlite3.connect(DB_PATH)

# Obtener todos los registros
def get_trabajadores():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Trabajadores")
    trabajadores = cursor.fetchall()
    conn.close()
    return trabajadores

# Mostrar los trabajadores en el árbol de visualización
def show_trabajadores():
    for row in tree.get_children():
        tree.delete(row)
    trabajadores = get_trabajadores()
    for trabajador in trabajadores:
        tree.insert("", "end", values=trabajador)

# Validar entrada de Cargo y Sistema Pensionario
def validate_fields(cargo, sistema_pensionario):
    valid_cargos = ["OFICIAL", "OPERARIO", "PEON"]
    valid_sistema_pensionario = ["AFP", "ONP"]

    if cargo not in valid_cargos:
        messagebox.showerror("Error en Cargo", "El Cargo debe ser uno de los siguientes: OFICIAL, OPERARIO, PEON.")
        return False

    if sistema_pensionario not in valid_sistema_pensionario:
        messagebox.showerror("Error en Sistema Pensionario", "El Sistema Pensionario debe ser AFP o ONP.")
        return False

    return True

# Función para añadir un nuevo trabajador
def add_trabajador():
    cargo = entry_cargo.get()
    dni = entry_dni.get()
    nombre = entry_nombre.get()
    situacion = entry_situacion.get()
    fecha_ingreso = entry_fecha_ingreso.get()
    sistema_pensionario = entry_sistema_pensionario.get()
    descripcion_sistema_pensionario = entry_descripcion_sistema_pensionario.get()

    if not cargo or not dni or not nombre or not situacion or not fecha_ingreso or not sistema_pensionario or not descripcion_sistema_pensionario:
        messagebox.showwarning("Entrada inválida", "Todos los campos deben ser llenados.")
        return

    if not validate_fields(cargo, sistema_pensionario):
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Trabajadores (Cargo, DNI, Nombre, Situacion, Fecha_ingreso, Sistema_Pensionario, descripcion_sistema_pensionario) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (cargo, dni, nombre, situacion, fecha_ingreso, sistema_pensionario, descripcion_sistema_pensionario))
    conn.commit()
    conn.close()

    # Limpiar campos y actualizar la lista de trabajadores
    entry_cargo.delete(0, tk.END)
    entry_dni.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_situacion.delete(0, tk.END)
    entry_fecha_ingreso.delete(0, tk.END)
    entry_sistema_pensionario.delete(0, tk.END)
    entry_descripcion_sistema_pensionario.delete(0, tk.END)

    show_trabajadores()

# Función para eliminar un trabajador con confirmación
def delete_trabajador():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selección inválida", "Por favor, selecciona un trabajador para eliminar.")
        return

    confirm = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este trabajador?")
    if confirm:
        trabajador_id = tree.item(selected_item, 'values')[0]

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Trabajadores WHERE TrabajadorID=?", (trabajador_id,))
        conn.commit()
        conn.close()

        show_trabajadores()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Trabajadores")
root.geometry("1000x600")
root.resizable(True, True)

# Frame para los campos de entrada
frame_entry = tk.Frame(root)
frame_entry.pack(pady=10)

# Etiquetas y entradas
label_cargo = tk.Label(frame_entry, text="Cargo:")
label_cargo.grid(row=0, column=0, padx=5, pady=5)
entry_cargo = tk.Entry(frame_entry)
entry_cargo.grid(row=0, column=1, padx=5, pady=5)

label_dni = tk.Label(frame_entry, text="DNI:")
label_dni.grid(row=1, column=0, padx=5, pady=5)
entry_dni = tk.Entry(frame_entry)
entry_dni.grid(row=1, column=1, padx=5, pady=5)

label_nombre = tk.Label(frame_entry, text="Nombre:")
label_nombre.grid(row=2, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_entry)
entry_nombre.grid(row=2, column=1, padx=5, pady=5)

label_situacion = tk.Label(frame_entry, text="Situacion:")
label_situacion.grid(row=3, column=0, padx=5, pady=5)
entry_situacion = tk.Entry(frame_entry)
entry_situacion.grid(row=3, column=1, padx=5, pady=5)

label_fecha_ingreso = tk.Label(frame_entry, text="Fecha Ingreso:")
label_fecha_ingreso.grid(row=4, column=0, padx=5, pady=5)
entry_fecha_ingreso = tk.Entry(frame_entry)
entry_fecha_ingreso.grid(row=4, column=1, padx=5, pady=5)

label_sistema_pensionario = tk.Label(frame_entry, text="Sistema Pensionario:")
label_sistema_pensionario.grid(row=5, column=0, padx=5, pady=5)
entry_sistema_pensionario = tk.Entry(frame_entry)
entry_sistema_pensionario.grid(row=5, column=1, padx=5, pady=5)

label_descripcion_sistema_pensionario = tk.Label(frame_entry, text="Descripcion Sistema Pensionario:")
label_descripcion_sistema_pensionario.grid(row=6, column=0, padx=5, pady=5)
entry_descripcion_sistema_pensionario = tk.Entry(frame_entry)
entry_descripcion_sistema_pensionario.grid(row=6, column=1, padx=5, pady=5)

# Indicaciones para las entradas de Cargo y Sistema Pensionario
frame_alertas = tk.Frame(root)
frame_alertas.pack(pady=10)

label_cargo_alerta = tk.Label(frame_alertas, text="* Cargo debe ser: OFICIAL, OPERARIO, PEON", fg="red")
label_cargo_alerta.grid(row=0, column=0, padx=5, pady=5)

label_sistema_alerta = tk.Label(frame_alertas, text="* Sistema Pensionario debe ser: AFP o ONP", fg="red")
label_sistema_alerta.grid(row=1, column=0, padx=5, pady=5)

# Botones
button_add = tk.Button(root, text="Añadir Trabajador", command=add_trabajador)
button_add.pack(pady=10)

button_delete = tk.Button(root, text="Eliminar Trabajador", command=delete_trabajador)
button_delete.pack(pady=10)

# Crear el contenedor para el árbol de trabajadores y el scrollbar
frame_tree = tk.Frame(root)
frame_tree.pack(pady=20, fill=tk.BOTH, expand=True)

# Scrollbar vertical
scrollbar_y = tk.Scrollbar(frame_tree, orient="vertical")

# Árbol para mostrar los trabajadores
columns = ("TrabajadorID", "Cargo", "DNI", "Nombre", "Situacion", "Fecha_ingreso", "Sistema_Pensionario", "descripcion_sistema_pensionario")
tree = ttk.Treeview(frame_tree, columns=columns, show="headings", yscrollcommand=scrollbar_y.set)
tree.heading("TrabajadorID", text="TrabajadorID")
tree.heading("Cargo", text="Cargo")
tree.heading("DNI", text="DNI")
tree.heading("Nombre", text="Nombre")
tree.heading("Situacion", text="Situacion")
tree.heading("Fecha_ingreso", text="Fecha Ingreso")
tree.heading("Sistema_Pensionario", text="Sistema Pensionario")
tree.heading("descripcion_sistema_pensionario", text="Descripcion Sistema Pensionario")

# Asignar el scrollbar vertical al árbol
scrollbar_y.config(command=tree.yview)
scrollbar_y.pack(side="right", fill="y")

# Empacar el árbol de trabajadores en el frame
tree.pack(pady=20, fill=tk.BOTH, expand=True)

# Mostrar los trabajadores al iniciar la aplicación
show_trabajadores()

# Ejecutar la aplicación
root.mainloop()
