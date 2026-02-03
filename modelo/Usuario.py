from modelo.Persona import Persona
from modelo.Contenido import Contenido
class Usuario(Persona):
    def __init__(self,nombre, apellido, dni, direccion, correo_electronico, numero_telefono, password,id_user, nombre_user, idioma_fav, metodo_pago):
            super().__init__(nombre, apellido, dni, direccion, correo_electronico, numero_telefono, password)
            self.__id_user = id_user
            self.__nombre_user = nombre_user
            self.__idioma_fav = idioma_fav
            self.__metodo_pago = metodo_pago
            self.__lista_favoritos = list[Contenido]=[]
            self.__esta_bloqueado = False

    def _comprobar_bloqueo(self) -> bool:
        """
        Devuelve True si el usuario puede usar la cuenta.
        Si está bloqueado, muestra un mensaje y devuelve False.
        """
        if self.__esta_bloqueado:
            print("El usuario está bloqueado y no puede acceder al contenido.")
            return False
        return True
        
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

    @property
    def esta_bloqueado (self)->bool:
        return self.__esta_bloqueado
    @esta_bloqueado.setter
    def esta_bloqueado(self, esta_bloqueado:bool):
        self.__esta_bloqueado = esta_bloqueado

    def añadir_a_lista(self, contenido: Contenido)-> None:
        """Añade un contenido a la lista de favoritos si no está ya."""
        if not self._comprobar_bloqueo():
            return
        if contenido not in self.__lista_favoritos:
            self.__lista_favoritos.append(contenido)
    
    def ver_lista_favoritos(self)->list[Contenido]:
        """Devuelve la lista de contenidos favoritos."""
        if not self._comprobar_bloqueo():
            return []
        return self.__lista_favoritos

    def buscar_contenido_por_titulo(self, titulo: str, catalogo_contenidos: list)->list:
        """
        Busca contenidos por título dentro de un catálogo (lista de Contenido).
        Devuelve una lista con las coincidencias.
        """
        if not self._comprobar_bloqueo():
            return []
        resultados = list[Contenido]=[]
        for c in catalogo_contenidos:
            if titulo.lower() in c.titulo.lower():
                resultados.append(c)
        return resultados

    def filtrar_contenido_por_genero(self, genero: str, catalogo_contenidos: list)->list:
        """
        Filtra contenidos por género dentro de un catálogo (lista de Contenido).
        Devuelve una lista con las coincidencias.
        """
        if not self._comprobar_bloqueo():
            return []
        resultados = list[Contenido]=[]
        for c in catalogo_contenidos:
            if c.genero.lower() == genero.lower():
                resultados.append(c)
        return resultados
    
    def reproducir_contenido(self, contenido: Contenido, edad_usuario: int):
        """
        Reproduce el contenido si es apto para la edad del usuario.
        """
        if not self._comprobar_bloqueo():
            return 
        if contenido.es_apto_para_edad(edad_usuario):
            contenido.reproducir()
        else:
            print("Contenido no apto para tu edad.")

    def valorar_contenido(self, contenido: Contenido, nota: int):
        """
        Añade una valoración al contenido.
        """
        if not self._comprobar_bloqueo():
            return 
        contenido.añadir_valoracion(nota)

    def __str__(self) -> str:
        return f"Usuario {self.__nombre_user} (ID: {self.__id_user})"