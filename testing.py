class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search_iterative(self, value):

        current = self.head
        position = 0

        # Mientras el nodo actual no sea nulo
        while current is not None:
            if current.data == value:
                print(f"Elemento {value} encontrado en la posición {position}")
                return current, position
            current = current.next
            position += 1

        print(f"Elemento {value} no encontrado en la lista")
        return None, -1

    def delete(self, value):
        # Retorna True si se eliminó el elemento, False si no se encontró
        # Verificar si la lista está vacía
        if self.head is None:
            print("La lista está vacía")
            return False

        # Si el elemento a eliminar está en la cabeza
        if self.head.data == value:
            self.head = self.head.next
            print(f"Elemento {value} eliminado (head)")
            return True

        # Buscar el elemento a eliminar
        current = self.head
        while current.next is not None and current.next.data != value:
            current = current.next

        # Si encontramos el elemento, eliminarlo actualizando los enlaces
        if current.next is not None:
            current.next = current.next.next
            print(f"Elemento {value} eliminado")
            return True
        else:
            print(f"Elemento {value} no encontrado")
            return False

    def display(self):
        # Método auxiliar para mostrar la lista
        if self.head is None:
            print("Lista vacía")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Ejemplo
my_list = LinkedList()

# Insertar algunos elementos para probar
print("Lista de ejemplo:")
elements = [5, 10, 15, 20, 25]
for elem in elements:
    my_list.insert(elem)
my_list.display()

# Realizar diferentes búsquedas
print("\nBuscando elemento 15")
node, pos = my_list.search_iterative(15)
if node:
    print(f"Valor del nodo encontrado: {node.data}")

print("\nBuscando el elemento 10")
node, pos = my_list.search_iterative(10)
if node:
    print(f"Valor del nodo encontrado: {node.data}")

print("\nBuscando el elemento 25")
node, pos = my_list.search_iterative(25)
if node:
    print(f"Valor del nodo encontrado: {node.data}")

print("\nBuscando elemento que no existe en la lista):")
node, pos = my_list.search_iterative(7)