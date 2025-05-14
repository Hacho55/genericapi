from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import json
from datetime import datetime

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Generic Test API",
    description="API para realizar pruebas de conexión y análisis de requests/responses",
    version="1.0.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Log de la request
    request_time = datetime.now()
    logger.info(f"Request: {request.method} {request.url}")
    logger.info(f"Headers: {dict(request.headers)}")
    
    # Log del body para peticiones POST
    if request.method == "POST":
        try:
            # Leemos el body
            body = await request.body()
            # Decodificamos el body como JSON si es posible
            try:
                body_str = json.loads(body)
                logger.info(f"Request Body: {body_str}")
            except json.JSONDecodeError:
                logger.info(f"Request Body (raw): {body.decode()}")
            # Importante: necesitamos reconstruir el body para que pueda ser leído nuevamente
            request._body = body
        except Exception as e:
            logger.error(f"Error reading request body: {str(e)}")
    
    # Procesar la request
    response: Response = await call_next(request)
    
    # Log de la response
    process_time = (datetime.now() - request_time).total_seconds()
    logger.info(f"Response status: {response.status_code}")
    logger.info(f"Process time: {process_time:.4f} seconds")
    
    # Log del contenido de la response de manera segura
    if isinstance(response, JSONResponse):
        try:
            logger.info(f"Response Body (JSON): {response.body.decode()}")
        except Exception as e:
            logger.error(f"Error reading JSON response body: {str(e)}")
    else:
        logger.info(f"Response Type: {type(response).__name__}")
    
    return response

@app.get("/test")
async def test_connection():
    """
    Endpoint para probar la conexión básica
    """
    return {
        "status": "success",
        "message": "Conexión exitosa",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/echo")
async def echo_content(request: Request):
    """
    Endpoint que devuelve el contenido JSON recibido
    """
    try:
        body = await request.json()
        return {
            "status": "success",
            "received_data": body,
            "timestamp": datetime.now().isoformat()
        }
    except json.JSONDecodeError:
        return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "message": "Invalid JSON format",
                "timestamp": datetime.now().isoformat()
            }
        )

@app.get("/headers")
async def get_headers(request: Request):
    """
    Endpoint que muestra los headers de la petición
    """
    return {
        "status": "success",
        "headers": dict(request.headers),
        "timestamp": datetime.now().isoformat()
    }

@app.get("/info")
async def get_request_info(request: Request):
    """
    Endpoint que muestra información detallada de la petición
    """
    client_host = request.client.host if request.client else None
    return {
        "status": "success",
        "request_info": {
            "method": request.method,
            "url": str(request.url),
            "client_host": client_host,
            "headers": dict(request.headers),
            "query_params": dict(request.query_params),
            "path_params": request.path_params,
        },
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 