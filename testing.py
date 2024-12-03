class Paquete:
    def __init__(self, codigo, destino, estado="Pendiente"):
        self.codigo = codigo
        self.destino = destino
        self.estado = estado

    def __str__(self):
        return f"Paquete {self.codigo} para {self.destino} - Estado: {self.estado}"


class Nodo:
    def __init__(self, paquete):
        self.paquete = paquete
        self.siguiente = None
        self.anterior = None


class ListaPaquetes:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_paquete(self, codigo, destino, estado="Pendiente"):
        nuevo_paquete = Paquete(codigo, destino, estado)
        nuevo_nodo = Nodo(nuevo_paquete)

        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo


# Actualizar el estado de un paquete
    def actualizar_estado(self, codigo, nuevo_estado):
        actual = self.cabeza
        while actual:
            if actual.paquete.codigo == codigo:
                estado_anterior = actual.paquete.estado
                actual.paquete.estado = nuevo_estado
                print(f"Estado actualizado para paquete {codigo}")
                print(f"Estado anterior: {estado_anterior}")
                print(f"Nuevo estado: {nuevo_estado}")
                return True
            actual = actual.siguiente
        print(f"No se encontró el paquete {codigo}")
        return False

    def mostrar_paquetes(self):
        actual = self.cabeza
        if not actual:
            print("No hay paquetes en la lista")
            return

        print("\nLista de paquetes:")
        while actual:
            print(actual.paquete)
            actual = actual.siguiente


# Ejemplo
lista_paquetes = ListaPaquetes()

print("Insertando paquetes de prueba...")
lista_paquetes.insertar_paquete("P001", "Los Reyes 1220", "Pendiente")
lista_paquetes.insertar_paquete("P002", "Barcelona 435", "Pendiente")
lista_paquetes.insertar_paquete("P003", "Pajaritos 450 Block 4 piso 3 habitacion 12", "Pendiente")
lista_paquetes.insertar_paquete("P004", "Chile", "Pendiente")
lista_paquetes.mostrar_paquetes()

# Actualizar estado de un paquete específico
print("\nActualizando estado del paquete P002...")
lista_paquetes.actualizar_estado("P002", "En tránsito")
# Actualizar estado de un paquete inexistente
lista_paquetes.actualizar_estado("P006", "En tránsito")

# Mostrar estado final
print("\nEstado final de los paquetes:")
lista_paquetes.mostrar_paquetes()
