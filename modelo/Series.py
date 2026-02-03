from modelo.Contenido import Contenido
from datetime import date

class Series(Contenido):
    def __init__(self, id_contenido: int, titulo: str, descripcion: str, genero: str, edad_minima: int, duracion_minutos: int, fecha_estreno: date, num_temporadas: int, en_emision: bool):
        super().__init__(id_contenido, titulo, descripcion, genero, edad_minima, duracion_minutos, fecha_estreno )
        self.__num_temporadas = num_temporadas
        self.__en_emision = en_emision
        self.__temporada_actual = 1
        # Diccionario: {nº_temporada: nº_episodios}
        self.__episodios_por_temporada = {} 

    @property
    def num_temporadas(self) -> int:
        return self.__num_temporadas

    @num_temporadas.setter
    def num_temporadas(self, valor: int):
        self.__num_temporadas = valor

    @property
    def episodios_por_temporada(self) -> dict:
        return self.__episodios_por_temporada

    @property
    def en_emision(self) -> bool:
        return self.__en_emision

    @property
    def temporada_actual(self) -> int:
        return self.__temporada_actual


    def total_episodios(self) -> int:
        """ Devuelve el total de episodios en todas las temporadas """
        return sum(self.__episodios_por_temporada.values())

    def marcar_como_en_emision(self):
        """ Marca la serie como en emisión """
        self.__en_emision = True
        print(f"La serie '{self.nombre}' está ahora en emisión.")

    def marcar_como_finalizada(self):
        """ Marca la serie como finalizada """
        self.__en_emision = False
        print(f"La serie '{self.nombre}' ha finalizado.")

    def añadir_temporada(self, num_episodios: int):
        """ Añade una nueva temporada con el número de episodios especificado """
        self.__num_temporadas += 1
        self.__episodios_por_temporada[self.__num_temporadas] = num_episodios
        print(f"Temporada {self.__num_temporadas} añadida con {num_episodios} episodios.")

    def obtener_num_episodios(self, temporada: int) -> int:
        """ Uso de excepciones para manejo de errores y devuelve el número de episodios de una temporada dada """
        if temporada not in self.__episodios_por_temporada:
            raise ValueError(f"La temporada {temporada} no existe en esta serie.")
        return self.__episodios_por_temporada[temporada]
    def reproducir_episodio(self, temporada: int, episodio: int):
        self.reproducir()
        print(f"Reproduciendo Temporada {temporada}, Episodio {episodio} de '{self.titulo}'.")
        
    def añadir_valoracion(self, valoracion):
        return super().añadir_valoracion(valoracion)
    
    def siguiente_episodio(self, temporada: int, episodio: int) -> tuple:
        """ Lógica simple: si el episodio actual es el último de la temporada, pasa a la siguiente temporada """
        if episodio < self.__episodios_por_temporada.get(temporada, 0):
            return (temporada, episodio + 1)
        elif temporada < self.__num_temporadas:
            return (temporada + 1, 1)
        else:
            return (temporada, episodio) # Ya es el ultimo episodio de la serie