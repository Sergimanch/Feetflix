from Contenido import Contenido
from datetime import date
class Juegos(Contenido):
    def __init__(self, id_contenido: int, titulo: str, descripcion: str, genero: str, edad_minima: int, duracion_minutos: int, fecha_estreno: date, plataformas_disponibles : list[str], multijugador : bool, tiempo_jugado : int):
        super().__init__(id_contenido, titulo, descripcion, genero, edad_minima, duracion_minutos, fecha_estreno)
        self.__plataformas_disponibles = plataformas_disponibles ## Movil, Consola o PC
        self.__multijuador = multijugador
        self.__tiempo_jugado = tiempo_jugado
    @property
    def plataformas_disponibles(self):
        return self.__plataformas_disponibles

    @plataformas_disponibles.setter
    def plataformas_disponibles(self, plataformas):
        self.__plataformas_disponibles = plataformas

    @property
    def multijugador(self) -> bool:
        if self.__multijuador == True:
            return ("Multijugador")
        else:
            return("Un jugador")

    @multijugador.setter
    def multijugador(self, multijugador: bool):
        self.__multijugador = multijugador

    @property
    def tiempo_jugado(self) -> int:
        """Devuelve el tiempo jugado total."""
        return self.__tiempo_jugado
        
    def registrar_sesion_juego(self, minutos: int):
        """Suma minutos a tiempo_jugado (sesión de juego)."""
        if minutos > 0:
            self.__tiempo_jugado += minutos

    def reiniciar_tiempo_jugado(self):
        """Pone el tiempo jugado a 0."""
        self.__tiempo_jugado = 0

    def tiempo_jugado_en_horas(self) -> float:
        """
        Devuelve el tiempo jugado en horas (float).
        
        Return : tiempo_jugado en Horas
        """
        return self.__tiempo_jugado / 60
    
    def esta_disponible_en(self, plataforma: str) -> bool:
        """Indica si el juego está disponible en una plataforma concreta."""
        return plataforma.lower() in [p.lower() for p in self.__plataformas_disponibles]

    def añadir_plataforma(self, plataforma: str):
        """Añade una plataforma nueva si no existe ya."""
        if plataforma not in self.__plataformas_disponibles:
            self.__plataformas_disponibles.append(plataforma)
            
    def añadir_valoracion(self, valoracion):
        return super().añadir_valoracion(valoracion)
    
    def es_largo(self) -> bool:
        """
        Considera el juego 'largo' si su duración estimada supera cierto umbral.
        Por ejemplo, más de 20 horas (1200 minutos).
        """
        return self.__duracion is not None and self.__duracion > 1200