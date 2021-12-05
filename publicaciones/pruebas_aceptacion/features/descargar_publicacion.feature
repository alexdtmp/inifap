Característica: Como usuario revisor del sistema quiero poder descargar una publicación para realizar mi revisión.

    Escenario: Descarga de publicación correcta.
        Dado que me encuentro ya logueado como usuario revisor
        Y me dirijo a la lista de publicaciones que debo revisar 
        Y presiono el botón “Ver publicación” en una de las publicaciones de la lista
        Y el sistema me muestra el detalle de la publicación
        Cuando presiono el botón “Descargar publicación”
        Entonces el sistema comienza la descarga del archivo.