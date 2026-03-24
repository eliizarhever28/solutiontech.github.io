import os


## CREANDO EL TÍTULO DEL SISTEMA

def titulo():
    line_1 = "---------------------------------------"
    titulo = "SolutionTech GIC"
    subtitulo = "Plataforma de gestion de clientes"

    ## center() es una función para alinear el texto al centro
    print(line_1.center(130))
    print(titulo.center(130))
    print(subtitulo.center(130))
    print(line_1.center(130))

## FUNCIÓN PARA LIMPIAR LA PANTALLA

def clear_screen():
    # Si el sistema es Windows
    if os.name == 'nt':
        os.system('cls') # Comando para limpiar pantalla en Windows
    else:
        os.system('clear') # Comando para limpiar pantalla en Linux/Mac