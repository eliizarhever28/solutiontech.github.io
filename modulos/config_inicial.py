import os
from modulos.sistema import SistemaGestion
from modulos.usuarios import Admin


## CREANDO OBJETO DEL SISTEMA

sistema = SistemaGestion()

if not os.path.exists("base_datos_cliente"):
    os.mkdir("base_datos_cliente")

# Crear usuario admin si no existe archivo
if not os.path.exists(sistema.base_datos_usuarios):
    admin = Admin("US001", "admin", "1234")
    datos_admin = admin.mostrar_datos()
    datos_admin["tipo"] = "admin"
    sistema.guardar_usuarios([datos_admin])
