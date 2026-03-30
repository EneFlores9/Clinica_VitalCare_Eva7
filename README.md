# Sistema de Gestión Clínica - VitalCare

Este proyecto es una aplicación web desarrollada con **Django** y **PostgreSQL** para la gestión de médicos y pacientes.

## Requisitos
* Python 3.14 
* Django 6.02 
* PostgreSQL

## Instalación y Configuración
1. Clonar el repositorio.
2. Crear un entorno virtual: `python -m venv venv`.
3. Activar el entorno: `.\venv\Scripts\activate`.
4. Instalar dependencias: `pip install -r requirements.txt`.
5. Configurar la base de datos en `settings.py`.

## Pruebas Unitarias (Evaluación 7)
Para ejecutar las pruebas de validación de modelos, usa el comando:
```bash
python manage.py test