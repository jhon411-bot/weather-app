import json

ARCHIVO = "data.json"

def cargar_datos():
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except:
        return {"historial": [], "favoritos": []}
    
def guardar_datos(data):
    with open(ARCHIVO, "w") as f:
        json.dump(data, f, indent=4)

def guardar_historial(datos_clima):
    data = cargar_datos()
    
    
    for item in data["historial"]:
        if item["ciudad"] == datos_clima["ciudad"]:
            return
    
    data["historial"].append(datos_clima)

    guardar_datos(data)

def agregar_favorito(datos_clima):
    data = cargar_datos()

    for item in data["favoritos"]:
        if item["ciudad"] == datos_clima["ciudad"]:
            print("Ya está en favoritos.")
            return
    
    data["favoritos"].append(datos_clima)
    print("Añadido a favoritos.")

    guardar_datos(data)

def ver_historial():
    data = cargar_datos()
    
    if not data["historial"]:
        print("No hay historial de búsquedas.")
        return
   
    print("\nHistorial de búsquedas:")

    for item in data["historial"]:
        print(f"- {item['ciudad']}: {item['temperatura']}°C, {item['descripcion']} | {item['fecha']}")

def ver_favoritos():
    data = cargar_datos()
    
    if not data["favoritos"]:
        print("No hay favoritos.")
        return
    
    print("\n favoritos:")
    
    for item in data["favoritos"]:
        print(f"- {item['ciudad']}: {item['temperatura']}°C, {item['descripcion']} | {item['fecha']}")

def eliminar_historial():
    data = cargar_datos()
   
    if not data["historial"]:
        print("No hay historial para eliminar.")
        return

    for i, item in enumerate(data["historial"], 1):
        print(f"{i}. {item['ciudad']}")

    try:
        indice = int(input("Selecciona el número del historial a eliminar: ")) - 1
        
        if 0 <= indice < len(data["historial"]):
            eliminado = data["historial"].pop(indice)
            print(f"Historial de {eliminado['ciudad']} eliminado.")
        
        else:
            print("Número inválido.")
    except:
        print("Entrada no válida.")
    
    guardar_datos(data)
    
        