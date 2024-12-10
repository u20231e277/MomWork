import tkinter as tk
import subprocess

# Variables para almacenar las instancias de los procesos
process_buzon = None
process_clientes = None

# Funciones para ejecutar los otros scripts
def start_buzon():
    global process_buzon
    try:
        process_buzon = subprocess.Popen(["python", "Buzon.py"])  # Ejecuta el archivo 'buzon.py'
        print("Buzón iniciado.")
    except Exception as e:
        print(f"Error al abrir Buzón: {e}")

def start_buzon_dni():
    global process_buzon
    try:
        process_buzon = subprocess.Popen(["python", "BuzonDNI.py"])  # Ejecuta el archivo 'buzon.py'
        print("Buzón DNI iniciado.")
    except Exception as e:
        print(f"Error al abrir Buzón DNI: {e}")

def start_clientes():
    global process_clientes
    try:
        process_clientes = subprocess.Popen(["python", "clientes.py"])  # Ejecuta el archivo 'clientes.py'
        print("Clientes iniciado.")
    except Exception as e:
        print(f"Error al abrir Clientes: {e}")

# Función para detener los procesos
def stop_processes():
    global process_buzon, process_clientes
    if process_buzon is not None:
        process_buzon.terminate()  # Termina el proceso de 'buzon.py'
        process_buzon = None
        print("Buzón detenido.")
    if process_clientes is not None:
        process_clientes.terminate()  # Termina el proceso de 'clientes.py'
        process_clientes = None
        print("Clientes detenido.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Panel de Control")
root.geometry("400x400")
root.config(bg="#0B3D91")  # Fondo azul oscuro

# Etiqueta de título
label = tk.Label(root, text="Elige una opción:", font=("Arial", 18), bg="#0B3D91", fg="white")
label.pack(pady=20)

# Botón para el Buzón
btn_buzon = tk.Button(root, text="Buzón - Start", font=("Arial", 14), bg="#1E90FF", fg="white", width=20, command=start_buzon)
btn_buzon.pack(pady=10)

# Botón para el BuzónDNI
btn_buzon_dni = tk.Button(root, text="BuzónDNI - Start", font=("Arial", 14), bg="#1E90FF", fg="white", width=20, command=start_buzon_dni)
btn_buzon_dni.pack(pady=10)

# Botón para los Clientes
btn_clientes = tk.Button(root, text="Clientes - Start", font=("Arial", 14), bg="#1E90FF", fg="white", width=20, command=start_clientes)
btn_clientes.pack(pady=10)

# Botón para detener los procesos
btn_stop = tk.Button(root, text="Detener", font=("Arial", 14), bg="#FF6347", fg="white", width=20, command=stop_processes)
btn_stop.pack(pady=20)

# Loop de la ventana
root.mainloop()
