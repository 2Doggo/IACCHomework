class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False


class Node:
    def __init__(self, task):
        self.task = task
        self.next = None


class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, name, description):
        # Insertar una nueva tarea al final de la lista
        new_task = Task(name, description)
        new_node = Node(new_task)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_task(self, name):
        # Eliminar una tarea por nombre
        if self.head is None:
            return False

        if self.head.task.name == name:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.task.name == name:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def mark_completed(self, name):
        # Marcar una tarea como completada
        current = self.head
        while current:
            if current.task.name == name:
                current.task.completed = True
                return True
            current = current.next
        return False

    def display_tasks(self):
        # Mostrar todas las tareas
        if self.head is None:
            print("No hay pendientes")
            return

        current = self.head
        while current:
            status = "OK" if current.task.completed else "✗"
            print(f"[{status}] Tarea: {current.task.name}")
            print(f"    Descripción: {current.task.description}")
            current = current.next


# Ejemplo
task_manager = TaskList()

# Agregar algunas tareas
task_manager.add_task("Preparar clase", "Preparar material para la clase de coding")
task_manager.add_task("Revisar pruebas", "Revisar pruebas coeficiente 2")
task_manager.add_task("Actualizar software", "Actualizar software de reconocimiento facial")

print("Lista inicial de tareas:")
task_manager.display_tasks()

print("\nMarcando tarea como completada...")
task_manager.mark_completed("Preparar clase")

print("\nEliminando tarea...")
task_manager.remove_task("Revisar pruebas")

print("\nLista actualizada de tareas:")
task_manager.display_tasks()