CREATE DATABASE IF NOT EXISTS API_TAREA;
USE API_TAREA;

CREATE TABLE IF NOT EXISTS contacto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(300) NOT NULL,
    fecha_maxima DATE
);