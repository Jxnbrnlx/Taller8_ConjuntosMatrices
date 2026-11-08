
# EJERCICIO 2: ANALISIS DE PARTICIPACION EN CURSOS

curso_A = {
    "Ana", "Carlos", "Laura", "Pedro",
    "Sofia", "Andres", "Camila"
}

curso_B = {
    "Laura", "Pedro", "Daniel", "Sofia",
    "Mateo", "Valentina"
}

# 1. Mostrar los estudiantes inscritos en cada curso
print("ESTUDIANTES DEL CURSO A:")
print(curso_A)

print("\nESTUDIANTES DEL CURSO B:")
print(curso_B)

# 2. Calcular la cantidad de estudiantes diferentes
todos = curso_A | curso_B

print("\nCANTIDAD DE ESTUDIANTES DIFERENTES:")
print(len(todos))

# 3. Identificar los estudiantes inscritos en ambos cursos
ambos = curso_A & curso_B

print("\nESTUDIANTES INSCRITOS EN AMBOS CURSOS:")
print(ambos)

# 4. Identificar los estudiantes unicamente del curso A
solo_A = curso_A - curso_B

print("\nESTUDIANTES UNICAMENTE DEL CURSO A:")
print(solo_A)

# 5. Identificar los estudiantes unicamente del curso B
solo_B = curso_B - curso_A

print("\nESTUDIANTES UNICAMENTE DEL CURSO B:")
print(solo_B)

# 6. Estudiantes inscritos en exactamente uno de los cursos
exactamente_uno = curso_A ^ curso_B

print("\nESTUDIANTES INSCRITOS EN EXACTAMENTE UN CURSO:")
print(exactamente_uno)

# 7. Determinar si todos los estudiantes del curso A estan en B
print("\n¿TODOS LOS ESTUDIANTES DEL CURSO A ESTAN EN B?")

if curso_A <= curso_B:
    print("Si, todos estan inscritos en el curso B.")
else:
    print("No, no todos estan inscritos en el curso B.")

# 8. Agregar un estudiante a cualquiera de los cursos
print("\nAGREGAR UN NUEVO ESTUDIANTE")

curso = input("¿A que curso desea agregarlo? (A/B): ").upper()
nombre = input("Ingrese el nombre del estudiante: ").strip()

if curso == "A":
    curso_A.add(nombre)
    print("Estudiante agregado al curso A.")

elif curso == "B":
    curso_B.add(nombre)
    print("Estudiante agregado al curso B.")

else:
    print("Curso no valido.")

# Mostrar los resultados actualizados
if curso == "A" or curso == "B":

    print("\nRESULTADOS ACTUALIZADOS")

    print("Curso A:", curso_A)
    print("Curso B:", curso_B)

    todos = curso_A | curso_B
    print("\nCantidad de estudiantes diferentes:", len(todos))

    ambos = curso_A & curso_B
    print("Estudiantes en ambos cursos:", ambos)

    solo_A = curso_A - curso_B
    print("Estudiantes unicamente en A:", solo_A)

    solo_B = curso_B - curso_A
    print("Estudiantes unicamente en B:", solo_B)

    exactamente_uno = curso_A ^ curso_B
    print("Estudiantes en exactamente uno:", exactamente_uno)

    if curso_A <= curso_B:
        print("Todos los estudiantes de A estan en B.")
    else:
        print("No todos los estudiantes de A estan en B.")
