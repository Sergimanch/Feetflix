class Contenido:
    def __init__(self, categoria, nombre, descripcion, duracion, fecha_lanzamiento):
        self.__categoria = categoria
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__duracion = duracion
        self.__fecha_lanzamiento = fecha_lanzamiento

    @property
    def categoria(self) -> str:
        return self.__categoria
    @categoria.setter
    def categoria(self, categoria: str):
        self.__categoria = categoria

    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

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
    def fecha_lanzamiento(self) -> str:
        return self.__fecha_lanzamiento
    @fecha_lanzamiento.setter
    def fecha_lanzamiento(self, fecha_lanzamiento: str):
        self.__fecha_lanzamiento = fecha_lanzamiento    