###Validadores generales

##para cadenas de texto en los que no quiero numeros ni caracteres especiales :
def validar_texto(texto):
    """
    Valida que el texto no esté vacío y contenga solo letras y espacios.
    No permite números ni caracteres especiales.
    
    Parámetros:
    - texto: Cadena a validar.
    
    Retorna:
    - bool: True si es válido, False en caso contrario.
    """
    if texto.strip() == "":
        return False
    # Verificamos cada carácter para asegurar solo letras o espacios
    for caracteres in texto:
        if caracteres != " " and not caracteres.isalpha():
            return False
    return True
##Para cadenas de texto corto(como nombre del producto):
def validar_texto_corto(texto):
    """
    Valida texto corto: no vacío, solo letras y espacios, máximo 20 caracteres.
    
    Parámetros:
    - texto: Cadena a validar.
    
    Retorna:
    - bool: True si es válido, False en caso contrario.
    """
    if texto.strip() == "":
        return False
    if len(texto)>20:
        return False
    # Verificamos cada carácter para letras o espacios
    for caracteres in texto:
        if caracteres != " " and not caracteres.isalpha():
            return False
    return True

def validar_texto_numero(texto):
    """
    Valida texto que puede contener letras, números y espacios, máximo 20 caracteres.
    No permite caracteres especiales.
    
    Parámetros:
    - texto: Cadena a validar.
    
    Retorna:
    - bool: True si es válido, False en caso contrario.
    """
    if texto.strip() == "":
        return False
    if len(texto)>20:
        return False
    # Verificamos cada carácter para alfanuméricos o espacios
    for caracteres in texto:
        if caracteres != " " and not caracteres.isalnum():
            return False
    return True
##Para vaalidar el nombre de usuario sin caracteres especiales
def validar_edad(edad):
    """
    Valida numeros: no vacío, debe ser entero y estar entre 18 y 110
    
    Parámetros:
    - edad: numero a validar.
    
    Retorna:
    - bool: True si es válido, False en caso contrario.
    """
    if edad is None or edad == "":
        return False
    try:
        edad_int = int(edad)

        # Verificar rango permitido
        if 18 <= edad_int <= 110:
            return True
        else:
            return False

    except (ValueError, TypeError):
        return False



def validar_usuario(usuario):
    """
    Valida nombre de usuario: no vacío, solo letras, números y espacios.
    No permite caracteres especiales.
    
    Parámetros:
    - usuario: Cadena a validar.
    
    Retorna:
    - bool: True si es válido, False en caso contrario.
    """
    if usuario.strip() == "":
        return False
    # Verificamos cada carácter para alfanuméricos o espacios
    for caracteres in usuario:
        if caracteres != " " and not caracteres.isalnum():
            return False
    return True

##Para precios
def validar_precio(precio):
    """
    Valida precio: debe ser convertible a float y mayor que 0.
    
    Parámetros:
    - precio: Cadena a validar.
    
    Retorna:
    - bool: True si es válido, False en caso contrario.
    """
    if precio.strip() == "":
        return False
    try:
        # Intentamos convertir a float y verificar que sea positivo
        return float(precio) > 0
    except:
        return False

##Para stock
def validar_stock(stock):
    """
    Valida stock: debe ser convertible a int y mayor o igual a 0.
    
    Parámetros:
    - stock: Cadena a validar.
    
    Retorna:
    - bool: True si es válido, False en caso contrario.
    """
    if stock.strip() == "":
        return False
    try:
        # Intentamos convertir a int y verificar que sea no negativo
        return int(stock) >= 0
    except:
        return False

def validacion_numero_telefono(numero):
    """Valida número de teléfono en Chile: debe ser convertible a int, mayor a 0 y debe tener 9 digitos 
    Parámetros: 
    -número: secuencia numerica a validar

    Retorna:
    - bool: True si es válido, False en caso contrario
    """
    if numero is None or numero == "":
        return False
    try:
        numero_int = int(numero)

        if numero_int <= 0:
            return False

        if len(numero) != 9:  #  usar numero ya limpio
            return False

        return True

    except (ValueError, TypeError):
        return False
    
###PARA VLIDAR EL LOGIN
def validacion_login(tipo_usuario, usuarios_validos, clave_correcta, intentos):
    """
    Valida el login de un usuario: verifica usuario en lista y clave correcta.
    Reduce intentos en caso de fallo.
    
    Parámetros:
    - tipo_usuario: Tipo de usuario (e.g., 'administrador').
    - usuarios_validos: Lista de usuarios válidos.
    - clave_correcta: Clave requerida.
    - intentos: Intentos restantes.
    
    Retorna:
    - tuple: (bool acceso, int intentos, str usuario) o (False, intentos, None) si falla.
    """
    usuario = input("Ingrese su nombre de usuario: ").lower().strip()
    clave = input(f"Ingrese la clave de acceso de {tipo_usuario}: ")

    # Verificamos si el usuario está en la lista y la clave es correcta
    if usuario in usuarios_validos and clave == clave_correcta:
        print(f"Acceso correcto como {tipo_usuario}!")
        usuario_sesion_activa=usuario
        return True, intentos, usuario_sesion_activa
    else:
        print("Credenciales incorrectas. Acceso denegado.")
        intentos -= 1

        if intentos == 0:
            print("Has agotado todos los intentos.")
            print("---Ingresando como invitado---")
            return False, intentos, None
        else:
            print("Intente nuevamente o inicie sesión desde otro tipo de usuario")
            print(f"Intentos restantes: {intentos}")

        return False, intentos, None
