from Persona import Persona
class Usuario(Persona):
    def __init__(self,nombre, apellido, dni, direccion, correo_electronico, numero_telefono, password,id_user, nombre_user, idioma_fav, metodo_pago):
            super().__init__(nombre, apellido, dni, direccion, correo_electronico, numero_telefono, password)
            self.__id_user = id_user
            self.__nombre_user = nombre_user
            self.__idioma_fav = idioma_fav
            self.__metodo_pago = metodo_pago
    
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
