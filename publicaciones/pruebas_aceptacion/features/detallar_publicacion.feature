Característica: Como usuario revisor del sistema quiero poder ver los detalles de una publicación que debo revisar

    Escenario: Se detalla la revisión correctamente.
        Dado que me encuentro ya logueado como usuario revisor
        Y me dirijo a la pantalla de inicio del sistema
        Y hago click en la pestaña que lleva por nombre "Mis revisiones"
        Y veo el encabezado "Revisar publicaciones"
        Cuando presiono el botón ver en una de las publicaciones de la lista
        Entonces el sistema me muestra el encabezado "Detalles de la revisión"
        Y puedo ver el campo "Título de la publicación"
        Y puedo ver el campo "Autor"
        Y puedo ver el campo "Estado"
        