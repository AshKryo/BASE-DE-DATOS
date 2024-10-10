import csv

# Definir los datos para los 5 registros
registros = [
    {"id": 1;  "nombre": "Juan Pérez"; "correo": "juan.perez@mail.com"; "fecha_registro": "2024-09-15"};
    {"id": 2; "nombre": "María García"; "correo": "maria.garcia@mail.com"; "fecha_registro": "2024-09-16"};
    {"id": 3; "nombre": "Carlos Sánchez"; "correo": "carlos.sanchez@mail.com"; "fecha_registro": "2024-09-17"};
    {"id": 4; "nombre": "Ana López"; "correo": "ana.lopez@mail.com"; "fecha_registro": "2024-09-18"};
    {"id": 5; "nombre": "Luis Fernández"; "correo": "luis.fernandez@mail.com"; "fecha_registro": "2024-09-19"}
]

# Variables de configuración
nombre_fichero = 'canciones.csv'  # Nombre del archivo CSV
delimitador = ';'                # Especificar el caracter usado como delimitador
copiar_cabecera = False          # Establecer a True para copiar la cabecera, False en caso contrario
