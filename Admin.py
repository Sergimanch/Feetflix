from Persona import Persona

class Admin(Persona):
    def __init__(self, nombre, apellido, dni, direccion, correo_electronico, numero_telefono, password, id_admin, categoria_trabajo):
        super().__init__(nombre, apellido, dni, direccion, correo_electronico, numero_telefono, password)
        self.__id_admin = id_admin
        self.__categoria_trabajo = categoria_trabajo

    @property
    def id_admin(self):
        return self.__id_admin

    @id_admin.setter
    def id_admin(self, valor):
        self.__id_admin = valor

    @property
    def categoria_trabajo(self):
        return self.__categoria_trabajo

    @categoria_trabajo.setter
    def categoria_trabajo(self, valor):
        self.__categoria_trabajo = valor

    def crear_contenido(self, contenido):
        print(f"Admin {self.nombre}: Creando nuevo contenido...")

    def eliminar_contenido(self, id_contenido):
        print(f"Contenido {id_contenido} eliminado correctamente.")

    def editar_contenido(self, id_contenido, nuevos_datos):
        print(f"Editando contenido {id_contenido} con nuevos datos.")

    def bloquear_usuario(self, id_usuario):
        print(f"Usuario {id_usuario} ha sido bloqueado.")

    def desbloquear_usuario(self, id_usuario):
        print(f"Usuario {id_usuario} ha sido desbloqueado.")

    def ver_estadisticas_contenido(self, id_contenido):
        print(f"Mostrando estadísticas (visualizaciones y notas) para: {id_contenido}")

    def listar_usuarios(self):
        print("Listando todos los usuarios del sistema")

    def listar_contenidos(self):
        print("Listando catálogo de Netflix (Películas, Series, Juegos)")