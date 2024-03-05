from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas 
        self.listadoAlumnos = estudiantes 

    def listadoAsignaturas(self, **kwargs):
        for asignatura_nombre in kwargs.values():
            asignatura=Asignatura(asignatura_nombre)
            self._asignaturas.append(asignatura)

    def agregarAlumno(self, alumno, lista=None):
        if lista==None:
             lista=[]
        lista.append(alumno)
        self.listadoAlumnos=self.listadoAlumnos + lista     

    def __str__(self):
       x=f"Grupo de estudiantes: {self._grupo}"
       return x
    @ classmethod
    def asignarNombre(cls,nombre):
            cls.grado= nombre
    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre
    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
            cls.grado = nombre
    
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
    

   
