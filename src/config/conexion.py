# --> Conexion con postgresql
class DevelopmentConfig():
    DEBUG = True
    USER_DB = 'postgres'
    PASS_DB = 'admin'
    URL_DB = 'localhost'
    NAME_DB = 'test_db'

# --> Configuracion de la app
config = {
    'development': DevelopmentConfig,
}