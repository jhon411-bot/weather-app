def obtener_icono(descripcion):
    descripcion = descripcion.lower()
    
    if "nublado" in descripcion:
        return "☁️"
    elif "soleado" in descripcion:
        return "☀️"
    elif "lluvia" in descripcion:
        return "🌧️"
    elif "tormenta" in descripcion:
        return "⛈️"
    elif "nieve" in descripcion:
        return "❄️"
    else:
        return ""

def mostrar_clima(info):
    if not info:
        print("\nError desconocido al obtener el clima.")
        return
    
    if "error" in info:
        print(f"\nError: {info['error']}")
        return
    
    icono = obtener_icono(info['descripcion'])
    
    print("\n--- CLIMA ACTUAL ---")
    print(f" {icono} Ciudad: {info['ciudad']}")
    print(f"🌡️ Temperatura: {info['temperatura']}°C")
    print(f"🤔 Sensación: {info['sensacion']}°C")
    print(f"☁️ Estado: {info['descripcion'].capitalize()}")
    print(f"💧 Humedad: {info['humedad']}%")
    print(f"🌬️ Viento: {info['viento']}m/s")
    print(f"📅 Fecha: {info['fecha']}")