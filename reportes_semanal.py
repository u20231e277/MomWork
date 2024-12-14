import os
import sqlite3
import pandas as pd  # Para manejar datos y exportar a Excel
from tkinter import IntVar
import tkinter as tk

def seleccionar_semana():
    # Guarda el valor seleccionado en la variable "semana"
    semana_seleccionada = variable_semana.get()
    print(f"Semana seleccionada: {semana_seleccionada}")
    ventana.destroy()  # Cierra la ventana

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Seleccionar Semana")
ventana.geometry("350x300")

# Etiqueta de instrucción
etiqueta = tk.Label(ventana, text="¿Qué semana es?", font=("Arial", 14))
etiqueta.pack(pady=10)

# Variable para almacenar la opción seleccionada
variable_semana = IntVar()
variable_semana.set(1)  # Valor predeterminado

# Crear los botones de opción
for i in range(1, 6):
    boton = tk.Radiobutton(
        ventana, text=f"Semana {i}", variable=variable_semana, value=i, font=("Arial", 12)
    )
    boton.pack(anchor=tk.W)

# Botón para confirmar la selección
boton_confirmar = tk.Button(
    ventana, text="Confirmar", command=seleccionar_semana, font=("Arial", 12)
)
boton_confirmar.pack(pady=10)

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()

# Al cerrar la ventana, el valor de la variable se puede utilizar
semana = variable_semana.get()
print(f"El valor final de semana es: {semana}")

def exportar_a_excel(semana):
    try:
        # Ruta de la base de datos
        current_dir = os.getcwd()
        db_folder = "Database_Clientes_Yuvana"
        db_filename = "Database_Constructoras.db"
        DB_PATH = os.path.join(current_dir, db_folder, db_filename)

        # Conexión a la base de datos
        conexion = sqlite3.connect(DB_PATH)

        # Nombre de la tabla dinámica
        table_name = f"Registro Semana {semana}"

        # Leer la tabla desde SQLite a un DataFrame de pandas
        query = f"SELECT * FROM '{table_name}'"
        df = pd.read_sql_query(query, conexion)

        # Cerrar la conexión a la base de datos
        conexion.close()

        # Crear la carpeta "Reporte Semanal" si no existe
        report_folder = os.path.join(current_dir, "Reporte Semanal")
        if not os.path.exists(report_folder):
            os.makedirs(report_folder)

        # Crear el archivo Excel dentro de la carpeta "Reporte Semanal"
        excel_file = os.path.join(report_folder, f"{table_name}.xlsx")
        df.to_excel(excel_file, index=False, engine='openpyxl')

        print(f"Tabla exportada exitosamente a '{excel_file}'")
    except Exception as e:
        print(f"Error al exportar a Excel: {e}")

exportar_a_excel(semana)
