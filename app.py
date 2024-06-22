from flask import Flask, request, jsonify
from config import Config
from modelos import db
from modelos.tareas import Tarea
from esquemas.tareas import ma, tarea_esquemas,tareas_esquema

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all() 
    
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    descripcion=request.json['descripcion']
    fecha_maxima=request.json['fecha_maxima']
    tarea_nueva=Tarea(descripcion, fecha_maxima)
    db.session.add(tarea_nueva)
    db.session.commit()
    return tarea_esquemas.jsonify(tarea_nueva)

@app.route('/tareas', methods=['GET'])
def listar_tareas():
    total_tareas=Tarea.query.all()
    resultado=tareas_esquema.dump(total_tareas)
    return jsonify(resultado)

@app.route('/tareas/<int:id>', methods=['GET'])
def obtener_tarea(id):
    tarea=Tarea.query.get(id)
    if tarea is None:
        return jsonify({"mensaje":"Tarea no encontrada"}), 404
    return tarea_esquemas.jsonify(tarea)

@app.route('/tareas/<int:id>', methods=['PUT'])
def modificar_tarea(id):
    tarea=Tarea.query.get(id)
    if tarea is None:
        return jsonify({"mensaje":"Tarea no encontrada"}), 404
    
    descripcion=request.json.get('descripcion', tarea.descripcion)
    fecha_maxima=request.json.get('fecha_maxima', tarea.fecha_maxima)
    
    tarea.descripcion=descripcion
    tarea.fecha_maxima=fecha_maxima
    db.session.commit()
    return tarea_esquemas.jsonify(tarea)

@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    tarea=Tarea.query.get(id)
    if tarea is None:
        return jsonify({"mensaje":"Tarea no encontrada"}), 404
    
    db.session.delete(tarea)
    db.session.commit()
    return jsonify({"mensaje":"Tarea eliminada"})

if __name__=='__main__':
    app.run(debug=True)