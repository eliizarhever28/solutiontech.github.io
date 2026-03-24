import os
import json
from modulos.clientes import ClienteRegular, ClientePremium, ClienteCorporativo
from modulos.usuarios import Admin, Trabajador
from modulos.otras_funciones import clear_screen, titulo
from modulos import validaciones

## SISTEMA DE GESTIÓN DE CLIENTES

class SistemaGestion:

    def __init__(self):
        # Ruta privada para evitar modificación externa
        self.__base_datos_clientes = "base_datos_cliente/clientes.json"
        self.__base_datos_usuarios = "base_datos_cliente/usuarios.json"
    

    # Getter de ruta base de datos
    @property
    def base_datos_clientes(self):
        return self.__base_datos_clientes
    
    #Getter de ruta de base de usuarios
    @property
    def base_datos_usuarios(self):
        return self.__base_datos_usuarios
    
    ##METODOS DEL SISTEMA 
    #Mmetodos para el login

    def cargar_usuarios(self):
        if not os.path.exists(self.base_datos_usuarios):
            return []
        with open(self.base_datos_usuarios, 'r', encoding='utf-8') as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                print("Error: Base de datos corrupta.")
                return []

    def guardar_usuarios(self, datos):
        with open(self.base_datos_usuarios, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4)

    def login(self):
        clear_screen()
        titulo()
        print("INICIO DE SESIÓN\n")

        username = input("Usuario: ")
        password = input("Contraseña: ")

        usuarios = self.cargar_usuarios()

        for user_data in usuarios:
            if user_data["username"] == username and user_data["password"] == password:
                
                tipo = user_data.get("tipo", "trabajador")
                if tipo == "admin":
                    usuario = Admin(user_data["id_usuario"], user_data["username"], user_data["password"])
                else:
                    usuario = Trabajador(user_data["id_usuario"], user_data["username"], user_data["password"])

                print("\nAcceso concedido")
                input("Presione ENTER para continuar...")
                return usuario

        print("\nCredenciales incorrectas")
        input("Presione ENTER para continuar...")
        return None

    ##Metodos para la navegacion en el sistema

    def cargar_datos(self):
        # Verifica si el archivo de base de datos existe
        if not os.path.exists(self.base_datos_clientes):
            # Si no existe, retorna una lista vacía para evitar errores al procesar datos
            return []

        # Si el archivo existe, se abre en modo lectura ('r') con codificación UTF-8
        with open(self.base_datos_clientes, 'r', encoding='utf-8') as archivo:
            # Se cargan los datos del archivo JSON y se retorna como una lista de diccionarios
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                print("Error: Base de datos corrupta.")
                return []

    def guardar_datos(self, datos):
        # Abre el archivo de base de datos en modo escritura
        # Esto reemplaza completamente el contenido del archivo con los nuevos datos
        with open(self.base_datos_clientes, 'w', encoding='utf-8') as archivo:
            # Convierte la lista/diccionario de Python en formato JSON y lo escribe en el archivo
            # 'indent=4' sirve para que el JSON se guarde con sangría de 4 espacios
            json.dump(datos, archivo, indent=4)
        
    
    ##METODO para agregar usuario
    def agregar_usuario(self):
        while True:
            clear_screen()
            titulo()
            print("Agregar nuevo usuario:\n")

            usuarios = self.cargar_usuarios()

            # Generar nuevo ID usuario automático basado en cantidad actual
            nuevo_id = f"US{len(usuarios) + 1:03d}"

            while True:
                username = input("Ingrese nombre de usuario: ").strip()
                if validaciones.validar_usuario(username):
                    if any(user['username'] == username for user in usuarios):
                        print("El usuario ya existe.")
                        continue
                    break
                
                print("Nombre de usuario inválido. Usuario no debe estar vacío o tener carácteres especiales")

            while True:
                password = input("Ingrese contraseña: ").strip()
                if len(password) < 4:
                    print("La contraseña debe tener al menos 4 caracteres.")
                    continue
                break

            while True:
                tipo = input("Ingrese tipo de usuario (admin/trabajador): ").lower().strip()
                if tipo in ("admin", "trabajador"):
                    break
                print("Tipo inválido. Debe ser 'admin' o 'trabajador'.")

            if tipo == "admin":
                nuevo_usuario = Admin(nuevo_id, username, password)
            else:
                nuevo_usuario = Trabajador(nuevo_id, username, password)

            datos_usuario = nuevo_usuario.mostrar_datos()
            datos_usuario["tipo"] = tipo

            print("Información del nuevo usuario: ")
            print(f"Username: {datos_usuario["username"]}\nTipo: {datos_usuario["tipo"]}\n")
            
            opcion_continuar=input("¿Está seguro de agregar el usuario? 1. Sí | 2. No : ")
            if opcion_continuar=="2":
                print("No se agregó el usuario")
            else:
                usuarios.append(datos_usuario)
                self.guardar_usuarios(usuarios)

                print("Usuario agregado correctamente.")
                input("ENTER para continuar...")
            while True:
                try:
                    opcion_continuar = int(input("Agregar otro usuario? 1. Sí | 2. No : "))
                    if opcion_continuar == 2:
                        return
                    else:
                        break
                except ValueError:
                    print("Debe ingresar una opción válida")
                

