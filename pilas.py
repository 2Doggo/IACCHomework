def crear_equipo():
    # Crea y retorna un diccionario vacío para almacenar las pilas de tareas
    return {}



# Agregar un nuevo miembro al equipo con una pila de tareas vacía
def agregar_miembro(equipo, nombre_miembro):
    if nombre_miembro not in equipo:
        equipo[nombre_miembro] = []
        print(f"{nombre_miembro} se ha añadido al equipo.")
    else:
        print(f"{nombre_miembro} ya está en el equipo.")


#Añadir una nueva tarea a la pila de un miembro (PUSH)
def push_tarea(equipo, nombre_miembro, descripcion):
    if nombre_miembro in equipo:
        equipo[nombre_miembro].append(descripcion)
        print(f"Tarea '{descripcion}' asignada a {nombre_miembro}")
    else:
        print(f"Error: {nombre_miembro} no existe en el equipo.")

#Remover y retornar la última tarea asignada a un miembro (POP) o avisar que el miembro no tiene tareas (pila vacía)
def pop_tarea(equipo, nombre_miembro):
    if nombre_miembro in equipo and equipo[nombre_miembro]:
        tarea = equipo[nombre_miembro].pop()
        print(f"Tarea completada por {nombre_miembro}: '{tarea}'")
        return tarea
    else:
        print(f"No hay tareas pendientes para {nombre_miembro}")
        return None

#Mostrar las tareas pendientes de un miembro
def ver_tareas_miembro(equipo, nombre_miembro):
    if nombre_miembro in equipo:
        tareas = equipo[nombre_miembro]
        if tareas:
            print(f"\nTareas pendientes de {nombre_miembro}:")
            # enumerate(reversed(tareas), 1) para mostrar las ultimas tareas añadidas primero
            for i, tarea in enumerate(reversed(tareas), 1):
                print(f"{i}. {tarea}")
            print(f"RECUERDA: completa primero la tarea 1")
        else:
            print(f"{nombre_miembro} no tiene tareas pendientes.")
    else:
        print(f"Error: {nombre_miembro} no existe en el equipo.")

#Muestra todas las tareas pendientes del equipo
def ver_todas_tareas(equipo):
    print("\nEstado actual de tareas del equipo:")
    for miembro in equipo:
        ver_tareas_miembro(equipo, miembro)


def main():
    # Crear el equipo
    equipo1 = crear_equipo()

    # Agregar miembros al equipo
    agregar_miembro(equipo1, "Ana")
    agregar_miembro(equipo1, "Carlos")
    agregar_miembro(equipo1, "Diana")

    # Asignar tareas
    push_tarea(equipo1, "Ana", "Implementar login")
    push_tarea(equipo1, "Ana", "Realizar pruebas unitarias")
    push_tarea(equipo1, "Carlos", "Diseñar base de datos")
    push_tarea(equipo1, "Diana", "Documentar API")
    push_tarea(equipo1, "Diana", "Revisar pull requests")

    # Ver todas las tareas
    ver_todas_tareas(equipo1)

    # Completar algunas tareas
    print("\nCompletando tareas...")
    pop_tarea(equipo1, "Ana")
    pop_tarea(equipo1, "Diana")
    pop_tarea(equipo1, "Diana")

    # Ver el estado actualizado
    ver_todas_tareas(equipo1)


if __name__ == "__main__":
    main()