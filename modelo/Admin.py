from modelo.Persona import Persona
from modelo.Contenido import Contenido
from modelo.Usuario import Usuario
class Admin(Persona):
    def __init__(self, nombre, apellido, dni, direccion, correo_electronico, numero_telefono, password, id_admin, categoria_trabajo):
        super().__init__(nombre, apellido, dni, direccion, correo_electronico, numero_telefono, password)
        self.__id_admin = id_admin
        self.__categoria_trabajo = categoria_trabajo
        self.__usuarios_bloqueados = []
    
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

    def crear_contenido(self, contenido: Contenido, catalogo: list[Contenido]) -> None:
        """Añade un nuevo objeto de contenido al sistema."""
        catalogo.append(contenido)
        print(f"Admin {self.nombre}: creando nuevo contenido '{contenido.titulo}'...")

    def eliminar_contenido(self, id_contenido: int, catalogo: list[Contenido]) -> bool:
        """Elimina contenido por su ID. Devuelve True si tuvo éxito."""
        for c in catalogo:
            if c.id_contenido == id_contenido:
                catalogo.remove(c)
                print(f"Contenido {id_contenido} eliminado correctamente.")
                return True
        print(f"Contenido {id_contenido} no encontrado.")
        return False

    def editar_contenido(self, contenido: Contenido, nuevos_datos: dict) -> None:
        """Actualiza algunos campos básicos de un contenido existente."""
        if "titulo" in nuevos_datos:
            contenido.titulo = nuevos_datos["titulo"]
        if "descripcion" in nuevos_datos:
            contenido.descripcion = nuevos_datos["descripcion"]
        if "genero" in nuevos_datos:
            contenido.genero = nuevos_datos["genero"]
        print(f"Contenido {contenido.id_contenido} editado con nuevos datos.")

    def bloquear_usuario(self, usuario) -> None:
        """Cambia el estado de un usuario a bloqueado."""
        if usuario.id_user not in self.__usuarios_bloqueados:
            self.__usuarios_bloqueados.append(usuario.id_user)
            usuario.esta_bloqueado = True
            print(f"Usuario {usuario.id_user} ha sido bloqueado.")

    def desbloquear_usuario(self, usuario) -> None:
        """Restaura el acceso a un usuario bloqueado."""
        if usuario.id_user in self.__usuarios_bloqueados:
            self.__usuarios_bloqueados.remove(usuario.id_user)
            usuario.esta_bloqueado = False
            print(f"Usuario {usuario.id_user} ha sido desbloqueado.")

    def buscar_por_titulo(self, usuario: Usuario, titulo: str):
        return usuario.buscar_contenido_por_titulo(titulo, self.catalogo)

    def ver_estadisticas_contenido(self, contenido: Contenido) -> None:
        """Muestra métricas de visualización y valoraciones."""
        print(f"Estadísticas de '{contenido.titulo}':")
        print(f"- Visualizaciones: {contenido.num_visualizaciones}")
        print(f"- Media valoraciones: {contenido.calcular_media_valoraciones():.2f}/10")

    def listar_usuarios(self, lista_usuarios: list) -> None:
        """Muestra por consola la lista de todos los usuarios."""
        print("Listado de usuarios:")
        for u, b in lista_usuarios:
            print(f"- {u}")

    def listar_contenidos(self, catalogo : list[Contenido]) -> None:
        """Muestra por consola el catálogo completo."""
        print("Catálogo de la plataforma: ")
        for c  in catalogo:
            print(f"- {c.mostrar_info_resumida()}")
    
    def __str__(self) -> str:
        return f"Admin: {self.nombre} {self.apellido}, ID: {self.__id_admin}, Categoría: {self.__categoria_trabajo}"    