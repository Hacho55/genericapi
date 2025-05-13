# Generic Test API

Esta API está diseñada para realizar pruebas de conexión, verificar encabezados y analizar requests/responses.

## Instalación

1. Asegúrate de tener Python 3.8+ instalado
2. Instala pipenv si no lo tienes: `pip install pipenv`
3. Instala las dependencias: `pipenv install`
4. Activa el entorno virtual: `pipenv shell`
5. Ejecuta la API: `uvicorn app.main:app --reload`

## Endpoints

- `GET /test`: Test de conexión básico
- `POST /echo`: Endpoint que devuelve el contenido JSON recibido
- `GET /headers`: Muestra los headers de la petición
- `GET /info`: Información detallada sobre la petición

## Características

- Logging detallado de requests y responses
- Verificación de headers
- Echo de contenido JSON
- Información detallada de conexiones
