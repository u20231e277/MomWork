from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
import tkinter as tk
import subprocess
import sys
import sqlite3
import os

def bucle():

    # Obtener la ruta actual del script
    current_dir = os.getcwd()

    db_folder = "Database_Clientes_Yuvana"
    db_filename = "Database_Constructoras.db"
    DB_PATH = os.path.join(current_dir, db_folder, db_filename)
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute("SELECT TrabajadorID FROM Trabajadores")
    ids_trabajadores = [row[0] for row in cursor.fetchall()] 


    for id_trabajador in ids_trabajadores:   
        def interfaz():
            # Configuración de la ventana principal
            root = tk.Tk()
            root.title("Panel de Control")
            root.geometry("600x900")
            root.config(bg="#0B3D91")  # Fondo azul oscuro

            cursor.execute("SELECT Nombre FROM Trabajadores WHERE TrabajadorID = ?",(id_trabajador,))
            campo_nombres = cursor.fetchone()
            nombres = campo_nombres[0]

            cursor.execute("SELECT DNI FROM Trabajadores WHERE TrabajadorID = ?",(id_trabajador,))
            campo_dni = cursor.fetchone()
            dni = campo_dni[0]
                    

            """NOMBRE DEL TRABAJADOR"""
            labela = tk.Label(root, text=f"{nombres}", font=("Arial", 18), bg="#0B3D91", fg="black")
            labela.pack(pady=18)

            """NOMBRE DEL TRABAJADOR"""
            labelb = tk.Label(root, text=f"{dni}", font=("Arial", 20), bg="#0B3D91", fg="black")
            labelb.pack(pady=18)


            """DIAS TRABAJADOS"""
            label1 = tk.Label(root, text="Dias Trabajados", font=("Arial", 14), bg="#0B3D91", fg="white")
            label1.pack(pady=14)
            entry_dias_trabajados = tk.Entry(root, font=("Arial", 14), width=20)
            entry_dias_trabajados.pack(pady=10)

            """DOMINGOS Y FERIADOS"""
            label2 = tk.Label(root, text="Trabajo domigo ( 1 = si / 0 = no )", font=("Arial", 14), bg="#0B3D91", fg="white")
            label2.pack(pady=14)
            entry_domingo_cantidad = tk.Entry(root, font=("Arial", 14), width=20)
            entry_domingo_cantidad.pack(pady=10)

            label3 = tk.Label(root, text="Trabajo feriados (0 / 1 / 2 / 3)", font=("Arial", 14), bg="#0B3D91", fg="white")
            label3.pack(pady=14)
            entry_feriados_cantidad = tk.Entry(root, font=("Arial", 14), width=20)
            entry_feriados_cantidad.pack(pady=10)

            """RENTA 5TA CATEGORIA"""
            label4 = tk.Label(root, text="Renta 5ta Categoria", font=("Arial", 14), bg="#0B3D91", fg="white")
            label4.pack(pady=14)
            entry_renta_5ta_categoria = tk.Entry(root, font=("Arial", 14), width=20)
            entry_renta_5ta_categoria.pack(pady=10)

            """AFP COMISION SOBRE LA RA"""
            label5 = tk.Label(root, text="AFP comision sobre la RA", font=("Arial", 14), bg="#0B3D91", fg="white")
            label5.pack(pady=14)
            entry_afp_comision_sobre_ra = tk.Entry(root, font=("Arial", 14), width=20)
            entry_afp_comision_sobre_ra.pack(pady=10)

            """VERIFICACION SCTR SALUD"""
            label6 = tk.Label(root, text="Verificacion SCTR Salud ( 1 = si / 0 = no )", font=("Arial", 14), bg="#0B3D91", fg="white")
            label6.pack(pady=14)
            entry_verificacion_sctr_salud = tk.Entry(root, font=("Arial", 14), width=20)
            entry_verificacion_sctr_salud.pack(pady=10)

            # Botón para procesar los datos
            def procesar_datos():
                try:
                    dias_trabajados = int(entry_dias_trabajados.get() or 0)
                    domingos = int(entry_domingo_cantidad.get() or 0)
                    feriados = int(entry_feriados_cantidad.get() or 0)
                    renta_5ta_categoria = int(entry_renta_5ta_categoria.get() or 0)
                    afp_comision_sobre_ra = int(entry_afp_comision_sobre_ra.get() or 0)
                    verificacion_sctr_salud = int(entry_verificacion_sctr_salud.get() or 0)

                    # Otros valores estáticos
                    cursor.execute("SELECT Cargo FROM Trabajadores WHERE TrabajadorID = ?",(id_trabajador,))
                    campo_Cargo = cursor.fetchone()
                    cargo = campo_Cargo[0]
                    
                    cursor.execute("SELECT Sistema_Pensionario FROM Trabajadores WHERE TrabajadorID = ?",(id_trabajador,))
                    campo_sistema_pension = cursor.fetchone()
                    sistema_pension = campo_sistema_pension[0]
                    
                    

        
                    
                    cursor.execute("SELECT Fecha_ingreso FROM Trabajadores WHERE TrabajadorID = ?",(id_trabajador,))
                    campo_fecha_ingreso = cursor.fetchone()
                    fecha_ingreso = campo_fecha_ingreso[0]
                    
                    cursor.execute("SELECT Situacion FROM Trabajadores WHERE TrabajadorID = ?",(id_trabajador,))
                    campo_fecha_ingreso = cursor.fetchone()
                    situacion = campo_fecha_ingreso[0]
                

                    # Calcular domingos y feriados trabajados
                    domingos_feriados = domingos + feriados

                    # Llamar a la función cálculo
                    calculo(
                        dias_trabajados,
                        cargo,
                        domingos_feriados,
                        renta_5ta_categoria,
                        sistema_pension,
                        afp_comision_sobre_ra,
                        verificacion_sctr_salud,
                        dni,
                        nombres,
                        fecha_ingreso,
                        situacion,
                    )
                    # Cerrar la ventana automáticamente
                    root.destroy()
                except ValueError as e:
                    print(f"Error: {e}\nPor favor, ingrese valores numéricos en los campos.")

            button_procesar = tk.Button(root, text="Procesar Datos", command=procesar_datos, font=("Arial", 14), bg="#117A65", fg="white")
            button_procesar.pack(pady=20)

            # Loop de la ventana
            root.mainloop()

        def calculo(dias_trabajados, cargo, domingos_feriados,renta_5ta_categoria_input,sistema_pension_value,afp_comision_Sobre_RA_value,verificacion_SCTR_salud, dni, nombres, fecha_ingreso, situacion):

            """Horas Trabajadas:"""
            horas_trabajadas = dias_trabajados * 8 #Cada dia tiene 8 horas laborales

            """--------------------------------------------------------------------"""
            """Total Ingresos:"""
            #Jornal basico:
            if cargo == "OPERARIO":
                jornal_basico = 86.80
            elif cargo == "OFICIAL":
                jornal_basico = 68.10
            elif cargo == "PEON":
                jornal_basico = 61.30
            
            #jornal semanal:
            jornal_semanal = jornal_basico * dias_trabajados #Lo que gana en 1 semana

            #CTS:
            cts = jornal_semanal * 0.15

            #DOMINICAL:
            dominical_inicial = jornal_semanal / 6  # 16.66666666666667% = 1/6

            if (domingos_feriados == 0):
                dominical = dominical_inicial
            elif (domingos_feriados > 0):
                dominical = dominical_inicial * 3 * int(domingos_feriados)


            #BUC:
            
            if cargo == "OPERARIO":
                buc = jornal_semanal * 0.32
            elif cargo == "OFICIAL":
                buc = jornal_semanal * 0.30
            elif cargo == "PEON":
                buc = jornal_semanal * 0.30

            #Bonificacion Por Altura:
            bonificacion_altura = jornal_semanal * 0.08

            #Gratificacion Proporcional:
            
            if cargo == "OPERARIO":
                gratificacion_proporcional = dias_trabajados * 23.15
            elif cargo == "OFICIAL":
                gratificacion_proporcional = dias_trabajados * 18.16
            elif cargo == "PEON":
                gratificacion_proporcional = dias_trabajados * 16.35

            #Vacaciones Truncas:
            vacaciones_truncas = jornal_semanal * 0.10

            #Movilidad:
            movilidad = 8.6 * dias_trabajados

            #Bonificacion Extraordinario Ley 29351:
            bonificacion_extraordinario_ley_29351 = gratificacion_proporcional * 0.09

            #TOTAL INGRESOS:
            total_ingresos_ = jornal_semanal + cts + dominical + buc + bonificacion_altura + gratificacion_proporcional + vacaciones_truncas + movilidad + bonificacion_extraordinario_ley_29351

            """--------------------------------------------------------------------"""
            """Total egresos:"""
            #Conafovicer:
            conafovicer = (jornal_semanal + dominical) * 0.02

            #Renta de Quinta Categoria:
            renta_5ta_categoria = renta_5ta_categoria_input

            #Sacar de la base de datos si es ONP o AFP el trabajador
            
            sistema_pension = sistema_pension_value
            #Total Egresos caso ONP:
            if  sistema_pension == "ONP":
                onp = jornal_semanal * 0.13
                total_egresos_ = conafovicer + onp + renta_5ta_categoria
            #Total Egresos caso AFP:
            elif sistema_pension == "AFP":
                afp_aportacion_obligatoria = jornal_semanal * 0.10
                afp_prima_seguro = jornal_semanal * 0.017
                afp_comision_Sobre_RA = afp_comision_Sobre_RA_value
                total_egresos_ = conafovicer + afp_aportacion_obligatoria + afp_prima_seguro + afp_comision_Sobre_RA + renta_5ta_categoria

            """--------------------------------------------------------------------"""
            """Total Aporte:"""
            #Essalud:
            essalud_ = (jornal_semanal + dominical + buc + vacaciones_truncas ) * 0.09 

            if verificacion_SCTR_salud == 1:
                SCTR_salud = (jornal_semanal + dominical + buc + vacaciones_truncas + bonificacion_altura) * 0.0153
                total_aporte = essalud_ + SCTR_salud
            
            elif verificacion_SCTR_salud == 0:
                total_aporte = essalud_
            
            """--------------------------------------------------------------------"""
            """Total NETO:"""
            total_neto_ = total_ingresos_ - total_egresos_

            """--------------------------------------------------------------------"""
            """Datos para la Boleta:"""
            #Periodo:
            fecha_actual = datetime.now()
            periodo_ = fecha_actual.strftime("%m-%Y")
            

            def generar_boleta():
                # Obtener el directorio actual del script
                current_dir = os.path.dirname(__file__)
                # Construir la ruta completa utilizando os.path.join
                ruta_carpeta = os.path.join(current_dir, "Boletas")
                # Crear la carpeta
                os.makedirs(ruta_carpeta, exist_ok=True)

                # Crear el lienzo
                ruta_pdf = os.path.join(ruta_carpeta, f"boleta_{nombres}.pdf")
                c = canvas.Canvas(ruta_pdf, pagesize=A4)
                ancho_pagina, alto_pagina = A4

                """Bloque 1"""
                c.setFillColor(HexColor("#d6eaf8"))  # Gris claro suave
                # Dibujar rectángulo
                c.rect(9, 713, 577, 72, fill=1)
                # Configurar color del texto (negro por defecto)
                c.setFillColor(HexColor("#000000"))
                # Agregar texto
                c.drawString(16, 770, "RUC: 20610400028")
                c.drawString(16, 753, "Empleador: CONSORCIO SICAYA II")
                c.drawString(16, 736, "Periodo: ")
                c.drawString(73, 736, f"{periodo_}")
                c.drawString(16, 719, "PDT Planilla Electrónica - PLAME            Número de Orden : ")

                c.setFillColor(HexColor("#d5f5e3"))  # Gris claro suave

                # Dibujar rectángulo2
                c.rect(9, 484, 577, 212)
                # Dibujar rectángulo
                c.rect(9, 660, 577, 36, fill=1)
                # Dibujar rectángulo
                c.rect(9, 626, 577, 17, fill=1)
                # Dibujar rectángulo
                c.rect(9, 554, 577, 36, fill=1)
                # Dibujar rectángulo
                c.rect(9, 501, 577, 36, fill=1)
                #VERTICAL
                # Dibujar línea
                c.line(444, 484, 444, 696)
                # Dibujar línea
                c.line(152, 537, 152, 696)
                # Dibujar línea
                c.line(293, 537, 293, 643)
                # Dibujar línea
                c.line(82, 537, 82, 590)
                # Dibujar línea
                c.line(223, 537, 223, 590)
                # Dibujar línea
                c.line(515, 537, 515, 572)
                # Dibujar línea
                c.line(363, 537, 363, 572)
                # Dibujar línea
                c.line(82, 643, 82, 678)
                # Dibujar línea
                c.line(82, 483, 82, 519)
                # Dibujar línea
                c.line(363, 483, 363, 519)
                #HORIZONTAL
                # Dibujar línea
                c.line(293, 572, 586, 572)
                # Dibujar línea
                c.line(9, 678, 152, 678)
                # Dibujar línea
                c.line(9, 519, 444, 519)
                #TEXTO:
                c.setFillColor(HexColor("#000000"))
                c.drawString(16, 682, "Documento Identidad")
                c.drawString(33, 664, "Tipo")
                c.drawString(95, 664, "Número")
                c.drawString(33, 647, "DNI")
                c.drawString(90, 647, f"{dni}") #
                c.drawString(33, 629, "Fecha de Ingreso")
                c.drawString(245, 664, "Nombre y Apellidos")
                c.drawString(156, 647, f"{nombres}") #
                c.drawString(170, 629, "Tipo de Trabajador")
                c.drawString(312, 629, "Regimen Pensionario")
                c.drawString(496, 629, "CUSPP")
                c.drawString(495, 664, "Situación")
                c.drawString(449, 647, f"{situacion}") 
                c.drawString(305, 609, "DL 19990 - SIST") #
                c.drawString(305, 596, "NAC DE PENS - ONP") #
                c.drawString(158, 601, "CONSTRUCCIÓN CIVIL") #
                c.drawString(52, 601, f"{fecha_ingreso}") #
                c.drawString(44, 540, f"{dias_trabajados}") #
                c.drawString(113, 540, "0") #
                c.drawString(185, 540, "0") #
                c.drawString(320, 540, f"{horas_trabajadas}") #
                c.drawString(226, 540, "Domicialado") #
                c.drawString(483, 575, "Sobretiempo") #
                c.drawString(527, 557, "Minutos") #
                c.drawString(448, 557, "Total Horas") #
                c.drawString(382, 557, "Minutos") #
                c.drawString(296, 557, "Total Horas") #
                c.drawString(319, 575, "Jornada Ordinaria") #
                c.drawString(232, 557, "Condición") #
                c.drawString(156, 557, "subsidiados") #
                c.drawString(90, 557, "Laborados") #
                c.drawString(19, 557, "Laborados") #
                c.drawString(177, 575, "Días") #
                c.drawString(98, 575, "Días no") #
                c.drawString(35, 575, "Días") #
                c.drawString(138, 523, "Motivo de Suspensión de Labores") #
                c.drawString(451, 523, "Otros empleadores por") #
                c.drawString(35, 504, "Tipo") #
                c.drawString(203, 504, "Motivo") #
                c.drawString(382, 504, "N° Días") #
                c.drawString(450, 505, "Rentas de 5ta Categoría") #
                c.drawString(491, 488, "No tiene") #

                # Dibujar rectángulo3
                #HORIZONTAL
                c.setFillColor(HexColor("#d5f5e3"))  # Gris claro suave
                c.rect(9, 167, 577, 299)
                c.rect(9, 449, 577, 17,fill=1)
                # Dibujar línea
                c.setFillColor(HexColor("#000000"))
                c.drawString(29, 452, "Código") #
                c.drawString(195, 452, "Conceptos") #
                c.drawString(373, 452, "Ingresos S/.") #
                c.drawString(454, 452, "Desc. S/.") #
                c.drawString(529, 452, "Neto S/.") #


                c.line(81, 449, 81, 466)
                c.line(363, 449, 363, 466)
                c.line(444, 449, 444, 466)
                c.line(516, 449, 516, 466)
                #RECTANGULOS INTERNOS:
                # Configurar color de relleno (gris claro, plomo suave)
                c.setFillColor(HexColor("#d6eaf8"))  # Gris claro suave
                # Desactivar borde configurando el grosor del trazo a 0
                c.setLineWidth(0)

                c.rect(9.5, 431.5, 576, 17, fill=1)
                c.rect(9.5, 236, 576, 36, fill=1)
                c.rect(9.5, 167.5, 576, 17, fill=1)
                c.setFillColor(HexColor("#000000"))
                #INGRESOS:
                c.drawString(16, 435, "Ingresos") #
                c.setFont("Helvetica", 10)  # Cambia "Helvetica" por la fuente deseada y 10 por el tamaño de letra
                c.drawString(85, 416, f"VACACIONES TRUNCAS:                                                                    {vacaciones_truncas:.3f}") #
                c.drawString(85, 399, f"REMUNERAC. DÍA DESCANSO Y FERIADOS:                                   {dominical:.3f}") #
                c.drawString(85, 382, f"REMUNERACIÓN O JORNAL BÁSICO:                                               {jornal_semanal:.3f}") #
                c.drawString(85, 365, f"BONIF. PRODUCCIÓN,ALTURA,TURNO,ETC.                                   {bonificacion_altura:.3f}") #
                c.drawString(85, 348, f"BONIFICACION UNIFICADA DE CONSTRUCC                                  {buc:.3f}") #
                c.drawString(85, 331, f"BONIF. EXTRAORD. PROPORC. LEY 29351 y 30334                        {bonificacion_extraordinario_ley_29351:.3f}") #
                c.drawString(85, 314, f"GRATIFIC. PROPORCIONAL - LEY 29351 Y 30334                           {gratificacion_proporcional:.3f}") #
                c.drawString(85, 297, f"COMPENSACIÓN TIEMPO DE SERVICIOS                                        {cts:.3f}") #
                c.drawString(85, 280, f"MOV SUPEDIT A ASIST CUBRE TRASLADO                                      {movilidad:.3f}") #
                    
                c.setFont("Helvetica", 12)  # Fuente y tamaño inicial
                c.drawString(16, 258, "Descuentos") #
                c.drawString(16, 241, "Aportes del Trabajador") #

                c.setFont("Helvetica", 10)  # Cambia "Helvetica" por la fuente deseada y 10 por el tamaño de letra
                c.drawString(85, 222, f"CONAFOVICER                                                                                                               {conafovicer:.3f}") #
                c.drawString(85, 205, f"RENTA QUINTA CATEGORÍA RETENCIONES                                                               {renta_5ta_categoria:.3f}") #
                if (sistema_pension == "ONP"):    
                    c.drawString(85, 188, f"SISTEMA NAC. DE PENSIONES DL 19990                                                                     {onp:.3f}") #
                elif (sistema_pension == "AFP"):
                    c.drawString(85, 188, f"AFP APORTACION OBLIGATORIA                                                                                {afp_aportacion_obligatoria:.3f}") #

                c.setFont("Helvetica", 12)  # Fuente y tamaño inicial
                c.drawString(16, 171, "Neto a Pagar") #
                

                # Dibujar rectángulo4

                c.setLineWidth(1)
                c.rect(9, 96, 577, 54)
                c.setLineWidth(0)
                c.setFillColor(HexColor("#d6eaf8"))  # Gris claro suave
                c.rect(9.5, 132.5, 576, 17, fill=1)
                c.setFillColor(HexColor("#000000"))
                c.drawString(16, 135, "Aportes del Empleador") #
                c.setFont("Helvetica", 10)  # Cambia "Helvetica" por la fuente deseada y 10 por el tamaño de letra
                c.drawString(85, 119, f"ESSALUD(REGULAR CBSSP AGRAR/AC)TRAB                                                                                       {essalud_:.3f}")
                if (verificacion_SCTR_salud == 1):
                    c.drawString(85, 102, f"SCTR SALUD                                                                                                                                               {SCTR_salud:.3f}")
            


                # Guardar PDF
                c.save()
                
                

            # Ejecutar la función
            generar_boleta()

        interfaz()
        
        print("TERMINO EL PROCESO")
        #FIN DEL while

        
    
    conexion.close()



bucle()
