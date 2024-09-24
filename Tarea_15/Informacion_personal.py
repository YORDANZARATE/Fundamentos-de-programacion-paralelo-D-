# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "yordan zarate",
    "edad": 30,
    "ciudad": "QUITO",
    "profesion": "Estudiante"
}

# Acceder y modificar el valor de "ciudad"
print(f"Ciudad original: {informacion_personal['ciudad']}")
informacion_personal["ciudad"] = "QUITO"
print(f"Ciudad modificada: {informacion_personal['ciudad']}")

# Agregar una nueva clave-valor para la "profesion"
informacion_personal["profesion"] = "estudiante"
print(f"Profesión actualizada: {informacion_personal['profesion']}")

# Verificar existencia de la clave "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0996129334"
    print(f"Número de teléfono agregado: {informacion_personal['telefono']}")

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]
    print("Clave 'edad' eliminada.")

# Imprimir el diccionario final
print("\nDiccionario final:")
print(informacion_personal)


