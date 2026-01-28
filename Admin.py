from Persona import Persona

class Admin(Persona):
    def __init__(self, nombre, apellido, dni, direccion, correo_electronico, numero_telefono, password, id_admin, categoria_trabajo):
        super().__init__(nombre, apellido, dni, direccion, correo_electronico, numero_telefono, password)
        self.__id_admin = id_admin
        self.__categoria_trabajo = categoria_trabajo
    
    @property
    def id_admin(self) -> str:
        return self.__id_admin

    @id_admin.setter
    def id_admin(self, valor: str):
        self.__id_admin = valor

    @property
    def categoria_trabajo(self) -> str:
        return self.__categoria_trabajo

    @categoria_trabajo.setter
    def categoria_trabajo(self, valor: str):
        self.__categoria_trabajo = valor

    def crear_contenido(self, contenido: object) -> None:
        """Añade un nuevo objeto de contenido al sistema."""
        print(f"Admin {self.nombre}: Creando nuevo contenido...")

    def eliminar_contenido(self, id_contenido: str) -> bool:
        """Elimina contenido por su ID. Devuelve True si tuvo éxito."""
        print(f"Contenido {id_contenido} eliminado correctamente.")
        return True

    def editar_contenido(self, id_contenido: str, nuevos_datos: dict) -> None:
        """Actualiza la información de un contenido existente."""
        print(f"Editando contenido {id_contenido} con nuevos datos.")

    def bloquear_usuario(self, id_usuario: str) -> None:
        """Cambia el estado de un usuario a bloqueado."""
        print(f"Usuario {id_usuario} ha sido bloqueado.")

    def desbloquear_usuario(self, id_usuario: str) -> None:
        """Restaura el acceso a un usuario bloqueado."""
        print(f"Usuario {id_usuario} ha sido desbloqueado.")

    def ver_estadisticas_contenido(self, id_contenido: str) -> None:
        """Muestra métricas de visualización y valoraciones."""
        print(f"Mostrando estadísticas (visualizaciones y notas) para: {id_contenido}")

    def listar_usuarios(self) -> None:
        """Muestra por consola la lista de todos los usuarios."""
        print("Listando todos los usuarios del sistema...")

    def listar_contenidos(self) -> None:
        """Muestra por consola el catálogo completo."""
        print("Listando catálogo de Netflix (Películas, Series, Juegos)...")