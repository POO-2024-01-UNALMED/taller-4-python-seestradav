class Asignatura:

    def __init__(self, nombre, salon=None,estudiantes=None):
        self._nombre = nombre
        self._salon = salon
        self.estudiantes=estudiantes
    def __str__(self):
        texto=f"{self._nombre} remoto"
        return texto
