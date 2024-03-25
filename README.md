# Chatbot with FastAPI, Dialogflow, and MongoDB
Este es un chatbot simple creado con FastAPI, Dialogflow y MongoDB.

## Requisitos
- Python 3.9 or higher
- FastAPI
- Uvicorn
- Google Cloud SDK
- Dialogflow Python SDK
- PyMongo

## Configuración

1. Instalar los paquetes necesarios:
```
pip install -r rquirements.txt
```

2. Cree un nuevo agente de Dialogflow y una nueva intención.

3. Obten la ID de su proyecto de Google Cloud.

4. Crear el archivo `.env` en el directorio raiz del proyecto con las siguientes variables:
```
MONGODB_URI = 'YOUR_CONNECT_STRING'
CREDENTIALS_JSON = '/PATH/TO/YOUR/CREDENTIALS.json'
PROJECT_ID = 'YOUR_PROJECT_ID'
SECRET_KEY = 'YOUR_SECRET_KEY'
```

## Documentación de la API
La aplicación escucha las solicitudes HTTP entrantes en el punto final `/get-message`. Cuando se recibe una solicitud, la aplicación envía el mensaje del usuario a Dialogflow y guarda la intención y la respuesta en MongoDB.

La documentación de la API está disponible en
- http://localhost:8000/docs#/
- http://localhost:8000/redoc

### Ejemplo:
- curl -X POST "http://localhost:8000/get-message?msg=Hello%20world"