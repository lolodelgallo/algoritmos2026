"""
Ejercicio 20 - Registro de Movimientos de Robot
------------------------------------------------
Algoritmo que registra los movimientos de un robot (pasos + dirección)
usando una pila. Luego genera la secuencia inversa para volver al origen
por el mismo camino.

El robot puede moverse en 8 direcciones:
norte, sur, este, oeste, noreste, noroeste, sureste, suroeste
"""

# ─── Constantes ───────────────────────────────────────────────────────────────

DIRECCIONES_VALIDAS = {
    'norte', 'sur', 'este', 'oeste',
    'noreste', 'noroeste', 'sureste', 'suroeste'
}

OPUESTOS = {
    'norte':    'sur',
    'sur':      'norte',
    'este':     'oeste',
    'oeste':    'este',
    'noreste':  'suroeste',
    'suroeste': 'noreste',
    'noroeste': 'sureste',
    'sureste':  'noroeste',
}


# ─── Funciones de pila ────────────────────────────────────────────────────────

def crear_pila():
    """Retorna una pila vacía."""
    return []


def apilar_movimiento(pila, pasos, direccion):
    """
    Registra un movimiento en la pila.
    :param pila: lista que actúa como pila
    :param pasos: cantidad de pasos (entero positivo)
    :param direccion: string con una de las 8 direcciones válidas
    """
    direccion = direccion.lower().strip()
    if direccion not in DIRECCIONES_VALIDAS:
        raise ValueError(
            f"Dirección '{direccion}' no válida. "
            f"Opciones: {', '.join(sorted(DIRECCIONES_VALIDAS))}"
        )
    if not isinstance(pasos, int) or pasos <= 0:
        raise ValueError("Los pasos deben ser un entero positivo.")
    pila.append((pasos, direccion))


def pila_vacia(pila):
    return len(pila) == 0


def cima(pila):
    if pila_vacia(pila):
        raise IndexError("La pila está vacía.")
    return pila[-1]


def desapilar(pila):
    if pila_vacia(pila):
        raise IndexError("La pila está vacía.")
    return pila.pop()


# ─── Lógica principal ─────────────────────────────────────────────────────────

def generar_retorno(pila_movimientos):
    """
    Genera la secuencia de movimientos inversa para volver al origen
    por el mismo camino recorrido.
    :param pila_movimientos: pila original (no se modifica)
    :return: lista con los movimientos de retorno
    """
    retorno = []
    # Recorremos la pila de arriba hacia abajo (último movimiento → primero)
    for pasos, direccion in reversed(pila_movimientos):
        retorno.append((pasos, OPUESTOS[direccion]))
    return retorno


# ─── Utilidades de visualización ──────────────────────────────────────────────

def mostrar_movimientos(movimientos, titulo="Movimientos"):
    separador = "─" * 40
    print(f"\n{separador}")
    print(f"  {titulo}")
    print(separador)
    if not movimientos:
        print("  (sin movimientos registrados)")
    for i, (pasos, direccion) in enumerate(movimientos, 1):
        print(f"  {i:2}. {pasos:3} paso(s)  →  {direccion.capitalize()}")
    print(separador)


def ingresar_movimientos_interactivo(pila):
    """Permite al usuario ingresar movimientos desde la consola."""
    print("\n=== Registro de movimientos del robot ===")
    print(f"Direcciones válidas: {', '.join(sorted(DIRECCIONES_VALIDAS))}")
    print("Escribí 'fin' como dirección para terminar.\n")

    while True:
        direccion = input("Dirección: ").strip().lower()
        if direccion == 'fin':
            break
        try:
            pasos = int(input("Pasos: ").strip())
            apilar_movimiento(pila, pasos, direccion)
            print(f"  ✓ Movimiento registrado: {pasos} paso(s) hacia {direccion}\n")
        except (ValueError, TypeError) as e:
            print(f"  ✗ Error: {e}\n")


# ─── Demo ─────────────────────────────────────────────────────────────────────

def demo():
    print("╔══════════════════════════════════════════╗")
    print("║     EJERCICIO 20 - ROBOT CON PILA        ║")
    print("╚══════════════════════════════════════════╝")

    pila = crear_pila()

    # Registrar movimientos de prueba
    movimientos_demo = [
        (3, 'norte'),
        (2, 'este'),
        (5, 'noreste'),
        (1, 'sur'),
        (4, 'noroeste'),
    ]

    print("\nCargando movimientos de ejemplo...")
    for pasos, direccion in movimientos_demo:
        apilar_movimiento(pila, pasos, direccion)

    mostrar_movimientos(pila, "Movimientos registrados (ida)")

    retorno = generar_retorno(pila)
    mostrar_movimientos(retorno, "Secuencia de retorno al origen")

    print("\nEl robot vuelve al punto de partida siguiendo el camino inverso.")


if __name__ == "__main__":
    demo()
    # Para modo interactivo, descomentá las siguientes líneas:
    # pila = crear_pila()
    # ingresar_movimientos_interactivo(pila)
    # mostrar_movimientos(pila, "Movimientos registrados")
    # mostrar_movimientos(generar_retorno(pila), "Retorno al origen")
