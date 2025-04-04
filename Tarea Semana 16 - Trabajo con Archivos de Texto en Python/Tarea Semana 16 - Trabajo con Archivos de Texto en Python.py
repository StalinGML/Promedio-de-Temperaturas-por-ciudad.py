# Tarea Semana 16: Trabajo con Archivos de Texto en Python
# Alumno: Stalin Mendieta

# Escritura de Archivo de Texto:
# Creamos y abrimos el archivo 'my_notes.txt' en modo escritura ('w').
# Si el archivo no existe, se crea. Si existe, se sobreescribe.
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo.
    file.write("Nombre: Stalin Mendieta\n")
    file.write("Proponerme metas para superarme y aprender mas de la materia:\n")
    file.write("- Estudiar para el examen de programacion\n")
    file.write("- Programación es una de las materias mas importantes dentro mi carrera\n")
    file.write("- No olvidar los fundamentos de python y practicar programas\n")

# Lectura de Archivo de Texto:
# Abrimos el archivo 'my_notes.txt' en modo lectura ('r').
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido línea por línea y lo mostramos en la consola.
    for line in file:
        print(line.strip())  # strip() elimina los saltos de línea al final de cada línea
# El uso de 'with open' automáticamente cierra el archivo después de su uso
# No es necesario llamar a file.close() manualmente
# Fin del programa