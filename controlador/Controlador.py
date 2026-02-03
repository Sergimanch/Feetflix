"""
CONTROLADOR PRINCIPAL - FEETFLIX DAM
Coordina Vista y Modelo siguiendo patrón MVC
"""

from modelo.Contenido import Contenido
from modelo.Usuario import Usuario
from modelo.Admin import Admin
from modelo.Peliculas import Pelicula
from modelo.Series import Series
from modelo.Juegos import Juegos
from modelo.Persona import Persona
from vista.Vista import Vista
from datetime import date
from typing import List

class Controlador:
    """
    Mantiene listas de usuarios, admins y catálogo.
    """

    def __init__(self):
        self.catalogo: List[Contenido] = []
        self.usuarios: List[Usuario] = []
        self.admins: List[Admin] = []
        self.vista = Vista()
        self.usuario_actual: Usuario | None = None
        self.admin_actual: Admin | None = None

    #MÉTODOS
    
    def crear_contenido(self):
        """Crea contenidos de prueba."""
        # Crear película
        reparto = ["Actor1", "Actor2"]
        peli = Pelicula(
            1, "Inception", "Película de sueños", "Ciencia Ficción",
            13, 148, date(2010, 7, 16),
            "Christopher Nolan", reparto, "Inglés", "4K"
        )
        peli.subtitulos_disponibles = ["Español", "Inglés"]
        self.catalogo.append(peli)

        # Crear serie
        serie = Series(
            2, "Breaking Bad", "Serie sobre química", "Drama",
            18, 45, date(2008, 1, 20),
            5, False
        )
        serie.añadir_temporada(13)
        serie.añadir_temporada(13)
        self.catalogo.append(serie)

        # Crear juego
        juego = Juegos(
            3, "Among Us", "Juego de impostores", "Multijugador",
            7, 30, date(2018, 6, 15),
            ["Móvil", "PC"], True
        )
        self.catalogo.append(juego)

    def registrar_usuario(self):
        """Crea usuarios de prueba."""
        persona1 = Persona("Juan", "Pérez", "12345678A", "Calle Falsa 123", "juan@email.com", "123456789", "pass123")
        usuario1 = Usuario(
            "Juan", "Pérez", "12345678A", "Calle Falsa 123", "juan@email.com", "123456789", "pass123",
            "USER001", "juanperez", "Español", "Tarjeta"
        )
        self.usuarios.append(usuario1)

        persona2 = Persona("Ana", "García", "87654321B", "Avenida Real 456", "ana@email.com", "987654321", "pass456")
        usuario2 = Usuario(
            "Ana", "García", "87654321B", "Avenida Real 456", "ana@email.com", "987654321", "pass456",
            "USER002", "anagarcia", "Inglés", "PayPal"
        )
        self.usuarios.append(usuario2)

    def registrar_admin(self):
        """Crea admins de prueba."""
        persona_admin = Persona("Admin", "Master", "11111111Z", "Netflix HQ", "admin@netflix.com", "666666666", "adminpass")
        admin1 = Admin(
            "Admin", "Master", "11111111Z", "Netflix HQ", "admin@netflix.com", "666666666", "adminpass",
            "ADMIN001", "Super Admin"
        )
        self.admins.append(admin1)

    #  MENÚ PRINCIPAL 

    def mostrar_menu_principal(self):
        """Muestra menú principal de la aplicación."""
        print("FEETFLIX")
        print()
        print("1. Iniciar sesión como Usuario")
        print("2. Iniciar sesión como Admin")
        print("3. Salir")

    def pedir_id_usuario(self):
        """Solicita ID para login."""
        return self.vista.pedir_id_usuario()

    #  SESIONES 

    def login_usuario(self, id_user: str):
        """Busca y establece usuario actual por ID."""
        for usuario in self.usuarios:
            if usuario.id_user == id_user:
                self.usuario_actual = usuario
                self.vista.mostrar_mensaje(f"¡Bienvenido, {usuario.nombre_user}!")
                return True
        self.vista.mostrar_mensaje(" Usuario NO encontrado.")
        return False

    def login_admin(self, id_admin: str):
        """Busca y establece admin actual por ID."""
        for admin in self.admins:
            if admin.id_admin == id_admin:
                self.admin_actual = admin
                self.vista.mostrar_mensaje(f"¡Bienvenido, Admin {admin.id_admin}!")
                return True
        self.vista.mostrar_mensaje(" Admin NO encontrado.")
        return False

    def salir_usuario(self):
        """Cierra sesión de usuario."""
        self.usuario_actual = None
        self.vista.mostrar_mensaje("Sesión cerrada.")

    def salir_admin(self):
        """Cierra sesión de admin."""
        self.admin_actual = None
        self.vista.mostrar_mensaje("Sesión de admin cerrada.")

    #  MENÚ USUARIO 

    def manejar_menu_usuario(self):
        """Maneja el menú del usuario actual."""
        while self.usuario_actual:
            self.vista.mostrar_menu_usuario(self.usuario_actual)
            opcion = self.vista.pedir_opcion()

            if opcion == "1":
                self.buscar_por_titulo()
            elif opcion == "2":
                self.ver_catalogo()
            elif opcion == "3":
                self.filtrar_por_genero()
            elif opcion == "4":
                self.ver_favoritos()
            elif opcion == "5":
                self.salir_usuario()
                break
            else:
                self.vista.mostrar_mensaje("Opción inválida.")
            self.vista.pausar()

    def buscar_por_titulo(self):
        """Ejecuta búsqueda por título."""
        titulo = self.vista.pedir_titulo_busqueda()
        resultados = self.usuario_actual.buscar_contenido_por_titulo(titulo, self.catalogo)
        self.vista.mostrar_resultados_busqueda(resultados)
        if resultados:
            self.manejar_contenido(resultados[0])

    def ver_catalogo(self):
        """Muestra catálogo completo."""
        self.vista.mostrar_catalogo(self.catalogo)
        if self.catalogo:
            self.manejar_contenido(self.catalogo[0])

    def filtrar_por_genero(self):
        """Filtra contenidos por género."""
        genero = self.vista.pedir_genero()
        resultados = self.usuario_actual.filtrar_contenido_por_genero(genero, self.catalogo)
        self.vista.mostrar_resultados_busqueda(resultados)

    def ver_favoritos(self):
        """Muestra favoritos del usuario."""
        favoritos = self.usuario_actual.ver_lista_favoritos()
        self.vista.mostrar_catalogo(favoritos)

    def manejar_contenido(self, contenido: Contenido):
        """Menú de acciones para contenido específico."""
        self.vista.mostrar_detalle_contenido(contenido)
        self.vista.mostrar_menu_contenido()
        opcion = self.vista.pedir_opcion()

        if opcion == "1":
            edad = self.vista.pedir_edad_usuario()
            self.usuario_actual.reproducir_contenido(contenido, edad)
        elif opcion == "2":
            self.usuario_actual.añadir_a_lista(contenido)
            self.vista.mostrar_mensaje(" Añadido a favoritos.")
        elif opcion == "3":
            nota = self.vista.pedir_nota_valoracion()
            self.usuario_actual.valorar_contenido(contenido, nota)
            self.vista.mostrar_mensaje(f" Valoración {nota}/10 registrada.")
        elif opcion == "4":
            return

    #  MENÚ ADMIN 

    def manejar_menu_admin(self):
        """Maneja el menú del admin actual."""
        while self.admin_actual:
            self.vista.mostrar_menu_admin(self.admin_actual)
            opcion = self.vista.pedir_opcion()

            if opcion == "1":
                self.admin_actual.listar_contenidos(self.catalogo)
            elif opcion == "2":
                self.crear_contenido_admin()
            elif opcion == "3":
                id_contenido = self.vista.pedir_id_contenido()
                self.admin_actual.eliminar_contenido(id_contenido, self.catalogo)
            elif opcion == "4":
                self.bloquear_usuario_admin()
            elif opcion == "5":
                self.desbloquear_usuario_admin()
            elif opcion == "6":
                self.ver_estadisticas_admin()
            elif opcion == "7":
                self.salir_admin()
                break
            else:
                self.vista.mostrar_mensaje("Opción inválida.")
            self.vista.pausar()

    def crear_contenido_admin(self):
        """Simula creación de contenido nuevo."""
        print("\nCrear contenido (simulado)")
        self.vista.mostrar_mensaje("En una versión completa pedirías todos los datos.")
        self.crear_contenido()

    def bloquear_usuario_admin(self):
        """Bloquea usuario seleccionado."""
        id_user = self.vista.pedir_id_usuario()
        for usuario in self.usuarios:
            if usuario.id_user == id_user:
                self.admin_actual.bloquear_usuario(usuario)
                break
        else:
            self.vista.mostrar_mensaje("Usuario no encontrado.")

    def desbloquear_usuario_admin(self):
        """Desbloquea usuario seleccionado."""
        id_user = self.vista.pedir_id_usuario()
        for usuario in self.usuarios:
            if usuario.id_user == id_user:
                self.admin_actual.desbloquear_usuario(usuario)
                break
        else:
            self.vista.mostrar_mensaje("Usuario no encontrado.")

    def ver_estadisticas_admin(self):
        """Muestra estadísticas de contenido."""
        id_contenido = self.vista.pedir_id_contenido()
        for c in self.catalogo:
            if c.id_contenido == id_contenido:
                self.admin_actual.ver_estadisticas_contenido(c)
                break
        else:
            self.vista.mostrar_mensaje("Contenido no encontrado.")

    #  EJECUCIÓN PRINCIPAL 

    def ejecutar(self):
        """Bucle principal de la aplicación."""
        self.registrar_usuario()
        self.registrar_admin()
        self.crear_contenido()

        while True:
            self.mostrar_menu_principal()
            opcion = self.vista.pedir_opcion()

            if opcion == "1":
                id_user = self.pedir_id_usuario()
                if self.login_usuario(id_user):
                    self.manejar_menu_usuario()
            elif opcion == "2":
                id_admin = self.pedir_id_usuario()
                if self.login_admin(id_admin):
                    self.manejar_menu_admin()
            elif opcion == "3":
                self.vista.mostrar_mensaje("¡Gracias por usar Netflix DAM!")
                break
            else:
                self.vista.mostrar_mensaje("Opción inválida.")
            self.vista.limpiar_pantalla()