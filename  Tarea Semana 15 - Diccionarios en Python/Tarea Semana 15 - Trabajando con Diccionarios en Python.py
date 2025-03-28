# Tarea Semana 15 - Stalin Mendieta
# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Stalin Mendieta",
    "edad": 27,
    "ciudad": "Quininde",
    "profesion": "Analista de administración"
}

# Acceder al valor de la clave "ciudad" para modificarlo
informacion_personal["ciudad"] = "Guayaquil"

# Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona
informacion_personal["profesion"] = "Ingeniero en Sistemas y Software"

# Verificar si la clave "telefono" existe en el diccionario. Si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0992208311"

# Eliminar la clave "edad" del diccionario, ya que no es necesaria
del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario final resultante:")
for clave, valor in informacion_personal.items():
    print(f"{clave.capitalize()}: {valor}")
# Fin del programa