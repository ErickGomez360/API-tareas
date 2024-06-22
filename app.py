from flask import Flask, request, jsonify
from config import Config
from modelos import db
from modelos.tareas import Tarea
from esquemas.tareas import ma, tarea_esquemas,tareas_esquema

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

