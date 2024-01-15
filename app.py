from flask import Flask
from src.config.conexion import config
from psycopg2 import connect

app = Flask(__name__)

# --------------------------| Configuracion |--------------------------
conexion = connect(
    user=config['development'].USER_DB,
    password=config['development'].PASS_DB,
    host=config['development'].URL_DB,
    database=config['development'].NAME_DB
)

# --------------------------| Rutas |--------------------------
@app.route('/')
def inicio():
    return 'Api de peliculas'


@app.route('/api/peliculas', methods=['GET'])
def listar_peliculas():
    try:
        with conexion.cursor() as cursor:
            cursor.execute('SELECT * FROM flask_peliculas')
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

# --------------------------| Manejo de errores |--------------------------
def pagina_no_encontrada():
    return '<h1>La pagina no fue encontrada</h1>'


# --------------------------| Funcion principal |--------------------------
if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)