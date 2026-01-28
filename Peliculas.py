from datetime import date
from typing import List
from Contenido import Contenido


class Pelicula(Contenido):
    """Clase Película que hereda de Contenido.
    
    Representa una película con atributos específicos como director,
    reparto, idiomas y formatos disponibles.
    """
    
    def __init__(self, id_contenido: int, titulo: str, descripcion: str,
                 genero: str, edad_minima: int, duracion_minutos: int,
                 fecha_estreno: date, director: str, 
                 reparto_principal: List[str], idioma_original: str,
                 formato: str = "HD"):
        # Inicializar la clase padre
        super().__init__(id_contenido, titulo, descripcion, genero,
                        edad_minima, duracion_minutos, fecha_estreno)
        
        # Atributos privados específicos de Película
        self.__director = director
        self.__reparto_principal = reparto_principal
        self.__idioma_original = idioma_original
        self.__subtitulos_disponibles: List[str] = []
        self.__formato = formato
    
    # Properties para director
    @property
    def director(self) -> str:
        return self.__director
    
    @director.setter
    def director(self, director: str):
        self.__director = director
    
    # Properties para reparto_principal
    @property
    def reparto_principal(self) -> List[str]:
        return self.__reparto_principal
    
    @reparto_principal.setter
    def reparto_principal(self, reparto_principal: List[str]):
        self.__reparto_principal = reparto_principal
    
    # Properties para idioma_original
    @property
    def idioma_original(self) -> str:
        return self.__idioma_original
    
    @idioma_original.setter
    def idioma_original(self, idioma_original: str):
        self.__idioma_original = idioma_original
    
    # Properties para subtitulos_disponibles
    @property
    def subtitulos_disponibles(self) -> List[str]:
        return self.__subtitulos_disponibles
    
    @subtitulos_disponibles.setter
    def subtitulos_disponibles(self, subtitulos_disponibles: List[str]):
        self.__subtitulos_disponibles = subtitulos_disponibles
    
    # Properties para formato
    @property
    def formato(self) -> str:
        return self.__formato
    
    @formato.setter
    def formato(self, formato: str):
        self.__formato = formato
    
    # Métodos específicos de Película
    def es_largometraje(self) -> bool:
        """Verifica si la película es un largometraje (>= 60 minutos)."""
        return self.duracion_minutos >= 60
    
    def listar_reparto(self) -> str:
        """Devuelve una cadena con el reparto principal."""
        if not self.__reparto_principal:
            return "Reparto no disponible"
        return ", ".join(self.__reparto_principal)
    
    def esta_disponible_en_idioma(self, idioma: str) -> bool:
        """Verifica si la película está disponible en un idioma específico.
        
        Args:
            idioma: Código o nombre del idioma a verificar
            
        Returns:
            True si está disponible en el idioma original o tiene subtítulos
        """
        idioma_lower = idioma.lower()
        return (self.__idioma_original.lower() == idioma_lower or 
                idioma_lower in [sub.lower() for sub in self.__subtitulos_disponibles])
    
    def añadir_subtitulo(self, idioma: str):
        """Añade un idioma de subtítulos disponible.
        
        Args:
            idioma: Código o nombre del idioma a añadir
        """
        if idioma not in self.__subtitulos_disponibles:
            self.__subtitulos_disponibles.append(idioma)
            print(f"Subtítulos en {idioma} añadidos a {self.titulo}")
        else:
            print(f"Los subtítulos en {idioma} ya están disponibles")
    
    def mostrar_info_detallada(self) -> str:
        """Devuelve información detallada de la película."""
        info_base = super().mostrar_info_detallada()
        tipo = "Largometraje" if self.es_largometraje() else "Cortometraje"
        subtitulos = ", ".join(self.__subtitulos_disponibles) if self.__subtitulos_disponibles else "Ninguno"
        
        info_pelicula = (f"\n--- Información específica de Película ---\n"
                        f"Tipo: {tipo}\n"
                        f"Director: {self.__director}\n"
                        f"Reparto: {self.listar_reparto()}\n"
                        f"Idioma original: {self.__idioma_original}\n"
                        f"Subtítulos disponibles: {subtitulos}\n"
                        f"Formato: {self.__formato}")
        
        return info_base + info_pelicula
    
    def __str__(self) -> str:
        """Representación en string de la película."""
        return f"Película: {self.titulo} ({self.fecha_estreno.year}) - Dir: {self.__director}"
    
    def __repr__(self) -> str:
        """Representación técnica de la película."""
        return (f"Pelicula(id={self.id_contenido}, titulo='{self.titulo}', "
                f"director='{self.__director}', duracion={self.duracion_minutos}min)")
