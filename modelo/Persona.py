class Persona:
    def __init__(self, nombre, apellido, dni, direccion, correo_electronico, numero_telefono, password):
            self.__nombre = nombre
            self.__apellido = apellido
            self.__dni = dni
            self.__direccion = direccion
            self.__correo_electronico = correo_electronico
            self.__numero_telefono = numero_telefono
            self.__password = password
    @property
    def nombre (self)->str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre:str):
        self.__nombre = nombre
    @property
    def apellido(self)->str:
        return self.__apellido
    @apellido.setter
    def apellido(self, apellido: str):
        self.__apellido = apellido
    @property
    def dni(self)-> str:
        return self.__dni
    @dni.setter
    def dni(self, dni:str):
        self.__dni = dni
    @property
    def direccion(self)-> str:
        return self.__direccion
    @direccion.setter
    def direccion(self, direccion : str):
        self.__direccion = direccion
    @property
    def correo_electronico(self)-> str:
        return self.__correo_electronico
    @correo_electronico.setter
    def correo_electronico(self, correo_electronico: str):
        self.__correo_electronico = correo_electronico
    @property
    def numero_telefono(self)-> str:
        return self.__numero_telefono
    @numero_telefono.setter
    def numero_telefono(self, numero_telefono: str):
        self.__numero_telefono = numero_telefono
    @property
    def password(self)-> str:
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    def actualizar_perfil(self, nombre, apellido, dni, direccion, correo_electronico, numero_telefono):
            self.__nombre = nombre
            self.__apellido = apellido
            self.__dni = dni
            self.__direccion = direccion
            self.__correo_electronico = correo_electronico
            self.__numero_telefono = numero_telefono
        return f"Nombre: {self.__nombre}