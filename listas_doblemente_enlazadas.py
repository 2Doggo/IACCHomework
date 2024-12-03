class Paquete:
    def __init__(self, codigo, origen, destino, estado="Pendiente"):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.estado = estado

    def __str__(self):
        return f"Paquete {self.codigo}: {self.origen} -> {self.destino} [{self.estado}]"


class Nodo:
    def __init__(self, paquete):
        self.paquete = paquete
        self.siguiente = None
        self.anterior = None


class ListaPaquetes:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_inicio(self, paquete):
        nuevo_nodo = Nodo(paquete)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_final(self, paquete):
        nuevo_nodo = Nodo(paquete)
        if not self.cola:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar_paquete(self, codigo):
        actual = self.cabeza
        while actual:
            if actual.paquete.codigo == codigo:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def buscar_paquete(self, codigo):
        actual = self.cabeza
        while actual:
            if actual.paquete.codigo == codigo:
                return actual.paquete
            actual = actual.siguiente
        return None

    def actualizar_estado(self, codigo, nuevo_estado):
        paquete = self.buscar_paquete(codigo)
        if paquete:
            paquete.estado = nuevo_estado
            return True
        return False

    def mostrar_paquetes(self):
        actual = self.cabeza
        while actual:
            print(actual.paquete)
            actual = actual.siguiente


# Ejemplo de uso
if __name__ == "__main__":
    print("=== INICIANDO PRUEBAS DEL SISTEMA DE GESTIÓN DE PAQUETES ===\n")

    # Crear sistema
    sistema = ListaPaquetes()

    # Verificar sistema vacío
    print("Sistema recién creado")
    print("Mostrando paquetes (debe estar vacío):")
    sistema.mostrar_paquetes()

    # Inserción de paquetes
    print("\nInserción de paquetes")
    print("Insertando paquetes en diferentes posiciones...")

    sistema.insertar_final(Paquete("PKT001", "Chile", "Venezuela", "Pendiente"))
    sistema.insertar_inicio(Paquete("PKT002", "Argentina", "Brasil", "Pendiente"))
    sistema.insertar_final(Paquete("PKT003", "Brasil", "Peru", "Pendiente"))
    sistema.insertar_inicio(Paquete("PKT004", "Peru", "Chile", "Pendiente"))

    print("\nMostrando todos los paquetes:")
    sistema.mostrar_paquetes()

    # Búsqueda de paquetes
    print("\nBúsqueda de paquetes")

    # Buscar paquete existente
    paquete = sistema.buscar_paquete("PKT002")
    print(f"Buscando PKT002: {'Encontrado ->' if paquete else 'No encontrado'}", paquete)

    # Buscar paquete inexistente
    paquete = sistema.buscar_paquete("PKT999")
    print(f"Buscando PKT999: {'Encontrado ->' if paquete else 'No encontrado'}")

    # Actualización de estados
    print("\nActualización de estados")

    # Actualizar estado de paquete existente
    resultado = sistema.actualizar_estado("PKT001", "En tránsito")
    print(f"Actualizando PKT001: {'Éxito' if resultado else 'Fallido'}")

    # Actualizar estado de paquete inexistente
    resultado = sistema.actualizar_estado("PKT999", "Entregado")
    print(f"Actualizando PKT999: {'Éxito' if resultado else 'Fallido'}")

    print("\nMostrando paquetes con estados actualizados:")
    sistema.mostrar_paquetes()

    # Eliminación de paquetes
    print("\nEliminación de paquetes")

    # Eliminar primer paquete
    resultado = sistema.eliminar_paquete("PKT004")
    print(f"Eliminando PKT004 (primer paquete): {'Éxito' if resultado else 'Fallido'}")

    # Eliminar paquete del medio
    resultado = sistema.eliminar_paquete("PKT002")
    print(f"Eliminando PKT002 (paquete del medio): {'Éxito' if resultado else 'Fallido'}")

    # Eliminar último paquete
    resultado = sistema.eliminar_paquete("PKT003")
    print(f"Eliminando PKT003 (último paquete): {'Éxito' if resultado else 'Fallido'}")

    # Intentar eliminar paquete inexistente
    resultado = sistema.eliminar_paquete("PKT999")
    print(f"Eliminando PKT999 (no existe): {'Éxito' if resultado else 'Fallido'}")

    print("\nMostrando paquetes después de eliminaciones:")
    sistema.mostrar_paquetes()

    # Prueba de extremos
    print("\nPrueba de extremos")

    # Eliminar último paquete restante
    sistema.eliminar_paquete("PKT001")
    print("Estado después de eliminar todos los paquetes:")
    sistema.mostrar_paquetes()

    # Insertar en sistema vacío
    sistema.insertar_inicio(Paquete("PKT005", "Chipre", "Jerusalem", "Pendiente"))
    print("\nEstado después de insertar en sistema vacío:")
    sistema.mostrar_paquetes()

    print("=== FINALIZANDO PRUEBAS DEL SISTEMA DE GESTIÓN DE PAQUETES ===")