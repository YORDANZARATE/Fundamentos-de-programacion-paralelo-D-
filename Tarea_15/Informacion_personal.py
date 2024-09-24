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


#Nuevo programa


# Crear un diccionario con información sobre un libro
informacion_libro = {
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "anio_publicacion": 1967,
    "genero": "Novela"
}

# Acceder y modificar el valor de "genero"
print(f"Género original: {informacion_libro['genero']}")
informacion_libro["genero"] = "Realismo mágico"
print(f"Género modificado: {informacion_libro['genero']}")

# Agregar una nueva clave-valor para el "editorial"
informacion_libro["editorial"] = "Editorial Sudamericana"
print(f"Editorial agregada: {informacion_libro['editorial']}")

# Verificar existencia de la clave "isbn"
if "isbn" not in informacion_libro:
    informacion_libro["isbn"] = "978-3-16-148410-0"
    print(f"Número ISBN agregado: {informacion_libro['isbn']}")

# Eliminar la clave
