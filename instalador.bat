@echo off
:: Título del instalador
title Instalación del proyecto

:: Descargar e instalar Python si no está presente
echo Verificando instalación de Python...
where python >nul 2>nul
if errorlevel 1 (
    echo Python no está instalado. Instalándolo ahora...
    powershell -Command "Start-Process https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe -Wait"
    echo Instale Python y asegúrese de habilitar la opción "Add Python to PATH".
    pause
    exit /b
) else (
    echo Python ya está instalado.
)

:: Crear un entorno virtual
echo Creando entorno virtual...
python -m venv venv
call venv\Scripts\activate

:: Instalar bibliotecas requeridas
echo Instalando bibliotecas requeridas...
pip install -r requirements.txt

:: Finalizar instalación
echo Instalación completada.
echo Puede ejecutar el programa con el comando:
echo    python Start.py
pause
