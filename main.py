from data_manager import guardar_historial, agregar_favorito, ver_historial, ver_favoritos, eliminar_historial
from api import obtener_clima
from utils import mostrar_clima
import os 
os.system("cls")

def menu():
    print("\n=== APP DEL CLIMA ===")
    print("1. Consultar clima")
    print("2. Ver historial de búsquedas")
    print("3. Ver favoritos")
    print("4. Eliminar historial")
    print("5. Salir")

while True:
    menu()
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        ciudad = input("Introduce una ciudad: ").strip()
        
        if not ciudad:
            print("Ciudad inválida")
            continue
        
        datos = obtener_clima(ciudad)
        mostrar_clima(datos)

        if datos and "error" not in datos:
            guardar_historial(datos)

            fav = input("¿Agregar a favoritos? (s/n): ").strip().lower()
            if fav == "s":
                agregar_favorito(datos)

    elif opcion == "2":
        ver_historial()

    elif opcion == "3":
        ver_favoritos()

    elif opcion == "4":
        eliminar_historial()

    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida")