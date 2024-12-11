from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
import sqlite3
import os
import sys

def Nueva_Plataforma(id_cliente):
    # Ruta al archivo de la base de datos
    # Obtener la ruta actual del script
    current_dir = os.getcwd()

    db_folder = "Database_Clientes_Yuvana"
    db_filename = "Nueva_Plataforma.db"
    DB_PATH = os.path.join(current_dir,db_folder, db_filename)

    # Conectar a la base de datos SQLite
    conn = sqlite3.connect(DB_PATH)

    # Crear un cursor
    cursor = conn.cursor()


    #id_cliente=1
    a=0
    i=1

    cursor.execute("SELECT COUNT(*) FROM Customers")
    campo_customerIDQuantity = cursor.fetchone()
    ValueCount = campo_customerIDQuantity[0]

    id_cliente_while = id_cliente

    while a < ValueCount:
        cursor.execute("SELECT Razon_Social FROM Customers WHERE CustomersID = ?",(id_cliente_while,))
        campo_RazonSocial = cursor.fetchone()
        razon_social=campo_RazonSocial[0]

        cursor.execute("SELECT Digito FROM Customers WHERE CustomersID = ?",(id_cliente_while,))
        campo_digito = cursor.fetchone()
        digito = campo_digito[0]
        
        # Configuración de opciones de Chrome
        options = Options()
        options.add_argument("--no-sandbox")  # Desactiva sandbox si hay problemas de permisos
        options.add_argument("--disable-dev-shm-usage")  # Soluciona problemas de memoria compartida
        options.add_argument("--ignore-certificate-errors")  # Ignora errores de certificados SSL
        options.add_argument("--incognito")  # Activar modo incógnito
        options.binary_location = r"C:/driver_google/chrome-win64/chrome.exe"  # Ruta al archivo chrome.exe
        # Configura la espera explícita (máximo 20 segundos)
        

        # Ruta al ChromeDriver dentro de la carpeta de Chrome
        service = Service(r"C:/driver_google/chrome-win64/chromedriver.exe")

        # Configuración del WebDriver
        driver = webdriver.Chrome(service=service, options=options)


        driver.get("https://api-seguridad.sunat.gob.pe/v1/clientessol/59d39217-c025-4de5-b342-393b0f4630ab/oauth2/loginMenuSol?lang=es-PE&showDni=true&showLanguages=false&originalUrl=https://e-menu.sunat.gob.pe/cl-ti-itmenu2/AutenticaMenuInternetPlataforma.htm&state=rO0ABXQA701GcmNEbDZPZ28xODJOWWQ4aTNPT2krWUcrM0pTODAzTEJHTmtLRE1IT2pBQ2l2eW84em5lWjByM3RGY1BLT0tyQjEvdTBRaHNNUW8KWDJRQ0h3WmZJQWZyV0JBaGtTT0hWajVMZEg0Mm5ZdHlrQlFVaDFwMzF1eVl1V2tLS3ozUnVoZ1ovZisrQkZndGdSVzg1TXdRTmRhbAp1ek5OaXdFbG80TkNSK0E2NjZHeG0zNkNaM0NZL0RXa1FZOGNJOWZsYjB5ZXc3MVNaTUpxWURmNGF3dVlDK3pMUHdveHI2cnNIaWc1CkI3SkxDSnc9")
        time.sleep(3)
        # Configura la espera explícita (máximo 5 segundos)
        wait = WebDriverWait(driver, 10)

        driver.maximize_window()

        cursor.execute("SELECT RUC FROM Customers WHERE CustomersID = ?",(id_cliente_while,))
        Campo_RUCSQL = cursor.fetchone()
        Value = Campo_RUCSQL[0]
        Ruc = wait.until(EC.presence_of_element_located((By.ID, "txtRuc")))
        Ruc.send_keys(Value)
    
        cursor.execute("SELECT Usuario FROM Customers WHERE CustomersID = ?",(id_cliente_while,))
        Campo_UsuarioSQL = cursor.fetchone()
        Value1 = Campo_UsuarioSQL[0]
        usuario = wait.until(EC.presence_of_element_located((By.ID, "txtUsuario")))
        usuario.send_keys(Value1) 

        cursor.execute("SELECT Password FROM Customers WHERE CustomersID = ?",(id_cliente_while,))
        Campo_PasswordSQL = cursor.fetchone()
        Value2 = Campo_PasswordSQL[0]
        Password = wait.until(EC.presence_of_element_located((By.ID, "txtContrasena")))
        Password.send_keys(Value2)
        Password.send_keys(Keys.ENTER)
        

        # Crear la carpeta si no existe
        nombre_carpeta = f"{digito} - {razon_social}"
        current_dir = os.path.dirname(__file__)
        carpeta_empresa = os.path.join(current_dir, "Nueva Plataforma" ,nombre_carpeta)
        os.makedirs(carpeta_empresa, exist_ok=True)
        time.sleep(5)


        """CLICK EN BOLETA DE PAGOS:"""
        #Abrir boleta de pago
        Boleta_de_pago= wait.until(EC.presence_of_element_located((By.ID, "nivel3_55_1_4"))) 
        Boleta_de_pago.click()

        time.sleep(3)
        
        """CLICK EN VALORES:"""
        #Abrir Valores
        Valores= wait.until(EC.presence_of_element_located((By.ID,("nivel4_55_1_4_1_3"))))
        Valores.click()

        time.sleep(5)

        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "iframeApplication"))  # ID del iframe
            )

        # Cambia al contexto del iframe
        iframe = driver.find_element(By.ID, "iframeApplication")
        driver.switch_to.frame(iframe)
        driver.execute_script("window.scrollBy(0, 700);")

        time.sleep(5)

        # Obtener el directorio actual del script
        current_dir = os.path.dirname(__file__)
        # Construir la ruta para Capturas
        ruta_capturas = os.path.join(current_dir, "Nueva Plataforma", nombre_carpeta)
        #Tomamos captura y guardamos en el archivo
        nombre_archivo = os.path.join(ruta_capturas, f"Valores.png")
        screenshot = pyautogui.screenshot()

        # Guardar la captura en un archivo
        screenshot.save(nombre_archivo)

        #Salir del iframe
        driver.switch_to.default_content()


        """CLICK EN FRACCIONAMIENTO:"""
        #Abrir boleta de pago
        Fraccionamiento= wait.until(EC.presence_of_element_located((By.ID, "nivel4_55_1_4_1_4"))) 
        Fraccionamiento.click()
        time.sleep(5)
        #Tomamos captura y guardamos en el archivo
        ruta_capturas = os.path.join(current_dir, "Nueva Plataforma", nombre_carpeta)
        nombre_archivo2 = os.path.join(ruta_capturas, f"Fraccionamiento.png")
        screenshot2 = pyautogui.screenshot()

        # Guardar la captura en un archivo
        screenshot2.save(nombre_archivo2)


        

        """CLICK EN BUZON:"""
        #Abrir boleta de pago
        Buzon= wait.until(EC.presence_of_element_located((By.ID, "aOpcionBuzon"))) 
        Buzon.click()

        time.sleep(6)

        #Tomamos captura y guardamos en el archivo
        ruta_capturas = os.path.join(current_dir, "Nueva Plataforma", nombre_carpeta)
        nombre_archivo3 = os.path.join(ruta_capturas, f"BuzonNotificaciones.png")
        screenshot3 = pyautogui.screenshot()

        # Guardar la captura en un archivo
        screenshot3.save(nombre_archivo3)

        i+=1
        a+=1
        id_cliente_while+=1
        driver.quit()

    # Fin del While    
    conn.close()


if __name__ == "__main__":
        # Verificar si se pasa un argumento (id_cliente)
        if len(sys.argv) > 1:
            try:
                # Obtener el id_cliente desde los argumentos
                id_cliente = int(sys.argv[1])  # El primer argumento es id_cliente
                Nueva_Plataforma(id_cliente)  # Llamar a la función buzon con id_cliente
            except ValueError:
                print("Error: El argumento proporcionado no es un número válido.")
        else:
            print("Error: No se proporcionó id_cliente.") 
