query= {
    'SELECCIONAR': 'SELECT * FROM flask_peliculas ORDER BY id',
    'INSERTAR': 'INSERT INTO flask_peliculas(nombre, anio, genero) VALUES(%s, %s, %s)',
    'ACTUALIZAR': 'UPDATE flask_peliculas SET nombre=%s, anio=%s, genero=%s WHERE id=%s',
    'ELIMINAR': 'DELETE FROM flask_peliculas WHERE id=%s',
    'SELECCIONAR_ID': 'SELECT * FROM flask_peliculas WHERE id=%s'
}