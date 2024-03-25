from fastapi import FastAPI, HTTPException
from google.cloud import dialogflow_v2 as dialogflow
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

app = FastAPI()
client = MongoClient(os.getenv("MONGODB_URI", 'mongodb://localhost:27017/'))
db = client["dialogflow_db"]
collection = db["messages"]

session_id = str(uuid.uuid4()) # generar una nueva ID de sesión para cada sesión de usuario

@app.get("/health")
def health():
    """# Api health endpoint."""
    return {"Api is up and running"}

@app.post("/get-message")
async def get_message(text: str):
    # Inicializar el cliente Dialogflow
    session_client = dialogflow.SessionsClient(credentials=os.getenv("CREDENTIALS_JSON"))

    # Establecer los parámetros de la sesión de Dialogflow
    session = session_client.session_path(project=os.getenv("PROJECT_ID"), session=session_id)

    # Definir la entrada de consulta para Dialogflow
    text_input = dialogflow.TextInput(text=text, language_code="es-ES")
    query_input = dialogflow.QueryInput(text=text_input)

    # Realizar la solicitud de API de Dialogflowflow
    response = session_client.detect_intent(session=session, query_input=query_input)

    # Comprobar si la respuesta es válida
    if not response.query_result:
        raise HTTPException(status_code=400, detail="Respuesta no válida de Dialogflow")

    # Guardar la intención en la base de datos.
    intent = {
        "intent": response.query_result.intent.display_name,
        "message": response.query_result.fulfillment_text
    }
    collection.insert_one(intent)

    # Devolver el mensaje de respuesta
    return response.query_result.fulfillment_text