from queue import Queue
from datetime import datetime

# Definimos las capacidades maximas por cola
CAPACIDADES_MAXIMAS = {
    'servicios_generales': 50,
    'administracion': 30,
    'facturacion': 40,
    'tecnologia': 25,
    'mercadeo': 20
}

# Inicializar cada una de las colas de servicio
def inicializar_sistema():
    sistema = {}
    for servicio, capacidad in CAPACIDADES_MAXIMAS.items():
        sistema[servicio] = Queue(maxsize=capacidad)
    return sistema


# Creacion e inserción de tickets si la cola no está llena
def insertar_ticket(cola, servicio, descripcion):
    if cola.full():
        return None

    ticket = {
        'timestamp': datetime.now(),
        'servicio': servicio,
        'descripcion': descripcion,
        'estado': 'pendiente'
    }
    cola.put(ticket)
    return ticket


# Atender un ticket
def atender_ticket(cola):
    if cola.empty():
        return None
    return cola.get()


# Verficar si la cola está vacia
def esta_vacia(cola):
    return cola.empty()


# Verificar cola llena
def esta_llena(cola):
    return cola.full()


# Eliminar todos los elementos de una cola
def vaciar_cola(cola):
    while not cola.empty():
        cola.get()


# Retornar el numero de tickets en cola
def consultar_tamano(cola):
    return cola.qsize()


def main():
    print("PRUEBAS\n")

    # Inicializar el sistema
    print("Inicialización")
    sistema_colas = inicializar_sistema()
    for servicio, cola in sistema_colas.items():
        print(f"Cola {servicio} creada con capacidad máxima de {CAPACIDADES_MAXIMAS[servicio]}")
    print()

    # Verificar colas vacías
    print("Verificar colas vacías...")
    for servicio, cola in sistema_colas.items():
        print(f"Cola {servicio} está vacía?: {esta_vacia(cola)}")
    print()

    # Insertar tickets
    print("Insertar tickets de prueba...")
    tickets_prueba = [
        ('administracion', 'ticket a'),
        ('administracion', 'ticket b'),
        ('facturacion', 'ticket a'),
        ('tecnologia', 'ticket a'),
        ('mercadeo', 'ticket a')
    ]

    for servicio, descripcion in tickets_prueba:
        ticket = insertar_ticket(sistema_colas[servicio], servicio, descripcion)
        if ticket:
            print(f"Ticket insertado en {servicio}: {descripcion}")
        else:
            print(f"Error: Cola {servicio} llena")
    print()

    # Verificar tamaños actuales
    print("Estado actual de las colas:")
    for servicio, cola in sistema_colas.items():
        print(f"Cola {servicio}: {consultar_tamano(cola)} tickets en cola")
    print()

    # Atender tickets
    print("Atendiendo tickets...")
    for servicio, cola in sistema_colas.items():
        print(f"\nAtendiendo tickets de {servicio}:")
        ticket = atender_ticket(cola)
        if ticket:
            print(f"Ticket atendido: {ticket['descripcion']}")
            print(f"Tickets restantes: {consultar_tamano(cola)}")
        else:
            print("No hay tickets pendientes")
    print()

    # Llenar una cola específica
    print("Prueba de cola full (ejemplo: administración)...")
    cola_admin = sistema_colas['administracion']
    tickets_insertados = 0
    while not esta_llena(cola_admin):
        insertar_ticket(cola_admin, 'administracion', f'Ticket prueba #{tickets_insertados + 1}')
        tickets_insertados += 1
    print(f"Se insertaron {tickets_insertados} tickets hasta llenar la cola")
    print(f"Cola administración está llena: {esta_llena(cola_admin)}")
    print()

    # Intentar insertar en cola llena
    print("Intentando insertar en cola llena...")
    resultado = insertar_ticket(cola_admin, 'administracion', 'Este ticket no debería subirse')
    print(f"Resultado: {'Fallido' if resultado is None else 'Exitoso'}")
    print()

    # Vaciar una cola
    print("Vaciando cola de administración...")
    print(f"Tickets antes de vaciar: {consultar_tamano(cola_admin)}")
    vaciar_cola(cola_admin)
    print(f"Tickets después de vaciar: {consultar_tamano(cola_admin)}")
    print(f"Cola está vacía?: {esta_vacia(cola_admin)}")
    print()

    print("FIN PRUEBA")



main()