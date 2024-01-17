class Movie:
    def __init__(self, id = None, nombre = None, anio = None, genero = None):
        self._id = id
        self._nombre = nombre
        self._anio = anio
        self._genero = genero
    
    def __str__(self):
        return f"""
            [+] id: {self._id}
            [+] nombre: {self._nombre}
            [+] anio: {self._anio}
            [+] genero: {self._genero}
        """

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero



if __name__ == "__main__":
    movie = Movie(1, 'El padrino', 1972, 'Drama')
    print(movie)
    print(f"[+] El nombre es: {movie.nombre}")
    movie.nombre = 'El padrino 2'
    print(f"[+] El nombre es: {movie.nombre}")
    print(movie)