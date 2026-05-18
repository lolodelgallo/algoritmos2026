"""
Ejercicio 24 - Pila de Personajes MCU
--------------------------------------
Dada una pila de personajes del Marvel Cinematic Universe (MCU)
con nombre y cantidad de películas, se implementan las siguientes
funciones:

  a. Posición de Rocket Raccoon y Groot (posición 1 = cima)
  b. Personajes con más de 5 películas + cantidad
  c. Cuántas películas participó Black Widow
  d. Personajes cuyos nombres empiezan con C, D o G
"""


# ─── Estructura de datos ──────────────────────────────────────────────────────

class PersonajeMCU:
    def __init__(self, nombre, peliculas):
        self.nombre    = nombre
        self.peliculas = peliculas

    def __str__(self):
        return f"{self.nombre:<25} | {self.peliculas} película(s)"

    def __repr__(self):
        return f"PersonajeMCU('{self.nombre}', {self.peliculas})"


# ─── Operaciones de pila ──────────────────────────────────────────────────────

def crear_pila():
    return []

def apilar(pila, personaje):
    pila.append(personaje)

def desapilar(pila):
    if pila_vacia(pila):
        raise IndexError("La pila está vacía.")
    return pila.pop()

def cima(pila):
    if pila_vacia(pila):
        raise IndexError("La pila está vacía.")
    return pila[-1]

def pila_vacia(pila):
    return len(pila) == 0

def tamanio(pila):
    return len(pila)


# ─── Funciones del ejercicio ──────────────────────────────────────────────────

def a_buscar_posicion(pila, nombres_buscados):
    """
    a. Determina en qué posición se encuentran los personajes indicados.
       Posición 1 = cima de la pila.
    :param nombres_buscados: list/set de nombres a buscar
    :return: dict {nombre: posición}
    """
    resultado = {}
    for posicion, personaje in enumerate(reversed(pila), start=1):
        if personaje.nombre in nombres_buscados:
            resultado[personaje.nombre] = posicion
        if len(resultado) == len(nombres_buscados):
            break  # ya encontramos todos, no seguimos
    return resultado


def b_mas_de_cinco_peliculas(pila):
    """
    b. Retorna lista de (nombre, películas) para personajes con > 5 películas.
    """
    return [
        (p.nombre, p.peliculas)
        for p in pila
        if p.peliculas > 5
    ]


def c_peliculas_personaje(pila, nombre_buscado):
    """
    c. Retorna la cantidad de películas de un personaje dado.
       None si no se encuentra.
    """
    for personaje in pila:
        if personaje.nombre.lower() == nombre_buscado.lower():
            return personaje.peliculas
    return None


def d_nombres_por_letra(pila, letras):
    """
    d. Retorna personajes cuyos nombres empiezan con alguna de las letras dadas.
    :param letras: iterable de letras (ej. ['C', 'D', 'G'])
    """
    letras_upper = {l.upper() for l in letras}
    return [p for p in pila if p.nombre[0].upper() in letras_upper]


# ─── Datos de ejemplo ─────────────────────────────────────────────────────────

def cargar_pila_mcu():
    """Carga una pila con personajes del MCU (base → cima)."""
    personajes = [
        # (nombre, películas en las que aparece)
        PersonajeMCU("Nick Fury",         11),
        PersonajeMCU("War Machine",        7),
        PersonajeMCU("Hawkeye",            7),
        PersonajeMCU("Hulk",               8),
        PersonajeMCU("Thor",               8),
        PersonajeMCU("Black Widow",        7),
        PersonajeMCU("Captain America",    7),
        PersonajeMCU("Iron Man",          10),
        PersonajeMCU("Nebula",             6),
        PersonajeMCU("Drax",               4),
        PersonajeMCU("Gamora",             4),
        PersonajeMCU("Star-Lord",          4),
        PersonajeMCU("Groot",              5),
        PersonajeMCU("Rocket Raccoon",     5),
        PersonajeMCU("Scarlet Witch",      5),
        PersonajeMCU("Vision",             3),
        PersonajeMCU("Falcon",             5),
        PersonajeMCU("Ant-Man",            3),
        PersonajeMCU("Doctor Strange",     4),
        PersonajeMCU("Captain Marvel",     3),
        PersonajeMCU("Spider-Man",         6),
        PersonajeMCU("Clint Barton",       1),   # empieza con C
        PersonajeMCU("Deadpool",           3),   # empieza con D
    ]
    pila = crear_pila()
    for p in personajes:
        apilar(pila, p)
    return pila


# ─── Utilidades de visualización ──────────────────────────────────────────────

SEP = "─" * 52

def imprimir_resultado(titulo, contenido):
    print(f"\n{SEP}")
    print(f"  {titulo}")
    print(SEP)
    if isinstance(contenido, list):
        if not contenido:
            print("  (sin resultados)")
        for item in contenido:
            print(f"  • {item}")
    else:
        print(f"  {contenido}")
    print(SEP)


# ─── Demo ─────────────────────────────────────────────────────────────────────

def demo():
    print("╔══════════════════════════════════════════════════╗")
    print("║        EJERCICIO 24 - PILA MCU                   ║")
    print("╚══════════════════════════════════════════════════╝")

    pila = cargar_pila_mcu()
    print(f"\nPila cargada con {tamanio(pila)} personajes.")
    print(f"Cima de la pila: {cima(pila).nombre}")

    # ── a. Posición de Rocket Raccoon y Groot ─────────────────────────────
    buscados    = {"Rocket Raccoon", "Groot"}
    posiciones  = a_buscar_posicion(pila, buscados)
    lineas_a    = [f"{nombre}: posición {pos}" for nombre, pos in posiciones.items()]
    if len(posiciones) < len(buscados):
        no_encontrados = buscados - posiciones.keys()
        lineas_a += [f"{n}: no encontrado en la pila" for n in no_encontrados]
    imprimir_resultado("a. Posición de Rocket Raccoon y Groot", lineas_a)

    # ── b. Personajes con más de 5 películas ─────────────────────────────
    top = b_mas_de_cinco_peliculas(pila)
    lineas_b = [f"{nombre:<25} → {cant} películas" for nombre, cant in top]
    imprimir_resultado("b. Personajes con más de 5 películas", lineas_b)

    # ── c. Películas de Black Widow ───────────────────────────────────────
    bw_count = c_peliculas_personaje(pila, "Black Widow")
    if bw_count is not None:
        resultado_c = f"Black Widow participó en {bw_count} película(s)."
    else:
        resultado_c = "Black Widow no se encuentra en la pila."
    imprimir_resultado("c. Películas de Black Widow", resultado_c)

    # ── d. Nombres que empiezan con C, D o G ─────────────────────────────
    cdg = d_nombres_por_letra(pila, ['C', 'D', 'G'])
    lineas_d = [str(p) for p in cdg]
    imprimir_resultado("d. Personajes cuyos nombres empiezan con C, D o G", lineas_d)


if __name__ == "__main__":
    demo()
