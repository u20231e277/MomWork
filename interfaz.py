import tkinter as tk
import subprocess
import sys

# Variables para almacenar las instancias de los procesos
process_buzon = None
process_clientes = None

# Función para ejecutar el script Buzon.py con el id_cliente
def start_buzon():
    global process_buzon
    try:
        id_cliente = int(entry_id_cliente.get())  # Obtener el id_cliente del campo de entrada
        # Llamamos al script Buzon.py pasando id_cliente como argumento
        process_buzon = subprocess.Popen(
            ["python", "Buzon.py", str(id_cliente)]  # Pasamos id_cliente como argumento
        )
        print("Buzón iniciado con id_cliente:", id_cliente)
    except ValueError:
        print("Por favor, ingresa un número válido para id_cliente.")
    except Exception as e:
        print(f"Error al abrir Buzón: {e}")

def start_buzon_dni():
    global process_buzon
    try:
        id_cliente = int(entry_id_cliente.get())  # Obtener el id_cliente del campo de entrada
        # Llamamos al script Buzon.py pasando id_cliente como argumento
        process_buzon = subprocess.Popen(
            ["python", "BuzonDNI.py", str(id_cliente)]  # Pasamos id_cliente como argumento
        )
        print("BuzónDNI iniciado con id_cliente:", id_cliente)
    except ValueError:
        print("Por favor, ingresa un número válido para id_cliente.")
    except Exception as e:
        print(f"Error al abrir BuzónDNI: {e}")

def start_clientes():
    global process_clientes
    try:
        process_clientes = subprocess.Popen(["python", "clientes.py"])  # Ejecuta el archivo 'clientes.py'
        print("Clientes iniciado.")
    except Exception as e:
        print(f"Error al abrir Clientes: {e}")

def start_sunafil():
    global process_sunafil
    try:
        id_cliente = int(entry_id_cliente.get())  # Obtener el id_cliente del campo de entrada
        # Llamamos al script Buzon.py pasando id_cliente como argumento
        process_sunafil = subprocess.Popen(
            ["python", "Sunafil.py", str(id_cliente)]  # Pasamos id_cliente como argumento
        )
        print("Sunafil iniciado con id_cliente:", id_cliente)
    except ValueError:
        print("Por favor, ingresa un número válido para id_cliente.")
    except Exception as e:
        print(f"Error al abrir Sunafil: {e}")

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
root.geometry("400x580")
root.config(bg="#0B3D91")  # Fondo azul oscuro

# Etiqueta de título
label = tk.Label(root, text="Elige una opción:", font=("Arial", 18), bg="#0B3D91", fg="white")
label.pack(pady=20)

# Etiqueta de título
label = tk.Label(root, text="Escribe el ID del Cliente", font=("Arial", 10), bg="#0B3D91", fg="white")
label.pack(pady=10)

# Campo de entrada para el id_cliente
entry_id_cliente = tk.Entry(root, font=("Arial", 14), width=20)
entry_id_cliente.pack(pady=10)

# Botón para el Buzón
btn_buzon = tk.Button(root, text="Buzón - Start", font=("Arial", 14), bg="#1E90FF", fg="white", width=20, command=start_buzon)
btn_buzon.pack(pady=10)

# Botón para el BuzónDNI
btn_buzon_dni = tk.Button(root, text="BuzónDNI - Start", font=("Arial", 14), bg="#1E90FF", fg="white", width=20, command=start_buzon_dni)
btn_buzon_dni.pack(pady=10)

# Botón para los Sunafil
btn_sunafil = tk.Button(root, text="Sunafil - Start", font=("Arial", 14), bg="#1E90FF", fg="white", width=20, command=start_sunafil)
btn_sunafil.pack(pady=10)

# Botón para los Clientes
btn_clientes = tk.Button(root, text="Clientes - Start", font=("Arial", 14), bg="#1E90FF", fg="white", width=20, command=start_clientes)
btn_clientes.pack(pady=10)



# Botón para detener los procesos
btn_stop = tk.Button(root, text="Detener", font=("Arial", 14), bg="#FF6347", fg="white", width=20, command=stop_processes)
btn_stop.pack(pady=20)

# Loop de la ventana
root.mainloop()
