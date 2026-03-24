
##CLASE BASE USUARIO

class Usuario:
    def __init__(self,id_usuario,username,password):
        self.__id_usuario=id_usuario
        self.__username=username
        self.__password=password

    # Getters (sin setter para id_usuario y password para proteger integridad y seguridad)
    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, nuevo_username):
        self.__username = nuevo_username 

    # No getter para password, solo método para verificar credenciales
    def verificar_credenciales(self, username, password):
        return self.__username == username and self.__password == password
    
    def mostrar_tipo(self):
        # Sobrescribe el tipo de cliente
        return "Usuario regular"
    
    # Método para mostrar datos sin mostrar password
    def mostrar_datos(self):
        return {
            "id_usuario": self.__id_usuario,
            "username": self.__username,
            "password":self.__password,
        }

##CLASES HIJAS DE USUAARIO:

class Admin(Usuario):

    def __init__(self, id_usuario, username, password):
        super().__init__(id_usuario, username, password)

    def mostrar_tipo(self):
        return "admin"

    def agregar_usuario(self, sistema):
        sistema.agregar_usuario()

    def eliminar_usuario(self, sistema):
        sistema.eliminar_usuario()


class Trabajador(Usuario):

    def __init__(self, id_usuario, username, password):
        super().__init__(id_usuario, username, password)

    def mostrar_tipo(self):
        return "trabajador"