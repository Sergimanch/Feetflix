class Vista:

    def mostrar_menu_usuario(self, usuario) -> None:
        """Muestra las opciones disponibles para un usuario estándar."""
        print(f"\nMenú de Usuario: {usuario.nombre_user}")
        print("1. Buscar contenido por título")
        print("2. Ver catálogo completo")
        print("3. Filtrar por género")
        print("4. Ver favoritos")
        print("5. Salir")

    def mostrar_menu_admin(self, admin):
        print(f"\nMenú de admin: {admin.id_admin}")
        print("1. Listar contenidos")
        print("2. Crear contenido")
        print("3. Eliminar contenido")
        print("4. Bloquear usuario")
        print("5. Desbloquear usuario")
        print("6. Ver estadísticas de un contenido")
        print("7. Listar usuarios")
        print("8. Listar usuarios bloqueados")
        print("9. Cerrar sesión")

    def mostrar_menu_contenido(self):
        print("\n Acciones sobre contenido: ")
        print("1. Reproducir")
        print("2. Añadir a favoritos")
        print("3. Valorar")
        print("4. Volver")

    def mostrar_detalle_contenido(self, contenido):
        print("\nDetalles del contenido: ")
        print(contenido.mostrar_info_detallada())

    def pedir_opcion(self, mensaje="Elige una opción: ") -> str:
        return input(mensaje)

    def mostrar_mensaje(self, mensaje: str):
        print(mensaje)

    def pausar(self):
        input("Pulsa ENTER para continuar...")

    def mostrar_catalogo(self, contenidos: list):
        print("\nCatálogo: ")
        if not contenidos:
            print("No hay contenidos disponibles.")
        for i, c in enumerate(contenidos, 1):
            print(f"{i}. {c.mostrar_info_resumida()}")
    
    def mostrar_resultados_busqueda(self, resultados: list):
        print("\nResultados de búsqueda: ")
        if not resultados:
            print("No se encontraron contenidos.")
        for i, c in enumerate(resultados, 1):
            print(f"{i}. {c.mostrar_info_detallada()}")

    def pedir_titulo_busqueda(self) -> str:
        return input("\nIntroduce el título a buscar: ")
    
    def pedir_genero(self) -> str:
        return input("\nIntroduce el género: ")

    def mostrar_detalle_contenido(self, contenido):
        print("\nDetalles del contenido: ")
        print(contenido.mostrar_info_resumida())
    
    def pedir_id_contenido(self) -> int:
        return int(input("\nIntroduce el ID del contenido: "))

    def pedir_id_usuario(self) -> str:
        return input("\nIntroduce el ID del usuario: ")

    def mostrar_lista_usuarios(self, usuarios: list):
        print("\nUsuarios registrados:")
        if not usuarios:
            print("No hay usuarios.")
        for u in usuarios:
            print(f"- {u}")

    def pedir_nota_valoracion(self) -> int:
        nota = int(input("Introduce una nota (0-10): "))
        while nota < 0 or nota > 10:
            print("Nota inválida. Debe estar entre 0 y 10.")
            nota = int(input("Introduce una nota (0-10): "))
        return nota

    def pedir_edad_usuario(self) -> int:
        return int(input("Introduce tu edad: "))
    
    def limpiar_pantalla(self) -> None:
        print("\n" * 30)  