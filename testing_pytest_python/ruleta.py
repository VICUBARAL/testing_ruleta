import random

DIFICULTAD_FACIL = "1"
DIFICULTAD_MEDIA = "2"
DIFICULTAD_ALTA = "3"

TAMANO_TAMBOR_FACIL = 6
TAMANO_TAMBOR_MEDIA = 8
TAMANO_TAMBOR_ALTA = 10

RESULTADO_VICTORIA = 0
RESULTADO_ABANDONO = 1
RESULTADO_MUERTE = 2
RESULTADO_SIGUE = 3

resultados = [0, 0, 0]
seguir_jugando = True

while seguir_jugando:
    dificultad = input('Elija dificultad (1, 2, 3): ')

    tamano_tambor = TAMANO_TAMBOR_FACIL
    if dificultad == DIFICULTAD_MEDIA:
        tamano_tambor = TAMANO_TAMBOR_MEDIA
    elif dificultad == DIFICULTAD_ALTA:
        tamano_tambor = TAMANO_TAMBOR_ALTA

    resultado = RESULTADO_SIGUE
    posicion_bala = random.randint(1, tamano_tambor)
    indice_tambor = 1

    while resultado == RESULTADO_SIGUE:
        disparar = input('Desea disparar (y/n)? ')
        if disparar == 'y' and indice_tambor == posicion_bala:
            print('Habia mala -> MUERTE')
            resultado = RESULTADO_MUERTE
        elif disparar != 'y':
            if indice_tambor != posicion_bala:
                print('CAGON, abandonaste')
                resultado = RESULTADO_ABANDONO
            else:
                print('Dale campeon, vivis otro dia mas')
                resultado = RESULTADO_VICTORIA
        indice_tambor += 1

    resultados[resultado] += 1

    print('Estadisticas:'
        f'\n\tVictorias: {resultados[RESULTADO_VICTORIA]}'
        f'\n\tAbandonos: {resultados[RESULTADO_ABANDONO]}'
        f'\n\tMuertes: {resultados[RESULTADO_MUERTE]}')

    seguir_jugando = input('Otra partida (y/n)? ') == 'y'



#####

class Bala():
    FALLADA = 0
    INTACTA = 1
    EXPLOTADA = 2

    def __init__(self, calibre: int = 9):
        self._calibre = calibre
        self._estado = Bala.INTACTA

    def calibre(self) -> int:
        return self._calibre

    def estado(self) -> int:
        return self._estado

    def establecer_estado(self, nuevo_estado: int):
        self._estado = nuevo_estado


class Persona():
    ESTADO_VIVA = 0
    ESTADO_MUERTA = 1
    ESTADO_CHANCATA = 2

    def __init__(self, nombre: str = 'Jugador'):
        self._nombre = nombre
        self._estado = Persona.ESTADO_VIVA

    def nombre(self) -> str:
        return self._nombre

    def estado(self) -> int:
        return self._estado

    def establecer_estado(self, nuevo_estado: int):
        self._estado = nuevo_estado


class Estadisticas():
    def __init__(self):
        self._estadisticas = {}

    def incrementar(self, nombre_estadistica: str, cuanto_incrementar: int = 1):
        if nombre_estadistica in self._estadisticas:
            self._estadisticas[nombre_estadistica] += cuanto_incrementar
        else:
            self._estadisticas[nombre_estadistica] = cuanto_incrementar
    
    def obtener(self, nombre_estadistica: str) -> int:
        if nombre_estadistica in self._estadisticas:
            return self._estadisticas[nombre_estadistica]
        self._estadisticas[nombre_estadistica] = 0
        return 0

    def reiniciar(self):
        self._estadisticas.clear()


class Revolver():
    def __init__(self, tamano_tambor: int = 6):
        self._tambor = [None] * tamano_tambor
        self._vaina_actual = 1

    def colocar_bala(self, en_vaina: int, bala: Bala = Bala()) -> bool:
        if en_vaina > 0 and en_vaina <= len(self._tambor):
            self._tambor[en_vaina - 1] = bala
            return True
        return False

    def tamano_tambor(self) -> int:
        return len(self._tambor)

    def jalar_gatillo(self) -> Bala:
        bala = None
        if self._hay_bala(self._vaina_actual):
            bala = self._tambor[self._vaina_actual - 1]
            self._tambor[self._vaina_actual - 1] = None
        self._vaina_actual += 1
        if self._vaina_actual > len(self._tambor):
            self._vaina_actual = 1
        return bala

    def _hay_bala(self, en_vaina: int) -> bool:
        return en_vaina > 0 and en_vaina <= len(self._tambor) and self._tambor[en_vaina - 1] is not None

    def vaciar_tambor(self):
        self._tambor = [None] * len(self._tambor)


class Juego():
    def __init__(self, revolver: Revolver, jugador: Persona):
        self._revolver = revolver
        self._jugador = jugador

    def inicializar_juego(self, balas: list, funcion_de_aleatorio: object):
        self._revolver.vaciar_tambor()
        self._jugador.establecer_estado(Persona.ESTADO_VIVA)

        for bala in balas:
            vaina = funcion_de_aleatorio(1, self._revolver.tamano_tambor())
            self._revolver.colocar_bala(vaina, bala)
    
    def accion_jalar_gatillo(self):
        bala = self._revolver.jalar_gatillo()

        if bala is not None:
            self._jugador.establecer_estado(Persona.ESTADO_MUERTA)

    def estado_jugador(self) -> int:
        return self._jugador.estado()



juego = Juego()
juego.inicializar_juego([Bala()], random.randint)




def aleatorio(desde: int, hasta: int):
    return desde

juego = Juego()
juego.inicializar_juego([Bala()], aleatorio)
juego.accion_jalar_gatillo()
assert(juego.estado_jugador() == Persona.ESTADO_MUERTA)


juego.inicializar_juego([Bala()], lambda desde, hasta: 3)
juego.accion_jalar_gatillo()
assert(juego.estado_jugador() == Persona.ESTADO_VIVA)
juego.accion_jalar_gatillo()
assert(juego.estado_jugador() == Persona.ESTADO_VIVA)
juego.accion_jalar_gatillo()
assert(juego.estado_jugador() == Persona.ESTADO_MUERTA)
