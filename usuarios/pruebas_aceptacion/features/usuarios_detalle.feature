Característica: Detalle usuario
    Como usuario administrador del sistema quiero poder ver una cuenta de usuario ya existente
    para saber sus datos.

    Escenario: Modificar usuario correctamente
        Dado que ingreso al sistema con la dirección "http://192.168.33.10:8000/usuarios/lista"
        Cuando presiono el botón de ver correspondiente a un registro de la lista
        Entonces puedo ver la página de "Detalle del Usuario"