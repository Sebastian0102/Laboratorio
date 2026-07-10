import json
import yaml

try:
    # 1. Leer el archivo JSON original
    with open('datos.json', 'r') as archivo_json:
        datos = json.load(archivo_json)
    print("-> Archivo datos.json leído correctamente.")

    # 2. Modificar los datos agregando el nuevo puerto (4)
    if 4 not in datos['puertos']:
        datos['puertos'].append(4)
    print("-> Puerto 4 agregado exitosamente.")

    # 3. Guardar el archivo JSON modificado
    with open('datos_modificado.json', 'w') as archivo_json_mod:
        json.dump(datos, archivo_json_mod, indent=4)
    print("-> Archivo datos_modificado.json creado con éxito.")

    # 4. Convertir y guardar como datos.yaml usando pyyaml
    with open('datos.yaml', 'w') as archivo_yaml:
        yaml.dump(datos, archivo_yaml, default_flow_style=False)
    print("-> Archivo datos.yaml creado con éxito.")

except FileNotFoundError:
    print("Error: El archivo datos.json no existe.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
