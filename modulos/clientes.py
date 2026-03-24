import datetime
from modulos import validaciones


## CLASE BASE CLIENTE 

class Cliente:
    # Atributos principales del cliente
    def __init__(self, id_cliente, nombre, apellido, telefono, edad, ciudad, genero):
        
        # id_cliente es privado para evitar modificaciones externas
        self.__id_cliente = id_cliente
        
        self.nombre = nombre
        self.apellido = apellido
        
        # telefono es privado para permitir futura validación interna
        self.__telefono = telefono
        
        # edad es privada para proteger integridad del dato
        self.__edad = edad
        
        self.ciudad = ciudad
        self.genero = genero
        
        #  fecha_registro es privada porque se genera automáticamente
        self.__fecha_registro = datetime.datetime.today().strftime("%d/%m/%Y")
    """Lo que vamos a hacer ahora es definir los getters y los setters de nuestro encapsulamiento

    Para ello hay que tener en cuenta que:
    +++id_cliente y fecha_registro:
    son FIJOS, lo ideal es que no se cambien y no se permitan modificaciones de estos
    por lo tanto no necesitan SETTER

    +++los demas atributos privados (edad, telefono):
    Pueden modificarse sin significar un problema a futuro para la base de datos.
    Por lo tanto debemos asignarles SETTER

    """

    #Getter de id_cliente 
    @property
    def id_cliente(self):
        return self.__id_cliente

    #Getter de telefono
    @property
    def telefono(self):
        return self.__telefono

    #Setter controlado de telefono
    @telefono.setter
    def telefono(self, nuevo_telefono):
        if validaciones.validacion_numero_telefono(nuevo_telefono):
            self.__telefono = nuevo_telefono
        else:
            raise ValueError("Teléfono inválido")

    #Getter de edad
    @property
    def edad(self):
        return self.__edad

    # Setter controlado de edad
    @edad.setter
    def edad(self, nueva_edad):
        if validaciones.validar_edad(nueva_edad):
            self.__edad = nueva_edad  
        else:
            raise ValueError("Edad inválida")


    #Getter de fecha_registro
    @property
    def fecha_registro(self):
        return self.__fecha_registro

    ## Método que se usaraa para sobreescribirse en subclases (POLIMORFISMO)
    def mostrar_tipo(self):
        return "Cliente"

    ## Método que devuelve los datos en lista
    def mostrar_datos(self):
        # Retorna todos los atributos en formato lista para guardarlos en JSON
        return {
        "id_cliente": self.id_cliente,
        "nombre": self.nombre,
        "apellido": self.apellido,
        "telefono": self.telefono,
        "edad": self.edad,
        "ciudad": self.ciudad,
        "genero": self.genero,
        "tipo": self.mostrar_tipo(),
        "fecha_registro": self.fecha_registro
    }


## SUBCLASES

class ClienteRegular(Cliente):
    def __init__(self, id_cliente, nombre, apellido, telefono, edad, ciudad, genero):
        # Hereda todos los atributos del padre
        super().__init__(id_cliente, nombre, apellido, telefono, edad, ciudad, genero)

    def mostrar_tipo(self):
        # Sobrescribe el tipo de cliente
        return "Cliente Regular"


class ClientePremium(Cliente):
    def __init__(self, id_cliente, nombre, apellido, telefono, edad, ciudad, genero):
        # Hereda atributos del padre
        super().__init__(id_cliente, nombre, apellido, telefono, edad, ciudad, genero)

    def mostrar_tipo(self):
        # Tipo específico Premium
        return "Cliente Premium"


class ClienteCorporativo(Cliente):
    def __init__(self, id_cliente, nombre, apellido, telefono, edad, ciudad, genero):
        # Hereda atributos del padre
        super().__init__(id_cliente, nombre, apellido, telefono, edad, ciudad, genero)

    def mostrar_tipo(self):
        # Tipo específico Corporativo
        return "Cliente Corporativo"
