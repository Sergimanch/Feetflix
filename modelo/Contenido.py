from datetime import date

class Contenido:
    def __init__(self, id_contenido: int, titulo: str, descripcion: str, genero: str, edad_minima: int, duracion_minutos: int, fecha_estreno: date):
        self.__id_contenido = id_contenido
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__genero = genero
        self.__edad_minima = edad_minima
        self.__duracion_minutos = duracion_minutos
        self.__fecha_estreno = fecha_estreno
        self.__num_visualizaciones = 0
        self.__valoraciones = []

# Getters y Setters de los atributos de la clase contenido


    @property
    def titulo(self) -> str:
        return self.__titulo
    @titulo.setter
    def nombre(self, titulo: str):
        self.__titulo = titulo

    @property
    def descripcion(self) -> str:
        return self.__descripcion
    @descripcion.setter
    def descripcion(self, descripcion: str):
        self.__descripcion = descripcion

    @property
    def duracion(self) -> str:
        return self.__duracion
    @duracion.setter
    def duracion(self, duracion: str):
        self.__duracion = duracion
        
    @property
    def fecha_estreno(self) -> date:
        return self.__fecha_estreno
    @fecha_estreno.setter
    def fecha_estreno(self, fecha_estreno: date):
        self.__fecha_estreno = fecha_estreno    

    @property
    def titulo(self) -> str:
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo
    
    @property
    def genero(self) -> str:
        return self.__genero
    @genero.setter
    def genero(self, genero: str):
        self.__genero = genero

    @property
    def edad_minima(self) -> int:
        return self.__edad_minima
    @edad_minima.setter
    def edad_minima(self, edad_minima: int):
        self.__edad_minima = edad_minima
    
    @property
    def num_visualizaciones(self) -> int:
        return self.__num_visualizaciones
    @num_visualizaciones.setter
    def num_visualizaciones(self, num_visualizaciones: int):
        self.__num_visualizaciones = num_visualizaciones

    @property
    def valoraciones(self) -> list:
        return self.__valoraciones
    @valoraciones.setter
    def valoraciones(self, valoraciones: list):
        self.__valoraciones = valoraciones

# Metodos de la Clase Contenido
    def es_apto_para_edad(self, edad_usuario: int) -> bool:
        return edad_usuario >= self.__edad_minima
    
    def reproducir(self):
        print(f"Reproduciendo {self.__titulo}...")
        self.__num_visualizaciones += 1

    def añadir_valoracion(self, valoracion: int):
        self.__valoraciones.append(valoracion)

    def calcular_media_valoraciones(self) -> float:
        if not self.__valoraciones:
            return 0.0
        return sum(self.__valoraciones) / len(self.__valoraciones)
    
    def mostrar_info_resumida(self):
        return f"{self.__titulo} ({self.__fecha_estreno.year}) - {self.__genero}"
    
    def mostrar_info_detallada(self):
        info = (
            f"Título: {self.__titulo}\n"
            f"Género: {self.__genero}\n"
            f"Descripción: {self.__descripcion}\n"
            f"Duración: {self.__duracion} minutos\n"
            f"Fecha de Estreno: {self.__fecha_estreno}\n"
            f"Edad Mínima: {self.__edad_minima} años\n"
            f"Número de Visualizaciones: {self.__num_visualizaciones}\n"
            f"Valoración Media: {self.calcular_media_valoraciones():.2f}/10\n"
        )
        return info