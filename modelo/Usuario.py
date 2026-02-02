from modelo.Persona import Persona
class Usuario(Persona):
    def __init__(self,nombre, apellido, dni, direccion, correo_electronico, numero_telefono, password,id_user, nombre_user, idioma_fav, metodo_pago):
            super().__init__(nombre, apellido, dni, direccion, correo_electronico, numero_telefono, password)
            self.__id_user = id_user
            self.__nombre_user = nombre_user
            self.__idioma_fav = idioma_fav
            self.__metodo_pago = metodo_pago
            self.__lista_favoritos = []      # lista de Contenido

    
    @property
    def id_user (self)->str:
        return self.__id_user
    
    @id_user.setter
    def id_user(self, id_user:str):
        self.__id_user = id_user

    @property
    def nombre_user (self)->str:
        return self.__nombre_user
    @nombre_user.setter
    def nombre_user(self, nombre_user:str):
        self.__nombre_user = nombre_user
    

    @property
    def idioma_fav (self)->str:
        return self.__idioma_fav
    @idioma_fav.setter
    def idioma_fav(self, idioma_fav:str):
        self.__idioma_fav = idioma_fav

    @property
    def metodo_pago (self)->str:
        return self.__metodo_pago
    @metodo_pago.setter
    def metodo_pago(self, metodo_pago:str):
        self.__metodo_pago = metodo_pago

    def añadir_a_lista(self, contenido):
        """Añade un contenido a la lista de favoritos si no está ya."""
        if contenido not in self.__lista_favoritos:
            self.__lista_favoritos.append(contenido)
    
    def ver_lista_favoritos(self)->list:
        """Devuelve la lista de contenidos favoritos."""
        return self.__lista_favoritos

    def buscar_contenido_por_titulo(self, titulo: str, catalogo_contenidos: list)->list:
        """
        Busca contenidos por título dentro de un catálogo (lista de Contenido).
        Devuelve una lista con las coincidencias.
        """
        resultados = []
        for c in catalogo_contenidos:
            if titulo.lower() in c.titulo.lower():
                resultados.append(c)
        return resultados

    def filtrar_contenido_por_genero(self, genero: str, catalogo_contenidos: list)->list:
        """
        Filtra contenidos por género dentro de un catálogo (lista de Contenido).
        Devuelve una lista con las coincidencias.
        """
        resultados = []
        for c in catalogo_contenidos:
            if c.genero.lower() == genero.lower():
                resultados.append(c)
        return resultados