###METODO ELIMINAR USUAARIO
    def eliminar_usuario(self, usuario_activo):
        while True:
            clear_screen()
            titulo()
            print("Eliminar usuario:\n")

            usuarios = self.cargar_usuarios()

            busar_usuario = input("Ingrese el ID o el Username del usuario a eliminar: ")

            # Verificacion : el usuario que estaa loggeado no se puede eliminar
            if busar_usuario == usuario_activo.id_usuario or  busar_usuario == usuario_activo.username:
                print("\nNo se puede eliminar el usuario que está actualmente activo.")
                input("Presione ENTER para continuar...")
                break
            # Verificación: no dejar base vacía
            if len(usuarios) <= 1:
                print("\nNo se puede eliminar el último usuario del sistema.")
                input("Presione ENTER para continuar...")
                break 

            nueva_lista = []
            encontrado = False

            for usuario in usuarios:
                if usuario["username"] == busar_usuario or busar_usuario==usuario["id_usuario"]:
                    encontrado = True
                else:
                    nueva_lista.append(usuario)

            if encontrado:
                try:
                    ##preguntaa de seguridad antes de eliminaar 
                    opcion_segura = int(input(f"\nEstá seguro que desea eliminar el usuario | {busar_usuario} | ? 1.Sí | 2.No : "))
                    if opcion_segura == 1:
                        self.guardar_usuarios(nueva_lista)
                        print("Usuario eliminado correctamente.")
                    else:
                        print("\nNo se eliminó el usuario.")
                except ValueError:
                    print("Opción inválida. No se eliminó el usuario.")
                
            else:
                print("Usuario no encontrado.")
        ##Preguntamos si quiere continuar eliminando usuarios
            try:
                opcion_continuar = int(input("Eliminar otro usuario? 1. Sí | 2. No : "))
                if opcion_continuar == 2:
                    break
            except ValueError:
                print("Debe ingresar una opción válida")
                input("Presione ENTER para continuar...")

    ## GENERAR ID AUTOMÁTICO
    
    def generar_id(self):
        datos = self.cargar_datos()
        # Si el archivo no existe, empieza desde CL001
        if not datos:
            return "CL001"
        ultimo_id = datos[-1]["id_cliente"] # Toma el ID del último registro
        numero = int(ultimo_id[2:]) + 1 # Extrae el número y lo incrementa
        return f"CL{numero:03d}" # Formato CL + número de 3 dígitos
    
    ## AGREGAR CLIENTE
    
    def agregar_cliente(self):
        while True:
            clear_screen()
            titulo()
            print("Agregar nuevo cliente:\n")

            datos=self.cargar_datos()

            # Se solicitan los datos al usuario
            id_cliente = self.generar_id() # Se genera ID automático
            while True:
                nombre = input("Ingrese Nombre: ")
                if validaciones.validar_texto_corto(nombre):
                    nombre=nombre.title()
                    break
                print("Nombre inválido. No se deben ingresar números y/o caracteres especiales. No puede haber más de 20 caracteres")

            while True:
                apellido = input("Ingrese Apellido: ")
                if validaciones.validar_texto_corto(apellido):
                    apellido=apellido.title()                    
                    break
                print("Apellido inválido. No se deben ingresar números y/o caracteres especiales. No puede haber más de 20 caracteres")
            if any(
                        cliente['nombre'] == nombre 
                        and cliente['apellido']==apellido 
                        for cliente in datos):
                        print("El cliente ya existe.")
                        try:
                            opcion_continuar = int(input("Agregar otro cliente? 1. Sí | 2. No : "))
                            if opcion_continuar == 2:
                                break
                            else:
                                continue
                        except ValueError:
                            print("Debe ingresar una opción válida")
                            input("Presione ENTER para continuar...")
            while True:
                telefono = input("Ingrese Número de teléfono: ")
                if validaciones.validacion_numero_telefono(telefono):
                    break
                print("Número inválido. Debe ser un número entero de 9 dígitos, no puede ser 0 o estar vacío")
            while True:
                edad = input("Ingrese Edad: ")
                if validaciones.validar_edad(edad):
                    break
                print("Edad inválida. Debe ser un número entero entre 18 y 110, no puede estar vacío")
            while True:
                ciudad = input("Ingrese Ciudad: ")
                if validaciones.validar_texto_corto(ciudad):
                    ciudad=ciudad.title()
                    break
                print("Ciudad inválida. No se deben ingresar números y/o caracteres especiales. No puede haber más de 20 caracteres")
            while True:
                print("Géneros:\nFemenino\nMasculino\nOtro")
                genero = input("Ingrese Género: ").lower()
                if genero in ("femenino", "masculino", "otro"):###lo ponemos en tupla para que no sea modificable
                    genero=genero.capitalize()
                    break
                print("Género inválido. Ingrese:  Femenino | Masculino | Otro.")

            print("\nSeleccione tipo de cliente:")
            print("1. Cliente Regular")
            print("2. Cliente Premium")
            print("3. Cliente Corporativo")
            while True:
                try:
                    tipo = input("Seleccione opción: ")

                    if tipo == "1":
                        cliente = ClienteRegular(id_cliente, nombre, apellido, telefono, edad, ciudad, genero)
                        break
                    elif tipo == "2":
                        cliente = ClientePremium(id_cliente, nombre, apellido, telefono, edad, ciudad, genero)
                        break
                    elif tipo == "3":
                        cliente = ClienteCorporativo(id_cliente, nombre, apellido, telefono, edad, ciudad, genero)
                        break
                    else:
                        print("Tipo de cliente inválido")
                        continue
                except ValueError:
                    print("Debe ingresar un número válido")
                    input("Presione ENTER para continuar...")
                    continue
            
            print("Información del nuevo cliente: ")
            print(f"Nombre: {nombre}\nApellido: {apellido}\nTelefono: {telefono} \nEdad: {edad}\nCiudad: {ciudad}\n")
            
            opcion_continuar=input("¿Está seguro de agregar el cliente? 1. Sí | 2. No : ")
            if opcion_continuar=="2":
                print("No se agregó el cliente")
            else:
                # Si la carpeta no existe, se crea
                if not os.path.exists("base_datos_cliente"):
                    os.mkdir("base_datos_cliente")

                # Se guardan los datos en el archivo
                datos = self.cargar_datos()
                datos.append(cliente.mostrar_datos())
                self.guardar_datos(datos)

                print(f"\nCliente {cliente.nombre} agregado correctamente como {cliente.mostrar_tipo()}\n")

            try:
                opcion_continuar = int(input("Agregar otro cliente? 1. Sí | 2. No : "))
                if opcion_continuar == 2:
                    break
            except ValueError:
                print("Debe ingresar una opción válida")
                input("Presione ENTER para continuar...")

    ## LISTAR CLIENTES
    
    def listar_cliente(self):
        clear_screen()
        titulo()
        print("Clientes:\n")

        datos = self.cargar_datos()

        # Verifica si la base de datos está vacía
        if not datos:
            print("Base de datos vacía.")
            input("Presione ENTER para continuar...")
            return

        print(f"Clientes totales: {len(datos)}\n")

        encabezados = ["ID", "Nombre", "Apellido", "Teléfono", "Edad", "Ciudad", "Género", "Tipo", "Fecha registro"]
        for campo in encabezados:
            print(f"{campo:<20}", end="")
        print()
        print("-" * 180)

        for cliente in datos:
            fila = [
                cliente["id_cliente"],
                cliente["nombre"],
                cliente["apellido"],
                cliente["telefono"],
                cliente["edad"],
                cliente["ciudad"],
                cliente["genero"],
                cliente["tipo"],
                cliente["fecha_registro"]
            ]
            for dato in fila:
                print(f"{dato:<20}", end="")
            print()

        input("\nPresione ENTER para continuar...")

    ## MODIFICAR CLIENTE
    
    def modificar_cliente(self):
        # Bucle principal para permitir modificar más de un cliente si el usuario lo desea
        while True:
            
            # Limpiamos pantalla para mantener interfaz ordenada
            clear_screen()
            
            # Mostramos el título del sistema
            titulo()
            
            print("Modificar cliente:\n")

            # Cargamos todos los clientes guardados en el archivo JSON
            datos = self.cargar_datos()

            # Si la base de datos está vacía, no se puede modificar nada
            if not datos:
                print("Base de datos vacía.")
                input("Presione ENTER para continuar...")
                return  # Salimos del método

            # Pedimos al usuario el ID o el nombre del cliente que quiere modificar
            busqueda = input("Ingrese Nombre o ID del cliente a modificar: ").strip()
            
            # Inicializamos variable donde guardaremos el cliente si lo encontramos
            cliente_encontrado = None

            # Recorremos la lista de clientes para buscar coincidencia
            for cliente in datos:
                
                # Comparamos por ID exacto o por nombre (ignorando mayúsculas/minúsculas)
                if cliente["id_cliente"] == busqueda or cliente["nombre"].lower() == busqueda.lower():
                    cliente_encontrado = cliente  # Guardamos el cliente encontrado
                    break  # Salimos del bucle porque ya lo encontramos

            # Si se encontró el cliente
            if cliente_encontrado:

                print("\nCliente encontrado:\n")

                # Mostramos encabezados de la tabla
                encabezados = ["ID", "Nombre", "Apellido", "Teléfono", "Edad", "Ciudad", "Género", "Tipo", "Fecha registro"]
                for campo in encabezados:
                    print(f"{campo:<20}", end="")
                print()
                print("-" * 180)

                # Creamos la fila con los datos actuales del cliente
                fila = [
                    cliente_encontrado["id_cliente"],
                    cliente_encontrado["nombre"],
                    cliente_encontrado["apellido"],
                    cliente_encontrado["telefono"],
                    cliente_encontrado["edad"],
                    cliente_encontrado["ciudad"],
                    cliente_encontrado["genero"],
                    cliente_encontrado["tipo"],
                    cliente_encontrado["fecha_registro"]
                ]

                # Mostramos los datos formateados
                for dato in fila:
                    print(f"{dato:<20}", end="")
                print()

                print("\nIngrese los nuevos datos (deje vacío para mantener el valor actual):\n")

                # =============================
                # MODIFICACIÓN DE CADA CAMPO
                # =============================

                # Pedimos nuevo nombre (si el usuario presiona ENTER, no se modifica)
                nuevo_nombre = input(f"Nuevo Nombre ({cliente_encontrado['nombre']}): ")
                
                # Si el usuario escribió algo
                if nuevo_nombre:
                    
                    # Validamos el nuevo dato antes de modificarlo
                    if validaciones.validar_texto_corto(nuevo_nombre):
                        cliente_encontrado["nombre"] = nuevo_nombre  # Actualizamos el valor
                    else:
                        print("Nombre inválido. No se modificó.")

                # Nuevo apellido
                nuevo_apellido = input(f"Nuevo Apellido ({cliente_encontrado['apellido']}): ")
                if nuevo_apellido:
                    if validaciones.validar_texto_corto(nuevo_apellido):
                        cliente_encontrado["apellido"] = nuevo_apellido
                    else:
                        print("Apellido inválido. No se modificó.")

                # Nuevo teléfono
                nuevo_telefono = input(f"Nuevo Teléfono ({cliente_encontrado['telefono']}): ")
                if nuevo_telefono:
                    if validaciones.validacion_numero_telefono(nuevo_telefono):
                        cliente_encontrado["telefono"] = nuevo_telefono
                    else:
                        print("Teléfono inválido. No se modificó.")

                # Nueva edad
                nueva_edad = input(f"Nueva Edad ({cliente_encontrado['edad']}): ")
                if nueva_edad:
                    if validaciones.validar_edad(nueva_edad):
                        cliente_encontrado["edad"] = nueva_edad
                    else:
                        print("Edad inválida. No se modificó.")

                # Nueva ciudad
                nueva_ciudad = input(f"Nueva Ciudad ({cliente_encontrado['ciudad']}): ")
                if nueva_ciudad:
                    if validaciones.validar_texto_corto(nueva_ciudad):
                        cliente_encontrado["ciudad"] = nueva_ciudad
                    else:
                        print("Ciudad inválida. No se modificó.")

                # Nuevo género
                nuevo_genero = input(f"Nuevo Género ({cliente_encontrado['genero']}): ").lower()
                if nuevo_genero:
                    if nuevo_genero in ("femenino", "masculino", "otro"):
                        cliente_encontrado["genero"] = nuevo_genero
                    else:
                        print("Género inválido. No se modificó.")
                
                opcion_segura=input("¿Está seguro de modificar la información? 1.Sí | 2.No : ")
                if opcion_segura=="2":
                    print("No se modificó la información del cliente.")
                    
                else:
                    # Guardamos toda la lista nuevamente en el archivo JSON
                    # Esto sobrescribe el archivo con los datos actualizados
                    self.guardar_datos(datos)
                    print("\nCliente modificado correctamente.")


            else:
                # Si no se encontró ningún cliente con ese ID o nombre
                print("\nNo se encontró ningún cliente con ese nombre o ID.")

            # Preguntamos si desea modificar otro cliente
            try:
                opcion_continuar = int(input("\nModificar otro cliente? 1. Sí | 2. No : "))
                if opcion_continuar == 2:
                    break  # Salimos del while principal
            except ValueError:
                print("Debe ingresar una pción válida")
                input("Presione ENTER para continuar...")
    
    ## BUSCAR CLIENTES
    
    def buscar_clientes(self):
        while True:
            clear_screen()
            titulo()
            print("Buscar clientes:\n")

            datos = self.cargar_datos()

            if not datos:
                print("Base de datos vacía.")
                input("Presione ENTER para continuar...")
                return

            busqueda = input("Ingrese Nombre o ID del cliente: ").strip()
            encontrados = []

            for cliente in datos:
                if cliente["id_cliente"] == busqueda or cliente["nombre"].lower() == busqueda.lower():
                    encontrados.append(cliente)

            print("\nResultados encontrados:\n")

            encabezados = ["ID", "Nombre", "Apellido", "Teléfono", "Edad", "Ciudad", "Género", "Tipo", "Fecha registro"]
            for campo in encabezados:
                print(f"{campo:<20}", end="")
            print()
            print("-" * 180)

            if encontrados:
                for cliente in encontrados:
                    fila = [
                        cliente["id_cliente"],
                        cliente["nombre"],
                        cliente["apellido"],
                        cliente["telefono"],
                        cliente["edad"],
                        cliente["ciudad"],
                        cliente["genero"],
                        cliente["tipo"],
                        cliente["fecha_registro"]
                    ]
                    for dato in fila:
                        print(f"{dato:<20}", end="")
                    print()
            else:
                print("\nNo se encontró ningún cliente con ese nombre o ID.")

            try:
                opcion_continuar = int(input("\nBuscar otro cliente? 1. Sí | 2. No : "))
                if opcion_continuar == 2:
                    break
            except ValueError:
                print("Debe ingresar una opción válida")
                input("Presione ENTER para continuar...")

    ## ELIMINAR CLIENTES
    
    def eliminar_cliente(self):
        while True:
            clear_screen()
            titulo()
            print("Eliminar cliente:\n")

            datos = self.cargar_datos()

            if not datos:
                print("Base de datos vacía.")
                input("Presione ENTER para continuar...")
                return

            busqueda = input("Ingrese Nombre o ID del cliente a eliminar: ").strip()
            lista_actualizada = []
            cliente_encontrado = None

            for cliente in datos:
                if cliente["id_cliente"] == busqueda or cliente["nombre"].lower() == busqueda.lower():
                    cliente_encontrado = cliente
                else:
                    lista_actualizada.append(cliente)

            if cliente_encontrado:

                print("\nCliente encontrado:\n")
                encabezados = ["ID", "Nombre", "Apellido", "Teléfono", "Edad", "Ciudad", "Género", "Tipo", "Fecha registro"]
                for campo in encabezados:
                    print(f"{campo:<20}", end="")
                print()
                print("-" * 180)

                fila = [
                    cliente_encontrado["id_cliente"],
                    cliente_encontrado["nombre"],
                    cliente_encontrado["apellido"],
                    cliente_encontrado["telefono"],
                    cliente_encontrado["edad"],
                    cliente_encontrado["ciudad"],
                    cliente_encontrado["genero"],
                    cliente_encontrado["tipo"],
                    cliente_encontrado["fecha_registro"]
                ]

                for dato in fila:
                    print(f"{dato:<20}", end="")
                print()

                try:
                    opcion_segura = int(input(f"\nEstá seguro que desea eliminar este cliente? 1.Sí | 2.No : "))
                    if opcion_segura == 1:
                        self.guardar_datos(lista_actualizada)
                        print("\nCliente eliminado correctamente.")
                    else:
                        print("\nNo se eliminó el cliente.")
                except ValueError:
                    print("Opción inválida. No se eliminó el cliente.")
            else:
                print("\nNo se encontró ningún cliente con ese nombre o ID.")
                input("Presione ENTER para continuar...")

            try:
                opcion_continuar = int(input("\nEliminar otro cliente? 1. Sí | 2. No : "))
                if opcion_continuar == 2:
                    break
            except ValueError:
                print("Debe ingresar una opción válida")
                input("Presione ENTER para continuar...")

