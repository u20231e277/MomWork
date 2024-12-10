from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import pyautogui
import time
import sqlite3
import os
import sys

def buzon(id_cliente):
    # Ruta al archivo de la base de datos
    # Obtener la ruta actual del script
    current_dir = os.getcwd()

    db_folder = "Database_Clientes_Yuvana"
    db_filename = "DatabaseCustomersYuvanaNEW.db"
    DB_PATH = os.path.join(current_dir, db_folder, db_filename)


    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    #id_cliente = 124

    a=0
    i=1
    cursor.execute("SELECT COUNT(*) FROM CustomersDNI")
    campo_customerIDQuantity = cursor.fetchone()
    ValueCount = campo_customerIDQuantity[0]
    id_clienteWhile = id_cliente

    while a < ValueCount:
        cursor.execute("SELECT Razon_Social FROM CustomersDNI WHERE CustomersID = ?",(id_clienteWhile,))
        campo_RazonSocial = cursor.fetchone()
        razonSocial = campo_RazonSocial[0]

        cursor.execute("SELECT Digito FROM CustomersDNI WHERE CustomersID = ?",(id_clienteWhile,))
        campo_digito = cursor.fetchone()
        digito = campo_digito[0]

        nombre_carpeta = f"{digito} - {razonSocial}"

        # Obtener el directorio actual del script
        current_dir = os.path.dirname(__file__)
        # Construir la ruta completa utilizando os.path.join
        ruta_carpeta = os.path.join(current_dir, "Capturas", nombre_carpeta)
        # Crear la carpeta
        os.makedirs(ruta_carpeta, exist_ok=True)

        # Configuración de opciones de Chrome
        options = Options()
        options.binary_location = r"C:\driver_google\chrome-win64\chrome.exe"  # Ruta al archivo chrome.exe
        options.add_argument("--no-sandbox")  # Desactiva sandbox si hay problemas de permisos
        options.add_argument("--disable-dev-shm-usage")  # Soluciona problemas de memoria compartida
        options.add_argument("--headless")  # Opcional: ejecuta en modo headless (sin interfaz gráfica)

        # Ruta al ChromeDriver dentro de la carpeta de Chrome
        service = Service(r"C:\driver_google\chrome-win64\chromedriver.exe")

        # Configuración del WebDriver
        driver = webdriver.Chrome(service=service)

        driver.get("https://api-seguridad.sunat.gob.pe/v1/clientessol/4f3b88b3-d9d6-402a-b85d-6a0bc857746a/oauth2/loginMenuSol?lang=es-PE&showDni=true&showLanguages=false&originalUrl=https://e-menu.sunat.gob.pe/cl-ti-itmenu/AutenticaMenuInternet.htm&state=rO0ABXNyABFqYXZhLnV0aWwuSGFzaE1hcAUH2sHDFmDRAwACRgAKbG9hZEZhY3RvckkACXRocmVzaG9sZHhwP0AAAAAAAAx3CAAAABAAAAADdAAEZXhlY3B0AAZwYXJhbXN0AEsqJiomL2NsLXRpLWl0bWVudS9NZW51SW50ZXJuZXQuaHRtJmI2NGQyNmE4YjVhZjA5MTkyM2IyM2I2NDA3YTFjMWRiNDFlNzMzYTZ0AANleGVweA==")
        time.sleep(3)
        # Configura la espera explícita (máximo 20 segundos)
        wait = WebDriverWait(driver, 20)

        driver.maximize_window()

        #DNI BOTON
        DNI = wait.until(EC.presence_of_element_located((By.ID, "btnPorDni")))
        DNI.click()
        time.sleep(10)
        # Espera a que el campo de usuario esté presente en el DOM
        cursor.execute("SELECT DNI FROM CustomersDNI WHERE CustomersID = ?",(id_clienteWhile,))
        Campo_DNI = cursor.fetchone()
        Value = Campo_DNI[0]
        DNI_TXT = wait.until(EC.presence_of_element_located((By.ID, "txtDni")))
        DNI_TXT.send_keys(Value)


        cursor.execute("SELECT Password FROM CustomersDNI WHERE CustomersID = ?",(id_clienteWhile,))
        Campo_PasswordSQL = cursor.fetchone()
        Value = Campo_PasswordSQL[0]
        contra = wait.until(EC.presence_of_element_located((By.ID, "txtContrasena")))
        contra.send_keys(Value)
        contra.send_keys(Keys.ENTER)

        time.sleep(5)
        """BOTON FINALIZAR"""
        # Verifica si el iframe está presente
        iframe_elements = driver.find_elements(By.TAG_NAME, "iframe")
        if iframe_elements:
            driver.switch_to.frame(iframe_elements[0])  # Cambia al primer iframe encontrado

            # Verifica si el botón 'Finalizar' está presente
            boton_finalizar_elements = driver.find_elements(By.ID, "btnFinalizarValidacionDatos")
            if boton_finalizar_elements:
                boton_finalizar_elements[0].click()
                print("Botón 'Finalizar' presionado con éxito.")
            else:
                print("El botón 'Finalizar' no apareció. Continuando...")

            # Regresa al contexto principal
            driver.switch_to.default_content()
        else:
            print("El iframe no está presente. Continuando...")

        time.sleep(2)

        """BOTON Continuar Sin Confirmar"""
        # Verifica si el iframe está presente
        iframe_elements = driver.find_elements(By.TAG_NAME, "iframe")
        if iframe_elements:
            driver.switch_to.frame(iframe_elements[0])  # Cambia al primer iframe encontrado

            # Verifica si el botón 'Continuar Sin Confirmar' está presente
            boton_continuar_elements = driver.find_elements(By.ID, "btnCerrar")
            if boton_continuar_elements:
                boton_continuar_elements[0].click()
                print("Botón 'Continuar Sin Confirmar' presionado con éxito.")
            else:
                print("El botón 'Continuar Sin Confirmar' no apareció. Continuando...")

            # Regresa al contexto principal
            driver.switch_to.default_content()
        else:
            print("El iframe no está presente. Continuando...")

        time.sleep(1)
        

        """BOTON Continuar EMPRESAS"""
        # Ahora localiza el botón
        botonEMPRESAS = wait.until(EC.presence_of_element_located((By.ID, "divOpcionServicio2")))
        botonEMPRESAS.click()

        time.sleep(1)

        """BOTON Continuar MiFraccionamiento"""
        # Ahora localiza el botón
        botonMiFraccionamiento = wait.until(EC.presence_of_element_located((By.ID, "nivel1_16")))
        botonMiFraccionamiento.click()

        """SCROLEAR"""
        driver.execute_script("window.scrollBy(0, 250);")  # 200 píxeles hacia abajo


        time.sleep(2)

        """BOTON Continuar Solicito"""
        # Ahora localiza el botón
        botonSolicito = wait.until(EC.presence_of_element_located((By.ID, "nivel2_16_1")))
        botonSolicito.click()

        time.sleep(2)

        """BOTON Continuar Art36"""
        # Ahora localiza el botón
        botonArt36 = wait.until(EC.presence_of_element_located((By.ID, "nivel3_16_1_1")))
        botonArt36.click()

        time.sleep(2)

        """BOTON Continuar Generacion"""
        # Ahora localiza el botón
        botonGeneracionDeuda = driver.find_element(By.ID, "nivel4_16_1_1_1_2")  # Localizar por el atributo id
        # Desplazar hacia el elemento
        driver.execute_script("arguments[0].scrollIntoView();", botonGeneracionDeuda) 
        # Hacer clic usando JavaScript
        driver.execute_script("arguments[0].click();", botonGeneracionDeuda) #Fuerzo a clickear

        time.sleep(3)

        """TESORO:"""
        # Espera a que el iframe esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "iframeApplication"))  # ID del iframe
        )

        # Cambia al contexto del iframe
        iframe = driver.find_element(By.ID, "iframeApplication")
        driver.switch_to.frame(iframe)

        # Interactúa con los elementos dentro del iframe
        # 1. Seleccionar una opción del menú desplegable
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "entidad"))
        )
        dropdown = driver.find_element(By.NAME, "entidad")
        entidad_selector = Select(dropdown)
        time.sleep(1)
        entidad_selector.select_by_value('1')  # Seleccionar 'ONP'

        # 2. Haz clic en el botón "Enviar Solicitud"
        enviar_boton = driver.find_element(By.NAME, "B1")
        enviar_boton.click()
        driver.switch_to.default_content()

        time.sleep(2)


        """BOTON Continuar Generacion"""
        # Ahora localiza el botón
        botonGeneracionDeuda = driver.find_element(By.ID, "nivel4_16_1_1_1_2")  # Localizar por el atributo id
        # Desplazar hacia el elemento
        driver.execute_script("arguments[0].scrollIntoView();", botonGeneracionDeuda) 
        # Hacer clic usando JavaScript
        driver.execute_script("arguments[0].click();", botonGeneracionDeuda) #Fuerzo a clickear

        time.sleep(3)

        """ESSALUD:"""
        # Espera a que el iframe esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "iframeApplication"))  # ID del iframe
        )

        # Cambia al contexto del iframe
        iframe = driver.find_element(By.ID, "iframeApplication")
        driver.switch_to.frame(iframe)

        # Interactúa con los elementos dentro del iframe
        # 1. Seleccionar una opción del menú desplegable
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "entidad"))
        )
        dropdown = driver.find_element(By.NAME, "entidad")
        entidad_selector = Select(dropdown)
        time.sleep(1)
        entidad_selector.select_by_value('2')  # Seleccionar 'ONP'

        # 2. Haz clic en el botón "Enviar Solicitud"
        enviar_boton = driver.find_element(By.NAME, "B1")
        enviar_boton.click()
        driver.switch_to.default_content()


        time.sleep(2)


        """BOTON Continuar Generacion"""
        # Ahora localiza el botón
        botonGeneracionDeuda = driver.find_element(By.ID, "nivel4_16_1_1_1_2")  # Localizar por el atributo id
        # Desplazar hacia el elemento
        driver.execute_script("arguments[0].scrollIntoView();", botonGeneracionDeuda) 
        # Hacer clic usando JavaScript
        driver.execute_script("arguments[0].click();", botonGeneracionDeuda) #Fuerzo a clickear

        time.sleep(3)

        """ONP:"""
        # Espera a que el iframe esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "iframeApplication"))  # ID del iframe
        )

        # Cambia al contexto del iframe
        iframe = driver.find_element(By.ID, "iframeApplication")
        driver.switch_to.frame(iframe)

        # Interactúa con los elementos dentro del iframe
        # 1. Seleccionar una opción del menú desplegable
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "entidad"))
        )
        dropdown = driver.find_element(By.NAME, "entidad")
        entidad_selector = Select(dropdown)
        time.sleep(1)
        entidad_selector.select_by_value('3')  # Seleccionar 'ONP'

        # 2. Haz clic en el botón "Enviar Solicitud"
        enviar_boton = driver.find_element(By.NAME, "B1")
        enviar_boton.click()
        driver.switch_to.default_content()


        time.sleep(2)





        """BOTON Continuar Formulario Virtual 678"""
        # Ahora localiza el botón
        botonFormulacionVirtual = driver.find_element(By.ID, "nivel4_16_1_1_1_3")  # Localizar por el atributo id
        # Desplazar hacia el elemento
        driver.execute_script("arguments[0].scrollIntoView();", botonFormulacionVirtual) 
        # Hacer clic usando JavaScript
        driver.execute_script("arguments[0].click();", botonFormulacionVirtual) #Fuerzo a clickear

        time.sleep(3)


        """REFREZCAR:"""
        # Espera a que el iframe esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "iframeApplication"))  # ID del iframe
        )

        # Cambia al contexto del iframe
        iframe = driver.find_element(By.ID, "iframeApplication")
        driver.switch_to.frame(iframe)

        # 2. Haz clic en el botón "Enviar Solicitud" (By.NAME, "Brefrecar")
        refrescar_boton = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "Brefrecar"))
        )
        n = 0
        while n < 65:  # Ejecutar por 65 segundos
            refrescar_boton = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "Brefrecar"))
            )
            refrescar_boton.click()
            print("Botón 'Refrescar' presionado.")
            time.sleep(1)  # Esperar 1 segundo entre cada clic
            n += 1
        print("Finalizó el ciclo de 65 segundos de refresco.")

        time.sleep(1)

        """Elaborar Solicitud _ ONP:"""
        # Espera a que la tabla esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'form-table')]"))
        )

        # Localiza la fila donde la entidad es "ONP"
        fila_onp = driver.find_element(By.XPATH, "//tr[td[contains(text(), 'ONP')]]")

        # Dentro de esa fila, localiza el enlace "Elaborar Solicitud"
        enlace_elaborar_solicitud = fila_onp.find_element(By.XPATH, ".//a[contains(text(), 'Elaborar Solicitud')]")

        # Haz clic en el enlace
        enlace_elaborar_solicitud.click()
        print("Clic en 'Elaborar Solicitud' realizado con éxito para ONP.")
        driver.switch_to.default_content()

        time.sleep(10)

        """Boton Aceptar Solicitud _ ONP:"""
        """AQUI EMPIEZA---"""
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "iframeApplication"))  # ID del iframe
            )

            # Cambia al contexto del iframe
            iframe = driver.find_element(By.ID, "iframeApplication")
            driver.switch_to.frame(iframe)
            aceptar_boton = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@widgetid='dijit_form_Button_0' and contains(., 'Aceptar')]"))
            )
            # Desplázate hacia el botón si no está visible
            driver.execute_script("arguments[0].scrollIntoView(true);", aceptar_boton)

            # Haz clic en el botón
            aceptar_boton.click()
            print("Clic en el botón 'Aceptar' realizado con éxito.")


            """Valores Solicitud _ ONP:"""
            # Espera a que el iframe esté presente


            valores_tab = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@widgetid='tipoOperacion_tablist_valores']"))
            )
            valores_tab.click()
            print("Clickeado CORRECTAMENTE")
            time.sleep(8)
        except TimeoutException:
            print("El boton Aceptar no aparecio no apareció, deteniendo el proceso.")

        """AQUI TERMINA---"""
        #Tomar Captura pantalla 1
        
        # Obtener el directorio actual del script
        current_dir = os.path.dirname(__file__)
        # Construir la ruta para Capturas
        ruta_capturas = os.path.join(current_dir, "Capturas", nombre_carpeta)
        nombre_archivo = os.path.join(ruta_capturas, f"ONP_{i}.png")
        screenshot = pyautogui.screenshot()

        # Guardar la captura en un archivo
        screenshot.save(nombre_archivo)
        driver.switch_to.default_content()

        time.sleep(3)

        """BOTON Continuar Formulario Virtual 678"""
        # Ahora localiza el botón
        botonFormulacionVirtual = driver.find_element(By.ID, "nivel4_16_1_1_1_3")  # Localizar por el atributo id
        # Desplazar hacia el elemento
        driver.execute_script("arguments[0].scrollIntoView();", botonFormulacionVirtual) 
        # Hacer clic usando JavaScript
        driver.execute_script("arguments[0].click();", botonFormulacionVirtual) #Fuerzo a clickear

        time.sleep(3)

        """Elaborar Solicitud _ Essalud:"""
        # Espera a que el iframe esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "iframeApplication"))  # ID del iframe
        )

        # Cambia al contexto del iframe
        iframe = driver.find_element(By.ID, "iframeApplication")
        driver.switch_to.frame(iframe)

        # Espera a que la tabla esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'form-table')]"))
        )

        # Localiza la fila donde la entidad es "ESSALUD"
        fila_essalud = driver.find_element(By.XPATH, "//tr[td[contains(text(), 'ESSALUD')]]")

        # Dentro de esa fila, localiza el enlace "Elaborar Solicitud"
        enlace_elaborar_solicitud_essalud = fila_essalud.find_element(By.XPATH, ".//a[contains(text(), 'Elaborar Solicitud')]")

        # Haz clic en el enlace
        enlace_elaborar_solicitud_essalud.click()
        driver.switch_to.default_content()


        time.sleep(10)

        """Boton Aceptar Solicitud _ ESSALUD:"""
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "iframeApplication"))  # ID del iframe
            )

            # Cambia al contexto del iframe
            iframe = driver.find_element(By.ID, "iframeApplication")
            driver.switch_to.frame(iframe)
            aceptar_boton = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@widgetid='dijit_form_Button_0' and contains(., 'Aceptar')]"))
            )
            # Desplázate hacia el botón si no está visible
            driver.execute_script("arguments[0].scrollIntoView(true);", aceptar_boton)

            # Haz clic en el botón
            aceptar_boton.click()
            print("Clic en el botón 'Aceptar' realizado con éxito.")


            """Valores Solicitud _ ESSALUD:"""
            # Espera a que el iframe esté presente


            valores_tab = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@widgetid='tipoOperacion_tablist_valores']"))
            )
            valores_tab.click()
            print("Clickeado CORRECTAMENTE")
            time.sleep(8)

        except TimeoutException:
            print("El boton Aceptar no aparecio no apareció, deteniendo el proceso.")


        #Tomar Captura pantalla 2
        
        # Obtener el directorio actual del script
        current_dir = os.path.dirname(__file__)
        # Construir la ruta para Capturas
        nombre_archivo = os.path.join(ruta_capturas, f"ESSALUD_{i}.png")
        screenshot = pyautogui.screenshot()

        # Guardar la captura en un archivo
        screenshot.save(nombre_archivo)
        driver.switch_to.default_content()

        time.sleep(3)

        """BOTON Continuar Formulario Virtual 678"""
        # Ahora localiza el botón
        botonFormulacionVirtual = driver.find_element(By.ID, "nivel4_16_1_1_1_3")  # Localizar por el atributo id
        # Desplazar hacia el elemento
        driver.execute_script("arguments[0].scrollIntoView();", botonFormulacionVirtual) 
        # Hacer clic usando JavaScript
        driver.execute_script("arguments[0].click();", botonFormulacionVirtual) #Fuerzo a clickear

        time.sleep(3)

        """Elaborar Solicitud _ TESORO:"""
        # Espera a que el iframe esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "iframeApplication"))  # ID del iframe
        )

        # Cambia al contexto del iframe
        iframe = driver.find_element(By.ID, "iframeApplication")
        driver.switch_to.frame(iframe)

        # Espera a que la tabla esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'form-table')]"))
        )

        # Localiza la fila donde la entidad es "ESSALUD"
        fila_TESORO = driver.find_element(By.XPATH, "//tr[td[contains(text(), 'TESORO')]]")

        # Dentro de esa fila, localiza el enlace "Elaborar Solicitud"
        enlace_elaborar_solicitud_TESORO = fila_TESORO.find_element(By.XPATH, ".//a[contains(text(), 'Elaborar Solicitud')]")

        # Haz clic en el enlace
        enlace_elaborar_solicitud_TESORO.click()
        driver.switch_to.default_content()


        time.sleep(10)

        """Boton Aceptar Solicitud _ ESSALUD:"""
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "iframeApplication"))  # ID del iframe
            )

            # Cambia al contexto del iframe
            iframe = driver.find_element(By.ID, "iframeApplication")
            driver.switch_to.frame(iframe)
            aceptar_boton = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@widgetid='dijit_form_Button_0' and contains(., 'Aceptar')]"))
            )
            # Desplázate hacia el botón si no está visible
            driver.execute_script("arguments[0].scrollIntoView(true);", aceptar_boton)

            # Haz clic en el botón
            aceptar_boton.click()
            print("Clic en el botón 'Aceptar' realizado con éxito.")


            """Valores Solicitud _ TESORO:"""
            # Espera a que el iframe esté presente


            valores_tab = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@widgetid='tipoOperacion_tablist_valores']"))
            )
            valores_tab.click()
            print("Clickeado CORRECTAMENTE")
            time.sleep(8)
        except TimeoutException:
            print("El boton Aceptar no aparecio no apareció, deteniendo el proceso.")


        #Tomar Captura pantalla 2
        
        # Obtener el directorio actual del script
        current_dir = os.path.dirname(__file__)
        # Construir la ruta para Capturas
        nombre_archivo = os.path.join(ruta_capturas, f"TESORO_{i}.png")
        screenshot = pyautogui.screenshot()

        # Guardar la captura en un archivo
        screenshot.save(nombre_archivo)
        driver.switch_to.default_content()

        """BUZON_Notificaciones:"""
        
        # Intentar localizar el botón "BUZON"
        botonBuzon = wait.until(EC.presence_of_element_located((By.ID, "aOpcionBuzon")))
        botonBuzon.click()

        time.sleep(6)

        #Tomar Captura pantalla 
        
        # Obtener el directorio actual del script
        current_dir = os.path.dirname(__file__)
        # Construir la ruta para Capturas
        ruta_capturas = os.path.join(current_dir, "Capturas", nombre_carpeta)
        nombre_archivo = os.path.join(ruta_capturas, f"BuzonNotificaciones_{i}.png")
        screenshot = pyautogui.screenshot()

        # Guardar la captura en un archivo
        screenshot.save(nombre_archivo)
        driver.switch_to.default_content()

        time.sleep(3)

        """BUZON_Mensajes:"""
        # Espera a que el iframe esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "iframeApplication"))  # ID del iframe
        )

        # Cambia al contexto del iframe
        iframe = driver.find_element(By.ID, "iframeApplication")
        driver.switch_to.frame(iframe)
        
        # Intentar localizar el botón "BUZON"
        botonBuzon = wait.until(EC.presence_of_element_located((By.ID, "aListMen")))
        botonBuzon.click()

        time.sleep(6)

        #Tomar Captura pantalla 
        
        # Obtener el directorio actual del script
        current_dir = os.path.dirname(__file__)
        # Construir la ruta para Capturas
        ruta_capturas = os.path.join(current_dir, "Capturas", nombre_carpeta)
        nombre_archivo = os.path.join(ruta_capturas, f"BuzonMensajes_{i}.png")
        screenshot = pyautogui.screenshot()

        # Guardar la captura en un archivo
        screenshot.save(nombre_archivo)
        driver.switch_to.default_content()

        time.sleep(3)

        i+=1
        a+=1
        id_clienteWhile+=1

        
        print("TERMINO EL PROCESO")
        driver.quit()


    #FIN DEL while
    conexion.close()

if __name__ == "__main__":
        # Verificar si se pasa un argumento (id_cliente)
        if len(sys.argv) > 1:
            try:
                # Obtener el id_cliente desde los argumentos
                id_cliente = int(sys.argv[1])  # El primer argumento es id_cliente
                buzon(id_cliente)  # Llamar a la función buzon con id_cliente
            except ValueError:
                print("Error: El argumento proporcionado no es un número válido.")
        else:
            print("Error: No se proporcionó id_cliente.")