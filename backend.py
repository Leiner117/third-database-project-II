from bd import Bd
from bd_local import Bd_local
cursor = Bd().cursor
connection = Bd().connection
cursor_local = Bd_local().cursor
connection_local = Bd_local().conn
# Recuperar todos los competirdores de la base de datos
def get_competidores():
    cursor.execute("SELECT * FROM COMPETIDORES")
    return cursor.fetchall()

# Recuperar todas las carreras de la base de datos
def get_carreras():
    cursor.execute("""
        SELECT 
            ID, 
            Nombre, 
            CASE 
                WHEN TO_CHAR(Fecha, 'YYYY') = '0000' THEN NULL 
                ELSE TO_CHAR(Fecha, 'DD-MM-YYYY HH24:MI') 
            END AS Fecha, 
            Maximo_Competidores, 
            Lugar, 
            CASE 
                WHEN TO_CHAR(Hora_Salida, 'YYYY') = '0000' THEN NULL 
                ELSE TO_CHAR(Hora_Salida, 'DD-MM-YYYY HH24:MI') 
            END AS Hora_Salida 
        FROM CARRERAS
        WHERE Fecha >= CURRENT_DATE
        ORDER BY Fecha DESC
    """)
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

# agregar participante a la base_local (id_carrera, id_competidor,dorsal), usar el procedimiento almacenado agregar_participante
def add_participante(id_carrera, id_competidor, dorsal):
    #verificar que la carrera exista en la base de datos central
    cursor.execute("SELECT * FROM CARRERAS WHERE ID = :1", (id_carrera,))
    carrera = cursor.fetchone()
    if not carrera:
        return
    #verificar que el competidor exista en la base de datos central
    cursor.execute("SELECT * FROM COMPETIDORES WHERE ID = :1", (id_competidor,))
    competidor = cursor.fetchone()
    if not competidor:
        return
    #verificar que el participante no este ya registrado
    cursor_local.execute("SELECT * FROM PARTICIPANTES WHERE id_carrera = %s AND id_competidor = %s", (id_carrera, id_competidor))
    participante = cursor_local.fetchone()
    if participante:
        return
    cursor_local.execute("CALL insertar_participante(%s, %s, %s)", (id_carrera, id_competidor, dorsal))
    connection_local.commit()

# agregar tiempo a la base_local (id_carrera, id_competidor, id_trayecto, tiempo), usar el procedimiento almacenado agregar_tiempo
def add_tiempo_local(id_carrera, id_competidor, id_trayecto, tiempo):
    #verificar que la carrera exista en la base de datos central
    cursor.execute("SELECT * FROM CARRERAS WHERE ID = :1", (id_carrera,))
    carrera = cursor.fetchone()
    if not carrera:
        return
    #verificar que el competidor exista en la base de datos central
    cursor.execute("SELECT * FROM COMPETIDORES WHERE ID = :1", (id_competidor,))
    competidor = cursor.fetchone()
    if not competidor:
        return
    #verificar que el trayecto exista en la base de datos central
    cursor.execute("SELECT * FROM TRAYECTOS WHERE ID = :1", (id_trayecto,))
    trayecto = cursor.fetchone()
    if not trayecto:
        return
    cursor_local.execute("CALL insertar_tiempoParticipante(%s, %s, %s, %s)", (id_carrera, id_trayecto,id_competidor,tiempo))
    connection_local.commit()

# actualizar datos de participante en la base_local (id_carrera, id_competidor, dorsal), usar el procedimiento almacenado actualizar_participante
def update_participante(id_carrera, id_competidor, dorsal):
    cursor_local.execute("CALL modificar_participante(%s, %s, %s)", (id_carrera, id_competidor, dorsal))
    connection_local.commit()

#eliminar participante de la base_local (id_competidor), no hay procedure
def delete_participante(id_competidor):
    cursor_local.execute("DELETE FROM PARTICIPANTES WHERE id_competidor = %s", (id_competidor,))
    connection_local.commit()

# modificar tiempo participante
def update_tiempo_local(id_carrera, id_competidor, id_trayecto, tiempo):
    cursor_local.execute("CALL actualizar_tiempo_participante(%s, %s, %s, %s)", (id_carrera, id_trayecto, id_competidor, tiempo))
    connection_local.commit()

# eliminar tiempo participante, con procedure
def delete_tiempo_local(id_carrera, id_competidor, id_trayecto):
    cursor_local.execute("CALL eliminar_tiempo_participante(%s, %s, %s)", (id_competidor,id_carrera, id_trayecto ))
    connection_local.commit()

# obtener todos participantes  y sus tiempos de una carrera del nodo local
def get_participantes_tiempos(id_carrera):
    cursor_local.execute("SELECT * FROM PARTICIPANTES WHERE id_carrera = %s", (id_carrera,))
    participantes = cursor_local.fetchall()
    for participante in participantes:
        cursor_local.execute("SELECT * FROM tiempos_participantes WHERE id_carrera = %s AND id_competidor = %s", (id_carrera, participante[1]))
        tiempos = cursor_local.fetchall()
        participante.append(tiempos)
    return participantes

# obtener carrera con id
def get_carrera_by_id(id_carrera):
    cursor.execute("SELECT * FROM CARRERAS WHERE ID = :1", (id_carrera,))
    return cursor.fetchone()

def get_times_by_participant(id_competidor):
    cursor_local.execute("SELECT * FROM TIEMPOS_PARTICIPANTES WHERE id_competidor = %s", (id_competidor,))
    return cursor_local.fetchall()

#obtener la lista de participantes del nodo local
def get_participantes():
    cursor_local.execute("SELECT * FROM PARTICIPANTES")
    return cursor_local.fetchall()