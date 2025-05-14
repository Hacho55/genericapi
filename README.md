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

## Sistema de Logging

La API incluye un sistema de logging detallado que registra:

### Para todas las peticiones:
- Método y URL de la petición
- Headers completos
- Tiempo de procesamiento
- Código de estado de la respuesta
- Tipo de respuesta

### Para peticiones POST:
- Contenido del body (en formato JSON si es válido)
- Contenido raw del body (si no es JSON válido)

### Para respuestas JSON:
- Contenido completo de la respuesta

## Ejemplos de Uso

### Test de Conexión
```bash
curl http://localhost:8000/test
```

### Enviar y recibir JSON
```bash
curl -X POST http://localhost:8000/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, World!"}'
```

### Ver Headers
```bash
curl http://localhost:8000/headers
```

### Información Detallada
```bash
curl http://localhost:8000/info
```

## Características

- Logging detallado de requests y responses
- Verificación de headers
- Echo de contenido JSON
- Información detallada de conexiones
- Manejo de CORS habilitado
- Documentación automática disponible en `/docs`

## Documentación

La documentación interactiva de la API está disponible en:
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Logs

Los logs se muestran en la consola con el siguiente formato:
```
YYYY-MM-DD HH:MM:SS,mmm - LEVEL - Mensaje
```

Ejemplo de log para una petición POST exitosa:
```
2024-03-19 10:00:00,000 - INFO - Request: POST http://localhost:8000/echo
2024-03-19 10:00:00,000 - INFO - Headers: {"content-type": "application/json", ...}
2024-03-19 10:00:00,000 - INFO - Request Body: {"message": "Hello, World!"}
2024-03-19 10:00:00,000 - INFO - Response status: 200
2024-03-19 10:00:00,000 - INFO - Process time: 0.1234 seconds
2024-03-19 10:00:00,000 - INFO - Response Body (JSON): {"status":"success","received_data":{"message":"Hello, World!"},"timestamp":"2024-03-19T10:00:00.000000"}
```
