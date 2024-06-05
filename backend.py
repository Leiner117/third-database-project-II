from bd import Bd
cursor = Bd().cursor
connection = Bd().connection
# Recuperar todos los competirdores de la base de datos
def get_competidores():
    cursor.execute("SELECT * FROM COMPETIDORES")
    return cursor.fetchall()

# Recuperar todas las carreras de la base de datos
def get_carreras():
    cursor.execute("SELECT * FROM CARRERAS")
    return cursor.fetchall()

#Recuperar todos los trayectos de la base de datos
def get_trayectos():
    cursor.execute("SELECT * FROM TRAYECTOS")
    return cursor.fetchall()

#Recuperar todos los tiempos de la base de datos
def get_tiempos():
    cursor.execute("SELECT * FROM TIEMPOS_COMPETIDORES")
    return cursor.fetchall()

# Agregar competidor a la base de datos
def add_competidor(nombre, edad, sexo):
    cursor.execute("INSERT INTO COMPETIDORES (NOMBRE, EDAD, SEXO) VALUES (:1, :2, :3)", (nombre, edad, sexo))
    connection.commit()
    
# Agregar carrera a la base de datos
def add_carrera(nombre, fecha, maximos_competidores, lugar, hora_salida):
    fecha_hora = f"{fecha} {hora_salida}"
    cursor.execute("INSERT INTO CARRERAS (NOMBRE, FECHA, maximo_competidores,COMPETIDORES_REGISTRADOS, lugar, hora_salida) VALUES (:1, TO_TIMESTAMP(:2, 'DD-MM-YYYY HH24:MI'), :3, :4,:5, TO_TIMESTAMP(:6, 'DD-MM-YYYY HH24:MI'))", (nombre, fecha_hora, maximos_competidores,0, lugar, fecha_hora))
    connection.commit()

# Agregar trayecto a la base de datos

def add_trayecto(id_carrera, nombre, distancia):
    cursor.execute("INSERT INTO TRAYECTOS (CARRERA_ID, NOMBRE, DISTANCIA_KM) VALUES (:1, :2, :3)", (id_carrera, nombre, distancia))
    connection.commit()

# Agregar tiempo a la base de datos

def add_tiempo(id_competidor, id_trayecto, tiempo):
    cursor.execute("INSERT INTO TIEMPOS_COMPETIDORES (COMPETIDOR_ID, TRAYECTO_ID, TIEMPO) VALUES (:1, :2, TO_TIMESTAMP(:3, 'DD-MM-YYYY HH24:MI'))", (id_competidor, id_trayecto, tiempo))
    connection.commit()

# Asociar competidro a carrera, la tabla competidor tiene un atributo de carrera_id que se actualiza con el id de la carrera y aumentar en la tabla carreras el numero de competidores registrados

def asociar_competidor_carrera(id_competidor, id_carrera):
    cursor.execute("UPDATE COMPETIDORES SET CARRERA_ID = :1 WHERE ID = :2", (id_carrera, id_competidor))
    cursor.execute("UPDATE CARRERAS SET COMPETIDORES_REGISTRADOS = COMPETIDORES_REGISTRADOS + 1 WHERE ID = :1", (id_carrera,))
    connection.commit()

# Acutalizar competidores
def update_competidor(id_competidor, nombre, edad, sexo):
    cursor.execute("UPDATE COMPETIDORES SET NOMBRE = :1, EDAD = :2, SEXO = :3 WHERE ID = :4", (nombre, edad, sexo, id_competidor))
    connection.commit()

# Acutalizar carreras
def update_carrera(id_carrera, nombre, fecha, maximos_competidores, lugar, hora_salida):
    fecha_hora = f"{fecha} {hora_salida}"
    cursor.execute("UPDATE CARRERAS SET NOMBRE = :1, FECHA = TO_TIMESTAMP(:2, 'DD-MM-YYYY HH24:MI'), maximo_competidores = :3, lugar = :4, hora_salida = TO_TIMESTAMP(:5, 'DD-MM-YYYY HH24:MI') WHERE ID = :6", (nombre, fecha_hora, maximos_competidores, lugar, fecha_hora, id_carrera))
    connection.commit()

# Acutalizar trayectos
def update_trayecto(id_trayecto, id_carrera, nombre, distancia):
    cursor.execute("UPDATE TRAYECTOS SET CARRERA_ID = :1, NOMBRE = :2, DISTANCIA_KM = :3 WHERE ID = :4", (id_carrera, nombre, distancia, id_trayecto))
    connection.commit()

# Acutalizar tiempos
def update_tiempo(id_tiempo, id_competidor, id_trayecto, tiempo):
    cursor.execute("UPDATE TIEMPOS_COMPETIDORES SET COMPETIDOR_ID = :1, TRAYECTO_ID = :2, TIEMPO = TO_TIMESTAMP(:3, 'DD-MM-YYYY HH24:MI') WHERE ID = :4", (id_competidor, id_trayecto, tiempo, id_tiempo))
    connection.commit()

# Eliminar competidor
def delete_competidor(id_competidor):
    cursor.execute("DELETE FROM COMPETIDORES WHERE ID = :1", (id_competidor,))
    connection.commit()

# Eliminar carrera
def delete_carrera(id_carrera):
    cursor.execute("DELETE FROM CARRERAS WHERE ID = :1", (id_carrera,))
    connection.commit()

# Eliminar trayecto
def delete_trayecto(id_trayecto):
    cursor.execute("DELETE FROM TRAYECTOS WHERE ID = :1", (id_trayecto,))
    connection.commit()

# Eliminar tiempo
def delete_tiempo(id_tiempo):
    cursor.execute("DELETE FROM TIEMPOS_COMPETIDORES WHERE ID = :1", (id_tiempo,))
    connection.commit()

# Eliminar competidor de carrera
def delete_competidor_carrera(id_competidor):
    cursor.execute("UPDATE CARRERAS SET COMPETIDORES_REGISTRADOS = COMPETIDORES_REGISTRADOS - 1 WHERE ID = (SELECT CARRERA_ID FROM COMPETIDORES WHERE ID = :1)", (id_competidor,))
    cursor.execute("UPDATE COMPETIDORES SET CARRERA_ID = NULL WHERE ID = :1", (id_competidor,))
    connection.commit()
