import Persona
class Usuario(Persona):
    def __init__(self,id_user, nombre_user, idioma_fav, metodo_pago):
            super().__init__(nombre, apellido, dni, direccion, correo_electronico, numero_telefono, contraseña)
            self.__id_user = id_user
            self.__nombre_user = nombre_user
            self.__idioma_fav = idioma_fav
            self.__metodo_pago = metodo_pago