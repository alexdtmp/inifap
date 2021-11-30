Característica: Iniciar Sesión
    Como usuario del sistema quiero iniciar sesión para realizar mis actividades.

    Escenario: Iniciar sesión correctamente
        Dado que ingreso al sistema con la dirección "http://192.168.33.10:8000/usuarios/login" 
        Y capturo "admin" en el nombre de usuario
        Y capturo "admin123" en contraseña
        Cuando presiono el botón "Ingresar"
        Entonces puedo ver la página de "Lista de usuarios"
    
    Escenario: Iniciar sesión incorrecto
        Dado que ingreso al sistema con la dirección "http://192.168.33.10:8000/usuarios/login" 
        Y capturo "admin_falso" en el nombre de usuario
        Y capturo "adminfalso" en contraseña
        Cuando presiono el botón "Ingresar"
        Entonces puedo ver la alerta "El usuario o la contraseña no son correctos" en la página