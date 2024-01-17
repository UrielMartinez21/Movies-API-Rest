from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host = cls._HOST,
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    port = cls._DB_PORT,
                    database = cls._DATABASE
                )
                print("[+] Creación del pool exitosa")
                return cls._pool
            except Exception as e:
                print("[+] Ocurrió un error al obtener el pool")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        print("[+] Conexión obtenida del pool")
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        print("[+] Regresamos la conexión al pool")

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        print(f"[+] Cerramos todas las conexiones del pool")


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        print("[+] Inicio de with método __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        print("[+] Se ejecuta método __exit__")
        if valor_excepcion:
            self._conexion.rollback()
            print(f"[+] Ocurrió una excepción: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}")
        else:
            self._conexion.commit()
            print("[+] Commit de la transacción")
        # Cerramos el cursor
        self._cursor.close()
        # Regresamos la conexión al pool
        Conexion.liberarConexion(self._conexion)


if __name__ == "__main__":
    with CursorDelPool() as cursor:
        print("Dentro del bloque with".center(50, '-'))
        cursor.execute('SELECT * FROM flask_peliculas')
        print("Listado de personas")
        print(cursor.fetchall())