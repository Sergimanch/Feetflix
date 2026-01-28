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
        
        # Atributos específicos de Película
        self.director = director
        self.reparto_principal = reparto_principal
        self.idioma_original = idioma_original
        self.subtitulos_disponibles: List[str] = []
        self.formato = formato
    
    def es_largometraje(self) -> bool:
        """Verifica si la película es un largometraje (>= 60 minutos)."""
        return self.duracion_minutos >= 60
    
    def listar_reparto(self) -> str:
        """Devuelve una cadena con el reparto principal."""
        if not self.reparto_principal:
            return "Reparto no disponible"
        return ", ".join(self.reparto_principal)
    
    def esta_disponible_en_idioma(self, idioma: str) -> bool:
        """Verifica si la película está disponible en un idioma específico.
        
        Args:
            idioma: Código o nombre del idioma a verificar
            
        Returns:
            True si está disponible en el idioma original o tiene subtítulos
        """
        idioma_lower = idioma.lower()
        return (self.idioma_original.lower() == idioma_lower or 
                idioma_lower in [sub.lower() for sub in self.subtitulos_disponibles])
    
    def añadir_subtitulo(self, idioma: str):
        """Añade un idioma de subtítulos disponible.
        
        Args:
            idioma: Código o nombre del idioma a añadir
        """
        if idioma not in self.subtitulos_disponibles:
            self.subtitulos_disponibles.append(idioma)
            print(f"Subtítulos en {idioma} añadidos a {self.titulo}")
        else:
            print(f"Los subtítulos en {idioma} ya están disponibles")
    
    def mostrar_info_detallada(self) -> str:
        """Devuelve información detallada de la película."""
        info_base = super().mostrar_info_detallada()
        tipo = "Largometraje" if self.es_largometraje() else "Cortometraje"
        subtitulos = ", ".join(self.subtitulos_disponibles) if self.subtitulos_disponibles else "Ninguno"
        
        info_pelicula = (f"\n--- Información específica de Película ---\n"
                        f"Tipo: {tipo}\n"
                        f"Director: {self.director}\n"
                        f"Reparto: {self.listar_reparto()}\n"
                        f"Idioma original: {self.idioma_original}\n"
                        f"Subtítulos disponibles: {subtitulos}\n"
                        f"Formato: {self.formato}")
        
        return info_base + info_pelicula
    
    def __str__(self) -> str:
        """Representación en string de la película."""
        return f"Película: {self.titulo} ({self.fecha_estreno.year}) - Dir: {self.director}"
    
    def __repr__(self) -> str:
        """Representación técnica de la película."""
        return (f"Pelicula(id={self.id_contenido}, titulo='{self.titulo}', "
                f"director='{self.director}', duracion={self.duracion_minutos}min)")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una película de ejemplo
    pelicula1 = Pelicula(
        id_contenido=1,
        titulo="El Padrino",
        descripcion="La saga de la familia Corleone",
        genero="Drama",
        edad_minima=16,
        duracion_minutos=175,
        fecha_estreno=date(1972, 3, 24),
        director="Francis Ford Coppola",
        reparto_principal=["Marlon Brando", "Al Pacino", "James Caan"],
        idioma_original="Inglés",
        formato="4K"
    )
    
    # Añadir subtítulos
    pelicula1.añadir_subtitulo("Español")
    pelicula1.añadir_subtitulo("Francés")
    pelicula1.añadir_subtitulo("Italiano")
    
    # Simular visualizaciones y valoraciones
    pelicula1.reproducir()
    pelicula1.reproducir()
    pelicula1.añadir_valoracion(5)
    pelicula1.añadir_valoracion(5)
    pelicula1.añadir_valoracion(4)
    
    # Mostrar información
    print("\n" + "="*50)
    print("INFORMACIÓN RESUMIDA:")
    print("="*50)
    print(pelicula1.mostrar_info_resumida())
    
    print("\n" + "="*50)
    print("INFORMACIÓN DETALLADA:")
    print("="*50)
    print(pelicula1.mostrar_info_detallada())
    
    # Verificar métodos específicos
    print("\n" + "="*50)
    print("VERIFICACIONES:")
    print("="*50)
    print(f"¿Es largometraje? {pelicula1.es_largometraje()}")
    print(f"¿Disponible en español? {pelicula1.esta_disponible_en_idioma('español')}")
    print(f"¿Disponible en alemán? {pelicula1.esta_disponible_en_idioma('alemán')}")
    print(f"¿Apto para 15 años? {pelicula1.es_apto_para_edad(15)}")
    print(f"¿Apto para 18 años? {pelicula1.es_apto_para_edad(18)}")