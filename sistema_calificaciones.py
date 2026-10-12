
# Proyecto: Sistema de calificaciones

calificaciones = [85, 67, 92, 74, 58]

print("SISTEMA DE CALIFICACIONES")
print("-" * 35)

# 1. Mostrar el vector inicial
print("Calificaciones iniciales:", calificaciones)

# 2. Acceder a una calificación mediante su índice
print("Calificación del índice 2:", calificaciones[2])

# 3. Recorrer el vector y mostrar cada nota
print("\nLista de calificaciones:")
for i, nota in enumerate(calificaciones):
    print(f"Estudiante {i + 1}: {nota}")

# 4. Calcular el promedio
promedio = sum(calificaciones) / len(calificaciones)
print(f"\nPromedio general: {promedio:.2f}")

# 5. Encontrar la nota mayor y la menor
print("Calificación más alta:", max(calificaciones))
print("Calificación más baja:", min(calificaciones))

# 6. Contar aprobados y reprobados
aprobados = 0
reprobados = 0

for nota in calificaciones:
    if nota >= 70:
        aprobados += 1
    else:
        reprobados += 1

print("Estudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)

# 7. Modificar una calificación
print("\nModificación de una calificación")
indice = int(input("Ingrese el índice que desea modificar (0-4): "))

if 0 <= indice < len(calificaciones):
    nueva_nota = float(input("Ingrese la nueva calificación (0-100): "))

    if 0 <= nueva_nota <= 100:
        calificaciones[indice] = nueva_nota
        print("Calificación modificada correctamente.")
    else:
        print("Error: la nota debe estar entre 0 y 100.")
else:
    print("Error: el índice no existe.")

# 8. Mostrar el vector actualizado
print("\nCalificaciones actualizadas:", calificaciones)

nuevo_promedio = sum(calificaciones) / len(calificaciones)
print(f"Nuevo promedio: {nuevo_promedio:.2f}")

print("\nFin del programa.")

    
    