from queue import Queue, Empty, Full

# Crear cola máxima de 3 elementos
cola = Queue(maxsize=3)

try:
    # Verificar si está vacía
    print("¿Cola vacía?:", cola.empty())

    # Agregar elementos
    cola.put("Cliente 1")
    cola.put("Cliente 2")
    cola.put("Cliente 3")

    # Verificar tamaño actual
    print("Tamaño actual:", cola.qsize())

    # Verificar si está llena
    print("¿Cola llena?:", cola.full())

    # Intentar agregar a cola llena
    cola.put_nowait("Cliente 4")

except Full:
    print("Error: Cola llena")

try:
    # Obtener elementos
    clientes = cola.get()
    print("Atendiendo:", clientes)

    # Intentar obtener un elemento de una cola vacía
    while not cola.empty():
        print("Atendiendo:", cola.get())

    cliente_extra = cola.get_nowait()

except Empty:
    print("Error: Cola vacía")

# Estado final
print("Tamaño final:", cola.qsize())
print("¿Cola vacía?:", cola.empty())