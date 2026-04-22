import requests
from config import API_KEY, BASE_URL
from datetime import datetime

def obtener_clima(ciudad):
    params = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }
    
    try:
        respuesta = requests.get(BASE_URL, params = params, timeout = 5)
        
        if respuesta.status_code == 404:
            return {"error": "Ciudad no encontrada"}

        if respuesta.status_code != 200:
            return {"error": f"Error al obtener datos"}
        
        data = respuesta.json()

        return {
            "ciudad": data.get("name"),
            "temperatura": data["main"].get("temp"),
            "sensacion": data["main"].get("feels_like"),
            "descripcion": data["weather"][0].get("description"),
            "humedad": data["main"].get("humidity"),
            "viento": data["wind"].get("speed"),
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
    
    except requests.exceptions.Timeout:
        return {"error": "Tiempo de espera agotado"}

    except requests.exceptions.RequestException:
        return {"error": "Error de conexión"}