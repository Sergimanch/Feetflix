class Persona:
    def __init__(self, nombre, apellido, dni, direccion, correo_electronico, numero_telefono, contraseña):
            self.__nombre = nombre
            self.__apellido = apellido
            self.__dni = dni
            self.__direccion = direccion
            self.__correo_electronico = correo_electronico
            self.__numero_telefono = numero_telefono
            self.__contraseña = contraseña
            @property
            def getNombre (self):
                return self.__nombre
            @nombre.setter
            def setNombre(self, nombre):
                self.__nombre = nombre
            @property
            def getApellido(self):
                return self.__apellido
            @apellido.setter
            def setApellido(self, apellido):
                self.__apellido = apellido
            @property
            def getDni(self):
                return self.__dni
            @dni.setter
            def setDni(self, dni):
                self.__dni = dni
            @property
            def getDireccion(self):
                return self.__direccion
            @direccion.setter
            def setDireccion(self, direccion):
                self.__direccion = direccion
            