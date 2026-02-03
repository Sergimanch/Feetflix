from modelo.Contenido import Contenido
from modelo.Usuario import Usuario
from modelo.Admin import Admin
from vista.Vista import Vista

class Controlador:
    """
    Controlador principal. Coordina Vista ↔ Modelo.
    Mantiene listas de usuarios, admins y catálogo.
    """

    def __init__(self):
        self.__catalogo: list[Contenido] = []
        self.__usuarios: list[Usuario] = []
        self.__admins: list[Admin] = []
        self.__vista = Vista()
        self.__usuario_actual = None
        self.__admin_actual = None