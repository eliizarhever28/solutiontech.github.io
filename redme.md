# Sistema de Gestión de Clientes GIC

**Sistema de Gestión de Clientes GIC** es una plataforma desarrollada en **Python** utilizando **Programación Orientada a Objetos (POO)**, diseñada para administrar de manera eficiente la información de clientes y usuarios dentro de una organización.  

El objetivo principal del proyecto es proporcionar una herramienta **modular, escalable y segura**, que permita:

- Gestionar clientes de diferentes tipos (Regular, Premium y Corporativo).  
- Realizar validaciones en línea sobre datos ingresados, garantizando integridad y consistencia.  
- Administrar usuarios con distintos niveles de permisos (Administradores y Trabajadores).  
- Integrarse con servicios externos o bases de datos JSON locales, asegurando persistencia de datos.  

El sistema está estructurado para facilitar futuras ampliaciones y mantenimiento, separando claramente la **lógica de negocio**, las **clases del modelo** y las **funciones utilitarias**.


## Tecnologías y Herramientas

- **Python 3.x**  
- **POO (Programación Orientada a Objetos)**  
- **JSON** para almacenamiento persistente de datos  
- Estructura modular
- Validaciones personalizadas de datos (texto, números, teléfonos, edades)  

## Flujo de Funcionamiento

1. **Inicio del Sistema**  
   - Al ejecutar `main.py`, el sistema verifica la existencia de la base de datos de usuarios.  
   - Si no existe, crea un usuario admin predeterminado (`username: admin`, `password: 1234`).  

2. **Login Obligatorio**  
   - Se solicita usuario y contraseña.  
   - Según el tipo de usuario (`Admin` o `Trabajador`), se habilitan diferentes opciones en el menú.  

3. **Menú Principal**  
   - Listar clientes  
   - Agregar cliente  
   - Buscar clientes  
   - Modificar cliente  
   - Eliminar cliente  
   - (Solo Admin) Agregar usuario  
   - (Solo Admin) Eliminar usuario  
   - Salir del sistema  

4. **Gestión de Clientes**  
   - Los clientes se pueden agregar como **Regular, Premium o Corporativo**.  
   - Cada cliente tiene atributos como: ID, nombre, apellido, teléfono, edad, ciudad, género y fecha de registro.  
   - Se realizan **validaciones en línea** para garantizar que los datos ingresados sean correctos y consistentes.  

5. **Gestión de Usuarios**  
   - Los administradores pueden agregar y eliminar usuarios.  
   - Los trabajadores solo pueden operar sobre clientes, sin permisos de administración.  

6. **Persistencia de Datos**  
   - La información se guarda en archivos JSON (`clientes.json` y `usuarios.json`) dentro de la carpeta `base_datos_cliente`.  
   - Se asegura que los datos sean válidos antes de guardarlos, evitando corrupción de la base de datos.  

---

## Funcionalidades Principales

### Clientes
- **Agregar cliente**: Crear nuevos clientes con validación de datos.  
- **Listar clientes**: Mostrar todos los clientes registrados con formato tabular.  
- **Buscar clientes**: Permite búsqueda por nombre o ID.  
- **Modificar cliente**: Actualizar cualquier campo del cliente, manteniendo validaciones.  
- **Eliminar cliente**: Remover un cliente de la base de datos de manera segura.  

### Usuarios
- **Agregar usuario (Admin)**: Crear nuevos usuarios con roles definidos.  
- **Eliminar usuario (Admin)**: Eliminar usuarios existentes.  
- **Login seguro**: Solo permite acceso con credenciales correctas.  

### Utilidades
- Limpieza de pantalla (`clear_screen`) para mejor experiencia de usuario.  
- Título del sistema (`titulo`) centrado y estético.  
- Generación automática de IDs únicos para clientes y usuarios.  

---

## Objetivos del Sistema

- **Modularidad**: Separar clases, funciones y lógica de negocio en distintos archivos para mayor claridad.  
- **Seguridad**: Protección de atributos críticos (como ID y contraseña) mediante encapsulamiento.  
- **Validaciones robustas**: Garantizar integridad de datos ingresados por el usuario.  
- **Escalabilidad**: Facilitar futuras integraciones con bases de datos externas o nuevas funcionalidades.  

---

## Credenciales de Inicio de Sesión (Primera Ejecución)

- **Usuario:** admin  
- **Contraseña:** 1234  
