import tkinter as tk
import subprocess
import sys

# Variables para almacenar las instancias de los procesos

process_clientes = None
process_Nueva_Plataforma = None
process_reporte_semanal = None

# Función para ejecutar el script Buzon.py con el id_cliente

def start_clientes():
    global process_clientes
    try:
        process_clientes = subprocess.Popen(["python", "trabajadores.py"])  # Ejecuta el archivo 'clientes.py'
        print("Trabajadores iniciado.")
    except Exception as e:
        print(f"Error al abrir Trabajadores: {e}")


def start_reporte_semanal():
    global process_reporte_semanal
    try:
        process_reporte_semanal = subprocess.Popen(["python", "reportes_semanal.py"])  # Ejecuta el archivo 'clientes.py'
        print("Reporte_semanal iniciado.")
    except Exception as e:
        print(f"Error al abrir Reporte_semanal: {e}")

"""DONE"""
def start_Nueva_Plataforma():
    global process_Nueva_Plataforma
    try:
        process_Nueva_Plataforma = subprocess.Popen(
            ["python", "reportes.py"]  # Pasamos id_cliente como argumento
        )
    except Exception as e:
        print(f"Error al abrir Reportes: {e}")

# Función para detener los procesos
def stop_processes():
    global process_clientes, process_Nueva_Plataforma, process_reporte_semanal
   
    if process_clientes is not None:
        process_clientes.terminate()  # Termina el proceso de 'Trabajadores.py'
        process_clientes = None
        print("Trabajadores detenido.")

    if process_Nueva_Plataforma is not None:
        process_Nueva_Plataforma.terminate()  # Termina el proceso de 'clientes.py'
        process_Nueva_Plataforma = None
        print("Reporte detenido.")
    
    if process_reporte_semanal is not None:
        process_reporte_semanal.terminate()  # Termina el proceso de 'clientes.py'
        process_reporte_semanal = None
        print("Reporte Semanal detenido.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Panel de Control")
root.geometry("400x650")
root.config(bg="#0B3D91")  # Fondo azul oscuro

# Etiqueta de título
label = tk.Label(root, text="Elige una opción:", font=("Arial", 18), bg="#0B3D91", fg="white")
label.pack(pady=20)


# Botón para los Nueva Plataforma
btn_Nueva_Plataforma = tk.Button(root, text="Boletas - Start", font=("Arial", 14), bg="#1E90FF", fg="white", width=20, command=start_Nueva_Plataforma)
btn_Nueva_Plataforma.pack(pady=10)

# Botón para los Nueva Plataforma
btn_reporte_semanal = tk.Button(root, text="Reporte Semanal - Start", font=("Arial", 14), bg="#1E90FF", fg="white", width=20, command=start_reporte_semanal)
btn_reporte_semanal.pack(pady=10)

# Botón para los Clientes
btn_clientes = tk.Button(root, text="Trabajadores - Start", font=("Arial", 14), bg="#1E90FF", fg="white", width=20, command=start_clientes)
btn_clientes.pack(pady=10)


# Botón para detener los procesos
btn_stop = tk.Button(root, text="Detener", font=("Arial", 14), bg="#FF6347", fg="white", width=20, command=stop_processes)
btn_stop.pack(pady=20)

# Loop de la ventana
root.mainloop()
