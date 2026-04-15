import sqlite3

#  Conexion 
conn = sqlite3.connect('zoo.db')
cursor = conn.cursor()

# TABLA ANIMALES
cursor.execute("""
CREATE TABLE IF NOT EXISTS animales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    especie TEXT NOT NULL,
    fecha_nacimiento TEXT NOT NULL
)
""")

# TABLA HABITATS
cursor.execute("""
CREATE TABLE IF NOT EXISTS habitats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo_clima TEXT NOT NULL
)
""")

# TABLA CUIDADORES 
cursor.execute("""
CREATE TABLE IF NOT EXISTS cuidadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    experiencia INTEGER NOT NULL
)
""")

# TABLA ASIGNACIONES
cursor.execute("""
CREATE TABLE IF NOT EXISTS asignaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    animal_id INTEGER,
    habitat_id INTEGER,
    FOREIGN KEY(animal_id) REFERENCES animales(id),
    FOREIGN KEY(habitat_id) REFERENCES habitats(id)
)
""")

# TABLA CUIDADO
cursor.execute("""
CREATE TABLE IF NOT EXISTS cuidado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    animal_id INTEGER,
    cuidador_id INTEGER,
    FOREIGN KEY(animal_id) REFERENCES animales(id),
    FOREIGN KEY(cuidador_id) REFERENCES cuidadores(id)
)
""")

# INSERTAR ANIMALES
cursor.execute("""
INSERT INTO animales (nombre, especie, fecha_nacimiento)
VALUES ('Simba', 'León', '2018-05-10')
""")

cursor.execute("""
INSERT INTO animales (nombre, especie, fecha_nacimiento)
VALUES ('Dumbo', 'Elefante', '2015-03-20')
""")

# INSERTAR HABITATS
cursor.execute("""
INSERT INTO habitats (nombre, tipo_clima)
VALUES ('Sabana', 'Caliente')
""")

cursor.execute("""
INSERT INTO habitats (nombre, tipo_clima)
VALUES ('Selva', 'Húmedo')
""")

# INSERTAR CUIDADORES
cursor.execute("""
INSERT INTO cuidadores (nombre, experiencia)
VALUES ('Carlos', 5)
""")

cursor.execute("""
INSERT INTO cuidadores (nombre, experiencia)
VALUES ('Ana', 8)
""")

# ASIGNACIONES 
cursor.execute("""
INSERT INTO asignaciones (fecha, animal_id, habitat_id)
VALUES ('2026-01-01', 1, 1)
""")

cursor.execute("""
INSERT INTO asignaciones (fecha, animal_id, habitat_id)
VALUES ('2026-01-02', 2, 2)
""")

# RELACION
cursor.execute("""
INSERT INTO cuidado (animal_id, cuidador_id)
VALUES (1, 1)
""")

cursor.execute("""
INSERT INTO cuidado (animal_id, cuidador_id)
VALUES (2, 2)
""")

conn.commit()

# CONSULTAS 

print("\n ANIMALES:")
for row in cursor.execute("SELECT * FROM animales"):
    print(row)

print("\n HABITATS:")
for row in cursor.execute("SELECT * FROM habitats"):
    print(row)

print("\n CUIDADORES:")
for row in cursor.execute("SELECT * FROM cuidadores"):
    print(row)

print("\n ASIGNACIONES:")
for row in cursor.execute("SELECT * FROM asignaciones"):
    print(row)

# CERRAR
conn.close()

