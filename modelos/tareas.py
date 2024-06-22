from . import db

class Tarea(db.Model):
    __tablename__ = 'tareas'
    
    id=db.Column(db.Interger, primary_key=True)
    descripcion=db.Column(db.String(300),nullable=False)
    fecha_maxima=db.Column(db.Date, nullable=False)
    
    def __init__(self,descripcion,fecha_maxima):
        self.descripcion=descripcion
        self.fecha_maxima=fecha_maxima