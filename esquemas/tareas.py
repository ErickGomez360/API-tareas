from . import ma
from modelos.tareas import Tarea

class TareaEsquema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tarea
        load_instance = True

tarea_esquemas = TareaEsquema()
tareas_esquema = TareaEsquema(many=True)