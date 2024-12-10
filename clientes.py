import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importar ttk
import sqlite3
import os

# Conectar a la base de datos
def connect_db():
    current_dir = os.getcwd()
    db_folder = "Database_Clientes_Yuvana"
    db_filename = "DatabaseCustomersYuvanaNEW.db"
    DB_PATH = os.path.join(current_dir, db_folder, db_filename)
    return sqlite3.connect(DB_PATH)

# Obtener todos los registros
def get_customers():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customers")
    customers = cursor.fetchall()
    conn.close()
    return customers

# Mostrar los clientes en el árbol de visualización
def show_customers():
    for row in tree.get_children():
        tree.delete(row)
    customers = get_customers()
    for customer in customers:
        tree.insert("", "end", values=customer)

# Función para añadir un nuevo cliente
def add_customer():
    digito = entry_digito.get()
    razon_social = entry_razon_social.get()
    regimen = entry_regimen.get()
    ruc = entry_ruc.get()
    usuario = entry_usuario.get()
    password = entry_password.get()

    if not digito or not razon_social or not regimen or not ruc or not usuario or not password:
        messagebox.showwarning("Entrada inválida", "Todos los campos deben ser llenados.")
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Customers (Digito, Razon_Social, Regimen, RUC, Usuario, Password) VALUES (?, ?, ?, ?, ?, ?)",
                   (digito, razon_social, regimen, ruc, usuario, password))
    conn.commit()
    conn.close()

    # Limpiar campos y actualizar la lista de clientes
    entry_digito.delete(0, tk.END)
    entry_razon_social.delete(0, tk.END)
    entry_regimen.delete(0, tk.END)
    entry_ruc.delete(0, tk.END)
    entry_usuario.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    show_customers()

# Función para reorganizar los IDs
def reorganize_ids():
    conn = connect_db()
    cursor = conn.cursor()

    # Obtener todos los registros ordenados por el ID
    cursor.execute("SELECT CustomersID FROM Customers ORDER BY CustomersID")
    customers = cursor.fetchall()

    # Actualizar los IDs para que sean consecutivos
    for index, customer in enumerate(customers, start=1):
        cursor.execute("UPDATE Customers SET CustomersID=? WHERE CustomersID=?",
                       (index, customer[0]))

    conn.commit()
    conn.close()

# Función para eliminar un cliente con confirmación
def delete_customer():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selección inválida", "Por favor, selecciona un cliente para eliminar.")
        return

    # Confirmar si realmente desea eliminar el cliente
    confirm = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este cliente?")
    if confirm:  # Si el usuario selecciona "Sí"
        customer_id = tree.item(selected_item, 'values')[0]

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Customers WHERE CustomersID=?", (customer_id,))
        conn.commit()
        conn.close()

        # Reorganizar los IDs después de eliminar el registro
        reorganize_ids()

        # Actualizar la lista de clientes
        show_customers()
    else:
        # Si el usuario selecciona "No", no hace nada
        return

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Clientes")

# Configurar la ventana para que sea redimensionable
root.geometry("1600x750")  # Ajusté el tamaño de la ventana
root.resizable(True, True)  # Permitir el redimensionamiento

# Frame para los campos de entrada
frame_entry = tk.Frame(root)
frame_entry.pack(pady=20)

# Etiquetas y entradas
label_digito = tk.Label(frame_entry, text="Dígito:")
label_digito.grid(row=0, column=0, padx=5, pady=5)
entry_digito = tk.Entry(frame_entry)
entry_digito.grid(row=0, column=1, padx=5, pady=5)

label_razon_social = tk.Label(frame_entry, text="Razón Social:")
label_razon_social.grid(row=1, column=0, padx=5, pady=5)
entry_razon_social = tk.Entry(frame_entry)
entry_razon_social.grid(row=1, column=1, padx=5, pady=5)

label_regimen = tk.Label(frame_entry, text="Régimen:")
label_regimen.grid(row=2, column=0, padx=5, pady=5)
entry_regimen = tk.Entry(frame_entry)
entry_regimen.grid(row=2, column=1, padx=5, pady=5)

label_ruc = tk.Label(frame_entry, text="RUC:")
label_ruc.grid(row=3, column=0, padx=5, pady=5)
entry_ruc = tk.Entry(frame_entry)
entry_ruc.grid(row=3, column=1, padx=5, pady=5)

label_usuario = tk.Label(frame_entry, text="Usuario:")
label_usuario.grid(row=4, column=0, padx=5, pady=5)
entry_usuario = tk.Entry(frame_entry)
entry_usuario.grid(row=4, column=1, padx=5, pady=5)

label_password = tk.Label(frame_entry, text="Contraseña:")
label_password.grid(row=5, column=0, padx=5, pady=5)
entry_password = tk.Entry(frame_entry)
entry_password.grid(row=5, column=1, padx=5, pady=5)

# Botones
button_add = tk.Button(root, text="Añadir Cliente", command=add_customer)
button_add.pack(pady=10)

button_delete = tk.Button(root, text="Eliminar Cliente", command=delete_customer)
button_delete.pack(pady=10)

# Crear el contenedor para el árbol de clientes y el scrollbar
frame_tree = tk.Frame(root)
frame_tree.pack(pady=20, fill=tk.BOTH, expand=True)

# Scrollbar vertical
scrollbar_y = tk.Scrollbar(frame_tree, orient="vertical")

# Árbol para mostrar los clientes
columns = ("CustomersID", "Dígito", "Razón Social", "Régimen", "RUC", "Usuario", "Contraseña")
tree = ttk.Treeview(frame_tree, columns=columns, show="headings", height=8, yscrollcommand=scrollbar_y.set)
tree.heading("CustomersID", text="CustomersID")
tree.heading("Dígito", text="Dígito")
tree.heading("Razón Social", text="Razón Social")
tree.heading("Régimen", text="Régimen")
tree.heading("RUC", text="RUC")
tree.heading("Usuario", text="Usuario")
tree.heading("Contraseña", text="Contraseña")

# Asignar el scrollbar vertical al árbol
scrollbar_y.config(command=tree.yview)
scrollbar_y.pack(side="right", fill="y")

# Empacar el árbol de clientes en el frame
tree.pack(pady=20, fill=tk.BOTH, expand=True)

# Mostrar los clientes al iniciar la aplicación
show_customers()

# Ejecutar la aplicación
root.mainloop()
