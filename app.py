from flask import Flask, request
from src.config.conexion import CursorDelPool
from src.querys.querys import query
from src.model.movie import Movie


app = Flask(__name__)


# --------------------------| Rutas |--------------------------
@app.route('/')
def inicio():
    return 'Api de peliculas'


@app.route('/api/peliculas', methods=['GET'])
def listar_peliculas():
    try:
        with CursorDelPool() as cursor:
            cursor.execute(query['SELECCIONAR'])
            peliculas = cursor.fetchall()

        # Convertir listado a diccionario
        for i, pelicula in enumerate(peliculas):
            peliculas[i] = {
                'id': pelicula[0],
                'nombre': pelicula[1],
                'anio': pelicula[2],
                'genero': pelicula[3]
            }
        return peliculas, 200
    except Exception as e:
        return {'msg': e}, 500


@app.route('/api/peliculas/<int:id>', methods=['GET'])
def obtener_pelicula(id):
    try:
        with CursorDelPool() as cursor:
            cursor.execute(query['SELECCIONAR_ID'], (id,))
            pelicula = cursor.fetchone()

        # Convertir listado a diccionario
        pelicula = {
            'id': pelicula[0],
            'nombre': pelicula[1],
            'anio': pelicula[2],
            'genero': pelicula[3]
        }
        return pelicula, 200
    except Exception as e:
        return {'msg': e}, 500


@app.route('/api/peliculas', methods=['POST'])
def crear_pelicula():
    try:
        with CursorDelPool() as cursor:
            movie = Movie()
            movie.nombre = request.json["nombre"]
            movie.anio = request.json["anio"]
            movie.genero = request.json["genero"]
            cursor.execute(query['INSERTAR'], (movie.nombre, movie.anio, movie.genero))
            return {'msg': 'Pelicula creada', 'movie': movie.nombre}, 201
    except Exception as e:
        return {'msg': e}, 500


@app.route('/api/peliculas/<int:id>', methods=['PUT'])
def actualizar_pelicula(id):
    try:
        with CursorDelPool() as cursor:
            movie = Movie()
            movie.nombre = request.json["nombre"]
            movie.anio = request.json["anio"]
            movie.genero = request.json["genero"]
            cursor.execute(query['ACTUALIZAR'], (movie.nombre, movie.anio, movie.genero, id))
            return {'msg': 'Pelicula actualizada', 'movie': movie.nombre}, 200
    except Exception as e:
        return {'msg': e}, 500


@app.route('/api/peliculas/<int:id>', methods=['DELETE'])
def eliminar_pelicula(id):
    try:
        with CursorDelPool() as cursor:
            cursor.execute(query['ELIMINAR'], (id,))
            return {'msg': 'Pelicula eliminada'}, 200
    except Exception as e:
        return {'msg': e}, 500


# --------------------------| Manejo de errores |--------------------------
def pagina_no_encontrada(error):
    return '<h1>La pagina no fue encontrada</h1>'


# --------------------------| Funcion principal |--------------------------
if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)