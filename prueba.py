from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.colors import HexColor

# Crear el lienzo
c = canvas.Canvas("boleta.pdf", pagesize=A4)
ancho_pagina, alto_pagina = A4

"""Bloque 1"""
c.setFillColor(HexColor("#d6eaf8"))  # Gris claro suave
# Dibujar rectángulo
c.rect(9, 713, 577, 72, fill=1)
# Configurar color del texto (negro por defecto)
c.setFillColor(HexColor("#000000"))
# Agregar texto
c.drawString(16, 770, "RUC: ")
c.drawString(16, 753, "Empleador: ")
c.drawString(16, 736, "Periodo: ")
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
c.drawString(90, 647, "40464282") #
c.drawString(33, 629, "Fecha de Ingreso")
c.drawString(245, 664, "Nombre y Apellidos")
c.drawString(156, 647, "ANSAR") #
c.drawString(170, 629, "Tipo de Trabajador")
c.drawString(312, 629, "Regimen Pensionario")
c.drawString(496, 629, "CUSPP")
c.drawString(495, 664, "Situación")
c.drawString(449, 647, "ACTIVO O SUBSIDIADO") 
c.drawString(305, 609, "DL 19990 - SIST") #
c.drawString(305, 596, "NAC DE PENS - ONP") #
c.drawString(158, 601, "CONSTRUCCIÓN CIVIL") #
c.drawString(52, 601, "05/14/2024") #
c.drawString(44, 540, "6") #
c.drawString(113, 540, "0") #
c.drawString(185, 540, "0") #
c.drawString(320, 540, "48") #
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
c.drawString(16, 435, "Ingresos") #
c.drawString(16, 258, "Descuentos") #
c.drawString(16, 241, "Aportes del Trabajador") #
c.drawString(16, 171, "Neto a Pagar") #

# Dibujar rectángulo4

c.setLineWidth(1)
c.rect(9, 114, 577, 36)
c.setLineWidth(0)
c.setFillColor(HexColor("#d6eaf8"))  # Gris claro suave
c.rect(9.5, 132.5, 576, 17, fill=1)
c.setFillColor(HexColor("#000000"))
c.drawString(16, 135, "Aportes del Empleador") #


# Guardar PDF
c.save()