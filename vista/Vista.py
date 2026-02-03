from modelo.Contenido import Contenido

class Vista:
    def mostrar_detalle_contenido(self, contenido):
        print("\n=== Detalle del contenido ===")
        print(contenido.mostrar_info_detallada())

    def pedir_opcion(self, mensaje="Elige una opción: ") -> str:
        return input(mensaje)

    def mostrar_mensaje(self, mensaje: str):
        print(mensaje)

    def pausar(self):
        input("Pulsa ENTER para continuar...")

    def mostrar_menu_usuario(self, usuario) -> None:
        """Muestra las opciones disponibles para un usuario estándar."""
        print(f"Menú de Usuario : {usuario.nombre_user}")
        print("1. Buscar contenido por título")
        print("2. Ver catálogo completo")
        print("3. Filtrar por género")
        print("4. Ver favoritos")
        print("5. Salir")

    def mostrar_catalogo(self, contenidos: list):
        print("Catálogo: ")
        if not contenidos:
            print("No hay contenidos disponibles.")
        for i, c in enumerate(contenidos, 1):
            print(f"{i}. {c.mostrar_info_resumida()}")
    
    def mostrar_resultados_busqueda(self, resultados: list):
        print("Resultados de búsqueda: ")
        if not resultados:
            print("No se encontraron contenidos.")
        for i, c in enumerate(resultados, 1):
            print(f"{i}. {c.mostrar_info:resumida()}")

    def pedir_titulo_busqueda(self) -> str:
        return input("Introduce el título  a buscar: ")
    
    def pedir_genero(self) -> str:
        return input("Introduce el género: ")

    def mostrar_detalle_contenido(self, contenido):
        print("\nDetalles del contenido: ")
        print(contenido.mostrar_info_detallada())


    