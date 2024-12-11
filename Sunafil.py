from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sqlite3
import os
import sys


def sunafil(id_cliente):

    # Ruta al archivo de la base de datos
    current_dir = os.getcwd()
    db_folder = "Database_Clientes_Yuvana"
    db_filename = "Sunafil.db"
    DB_PATH = os.path.join(current_dir,db_folder, db_filename)

    # Conectar a la base de datos SQLite
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    #id_cliente = 1
    a = 0
    i = 1

    cursor.execute("SELECT COUNT(*) FROM Customers")
    campo_customerIDQuantity = cursor.fetchone()
    ValueCount = campo_customerIDQuantity[0]

    id_cliente_while = id_cliente
    while a < ValueCount:
        
        """CREAR CARPETA:"""
        cursor.execute("SELECT Razon_Social FROM Customers WHERE CustomersID = ?", (id_cliente_while,))
        campo_RazonSocial = cursor.fetchone()
        razon_social = campo_RazonSocial[0]

        cursor.execute("SELECT Digito FROM Customers WHERE CustomersID = ?", (id_cliente_while,))
        campo_digito = cursor.fetchone()
        digito = campo_digito[0]

        # Crear la carpeta si no existe
        nombre_carpeta = f"{digito} - {razon_social}"
        current_dir = os.path.dirname(__file__)
        carpeta_empresa = os.path.join(current_dir, "Sunafil", nombre_carpeta)
        nombre_archivo = os.path.join(carpeta_empresa, f"Pantalla_inicio.png")
        os.makedirs(carpeta_empresa, exist_ok=True)
        
        """CONFIGURACION:"""
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--incognito")  # Activar modo incógnito
        options.binary_location = r"C:/driver_google/chrome-win64/chrome.exe"
        
        service = Service(r"C:/driver_google/chrome-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://api-seguridad.sunat.gob.pe/v1/clientessol/b6474e23-8a3b-4153-b301-dafcc9646250/oauth2/login?originalUrl=https://casillaelectronica.sunafil.gob.pe/si.inbox/Login/Empresa&state=s")
        time.sleep(3)
        
        wait = WebDriverWait(driver, 5)
        driver.maximize_window()
        
        """INICIAR SESION:"""
        cursor.execute("SELECT RUC FROM Customers WHERE CustomersID = ?", (id_cliente_while,))
        Campo_RUCSQL = cursor.fetchone()
        Value = Campo_RUCSQL[0]
        Ruc = wait.until(EC.presence_of_element_located((By.ID, "txtRuc")))
        Ruc.send_keys(Value)
    
        cursor.execute("SELECT Usuario FROM Customers WHERE CustomersID = ?", (id_cliente_while,))
        Campo_UsuarioSQL = cursor.fetchone()
        Value1 = Campo_UsuarioSQL[0]
        usuario = wait.until(EC.presence_of_element_located((By.ID, "txtUsuario")))
        usuario.send_keys(Value1) 

        cursor.execute("SELECT Password FROM Customers WHERE CustomersID = ?", (id_cliente_while,))
        Campo_PasswordSQL = cursor.fetchone()
        Value2 = Campo_PasswordSQL[0]
        Password = wait.until(EC.presence_of_element_located((By.ID, "txtContrasena")))
        Password.send_keys(Value2)
        Password.send_keys(Keys.ENTER)
        time.sleep(5)
    
        
        """SACAR CAPTURA:"""
        # Guardar la captura en un archivo
        screenshot = driver.get_screenshot_as_file(nombre_archivo)
        
        """CIERRA:"""
        # Encuentra el botón por su clase y haz clic en él
        boton = driver.find_element(By.CLASS_NAME, "close")
        boton.click()

        """NOTIFICAIONES DE FIZCALIZACION:"""
        # Encuentra y haz clic en el botón Notificaciones de fiscalización
        NotificacionesFiscalizacion = wait.until(EC.presence_of_element_located((By.ID, "formMenu2:j_idt25:1:j_idt29:0:j_idt31")))
        NotificacionesFiscalizacion.click() 
        
        time.sleep(5)
        """SCROLEAR:"""
        # Scrollear 400 píxeles abajo con JavaScript
        driver.execute_script("window.scrollBy(0, 400);")
        
        """CAPTURA DE PANTALLA:"""
        # Captura de pantalla Notificaciones de Fiscalización
        nombre_archivo1 = os.path.join(carpeta_empresa, f"Notificaciones_de_Fiscalización.png")
        driver.get_screenshot_as_file(nombre_archivo1)
        

        """NOTIFICAIONES PREVIAS:"""
        # Encuentra y haz clic en el botón Notificaciones previas
        NotificacionesPrevias = wait.until(EC.presence_of_element_located((By.ID, "formMenu2:j_idt25:1:j_idt29:1:j_idt31")))
        NotificacionesPrevias.click() 

        # Scrollear 400 píxeles abajo con JavaScript
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 400);")
        

        # Captura de pantalla Notificaciones previas
        nombre_archivo2 = os.path.join(carpeta_empresa, f"Notificaciones_Previas.png")
        driver.get_screenshot_as_file(nombre_archivo2)

        # Encuentra y haz clic en el botón Acciones previas
        AccionesPrevias = wait.until(EC.presence_of_element_located((By.ID, "formMenu2:j_idt25:1:j_idt29:2:j_idt31")))
        AccionesPrevias.click()

        # Scrollear 400 píxeles abajo con JavaScript
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 400);")
        

        # Captura de pantalla Acciones previas
        nombre_archivo3 = os.path.join(carpeta_empresa, f"Acciones_Previas.png")
        driver.get_screenshot_as_file(nombre_archivo3)

        i += 1
        a += 1
        id_cliente_while += 1
        driver.quit()

    # Fin del While    
    conn.close()



if __name__ == "__main__":
        # Verificar si se pasa un argumento (id_cliente)
        if len(sys.argv) > 1:
            try:
                # Obtener el id_cliente desde los argumentos
                id_cliente = int(sys.argv[1])  # El primer argumento es id_cliente
                sunafil(id_cliente)  # Llamar a la función buzon con id_cliente
            except ValueError:
                print("Error: El argumento proporcionado no es un número válido.")
        else:
            print("Error: No se proporcionó id_cliente.") 
