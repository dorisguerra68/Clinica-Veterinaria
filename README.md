# Clinica-Veterinaria
# 🐾 Sistema de Gestión - Clínica Veterinaria

Este proyecto es una API RESTful desarrollada para la gestión interna de una clínica veterinaria. Permite administrar de forma eficiente la información de los **Propietarios**, sus **Mascotas** y las **Razas** de los animales, garantizando la integridad de los datos mediante relaciones robustas en la base de datos y validaciones de negocio.

## 🚀 Tecnologías Utilizadas

*   **Backend:** FastAPI (Python 3.14)
*   **ORM / Base de Datos:** SQLAlchemy con PostgreSQL (pgAdmin 4)
*   **Validación de Datos:** Pydantic V2
*   **Pruebas Automatizadas:** Pytest & HTTPX
*   **Servidor ASGI:** Uvicorn

## 📚 Glosario de Librerías Utilizadas y su Propósito

Si eres nuevo en el ecosistema de desarrollo con Python y FastAPI, aquí tienes una explicación sencilla de para qué sirve cada paquete instalado en este proyecto:

1.  **`fastapi`**: Es el framework principal con el que construimos la API. Se encarga de recibir las peticiones de la web, dirigir las rutas y generar automáticamente la pantalla de documentación interactiva (Swagger UI).
2.  **`uvicorn`**: Es el motor o servidor que mantiene nuestra aplicación "viva" y corriendo en la computadora. Al usar el parámetro `--reload`, se da cuenta cuando guardamos un archivo y actualiza el servidor al instante.
3.  **`sqlalchemy`**: Es el ORM (Object Relational Mapper). Actúa como un "traductor" entre Python y PostgreSQL. Gracias a él, podemos crear tablas y hacer consultas usando clases de Python sin necesidad de escribir código SQL nativo.
4.  **`psycopg` (o `psycopg2`)**: Es el conector físico o "puente" que le permite a SQLAlchemy comunicarse y enviar datos directamente al motor de base de datos de PostgreSQL (pgAdmin 4).
5.  **`pydantic`**: Es la librería encargada de la seguridad de las entradas y salidas de datos (los esquemas). Revisa que si pedimos un texto no nos envíen un número, y formatea las respuestas JSON que viajan por la web.
6.  **`pytest`**: Es la herramienta especializada en realizar "pruebas de software". Lee nuestros archivos de prueba, ejecuta las funciones y nos avisa con reportes en verde si el código funciona bien ante diferentes escenarios.
7.  **`httpx` / `httpx2`**: Es un cliente web para Python. En este proyecto lo usa `TestClient` para simular que un usuario real de internet está haciendo clic en los botones de "Crear" o "Borrar", permitiendo testear la API de forma automatizada.


## 📂 Estructura del Proyecto

```text
Clinica-Veterinaria/
│
├── app/
│   ├── config/             # Configuración del entorno (Settings)
│   ├── controllers/        # Lógica de negocio (Controladores)
│   ├── database/           # Conexión a PostgreSQL (Engine y Base)
│   ├── models/             # Modelos de SQLAlchemy (Tablas)
│   ├── routers/            # Endpoints de la API (Rutas)
│   ├── schema_validator/   # Validaciones avanzadas de negocio
│   └── schemas/            # Esquemas de Pydantic (Validación de entrada/salida)
│
├── test/
│   └── test_delete.py      # Pruebas unitarias automatizadas para el CRUD
│
├── main.py                 # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto
```

## 🛠️ Instalación y Configuración

Sigue estos pasos para levantar el proyecto en tu entorno local:

### 1. Clonar el proyecto y activar el entorno virtual
Asegúrate de situarte en la carpeta raíz del proyecto y tener tu entorno virtual activo:
```bash
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar las dependencias
Instala todos los paquetes necesarios definidos en el archivo de requerimientos:
```bash
pip install -r requirements.txt
```

### 3. Configurar la Base de Datos
Asegúrate de tener **pgAdmin 4** encendido y una base de datos creada llamada exactamente `Clinica_Veterinaria`. Verifica tus credenciales de conexión en tu archivo de configuración o `.env`.

## 🖥️ Ejecución del Servidor

Para iniciar el servidor de desarrollo con recarga automática, ejecuta:
```bash
uvicorn main:app --reload
```
Una vez encendido, puedes acceder a la **Documentación Interactiva (Swagger UI)** en la siguiente ruta de tu navegador:
👉 **http://127.0.0.1:8000/docs#/**

## 🧪 Pruebas Automatizadas (Testing)

El proyecto cuenta con pruebas automatizadas integradas con `pytest` para validar la seguridad y estabilidad de las operaciones críticas (como el borrado seguro y el control del error 404).

Para correr los tests, apaga el servidor actual y ejecuta:
```bash
pytest
```

## 🛡️ Características Destacadas para la Evaluación

*   **Manejo de Errores Global:** Implementación de manejadores de excepciones personalizados para evitar respuestas `500` inesperadas y devolver códigos HTTP correctos (`404 Not Found`, `400 Bad Request`).
*   **Modularidad Excepcional:** Clara separación de responsabilidades siguiendo el patrón Controlador-Router-Modelo.
*   **Validaciones Cruzadas:** El sistema impide registrar mascotas si el propietario o la raza asignada no existen previamente en la base de datos.
