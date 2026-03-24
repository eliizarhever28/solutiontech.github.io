from modulos.config_inicial import sistema
from modulos.otras_funciones import clear_screen, titulo
from modulos.usuarios import Admin


##LOGIN OBLIGATORIO

"""
CREDENCIALES PARA INICIO DE SESION POR PRIMERA VEZ
USUARIO: admin
CONTRASEÑA: 1234

"""

usuario_activo=None

while usuario_activo is None:
    usuario_activo = sistema.login()


## MENÚ PRINCIPAL
while True:
    clear_screen()
    titulo()
    print(f"\nUsuario: {usuario_activo.username} | Tipo: {usuario_activo.mostrar_tipo().capitalize()}\n\n")


    print("1. Listar clientes")
    print("2. Agregar cliente")
    print("3. Buscar clientes")
    print("4. Modificar cliente")
    print("5. Eliminar cliente")

    # Mostrar opción para agregar usuarios solo si es admin
    if isinstance(usuario_activo, Admin):
        print("6. Agregar usuario")
        print("7. Eliminar usuario")
        print("8. Salir")
    else:
        print("6. Salir")

    try:
        opcion_menu = int(input("Seleccione una opción: "))
    except ValueError:
        clear_screen()
        print("")
        print("Debe ingresar una opción válida".center(130))
        input("Presione ENTER para continuar...".center(130))
        continue

    if opcion_menu == 1:
        sistema.listar_cliente()
    elif opcion_menu == 2:
        sistema.agregar_cliente()
    elif opcion_menu == 3:
        sistema.buscar_clientes()
    elif opcion_menu == 4:
        sistema.modificar_cliente()
    elif opcion_menu == 5:
        sistema.eliminar_cliente()
    elif opcion_menu == 6 and isinstance(usuario_activo, Admin):
        usuario_activo.agregar_usuario(sistema)
    elif opcion_menu == 7 and isinstance(usuario_activo, Admin):
        sistema.eliminar_usuario(usuario_activo)
    elif (opcion_menu == 6 and not isinstance(usuario_activo, Admin)) or (opcion_menu == 8 and isinstance(usuario_activo, Admin)):
        clear_screen()
        line_1 = "---------------------------------------"
        mensaje = "SolutionTech GIC"
        subtitulo = "Plataforma de gestion de clientes"
        final = "...Saliendo del sistema..."
        print(line_1.center(130))
        print(mensaje.center(130))
        print(subtitulo.center(130))
        print(line_1.center(130))
        print(final.center(130))
        print(line_1.center(130))
        break
    else:
        clear_screen()
        print("")
        print("Opción inválida".center(130))
        input("Presione ENTER para continuar...".center(130))

