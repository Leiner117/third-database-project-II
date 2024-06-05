------------------------------Participantes---------------------------------------------
create table participantes(
	id serial primary key,
	id_carrera int not null,
	id_competidor int not null,
	dorsal_participante varchar(20) not null
)
select * from participantes
CREATE OR REPLACE procedure insertar_participante(
    in p_id_carrera INT,
    in p_id_competidor INT,
    in p_dorsal_participante VARCHAR
)
AS $$
BEGIN
    INSERT INTO participantes (id_carrera, id_competidor, dorsal_participante)
    VALUES (p_id_carrera, p_id_competidor, p_dorsal_participante);
END;
$$ LANGUAGE plpgsql;
CALL insertar_participante(1, 02, 'DROCO');
CALL insertar_participante(2, 01, 'DRRABC');
CALL insertar_participante(2, 02, 'DROCO');
CREATE OR REPLACE procedure obtener_participantesPorCarrera(
    IN p_id_carrera INT,
    OUT result_set REFCURSOR
)
LANGUAGE plpgsql
AS $$
BEGIN
    OPEN result_set FOR
    SELECT id_carrera, id_competidor, dorsal_participante
    FROM participantes
    WHERE id_carrera = p_id_carrera;
END;
$$;
CREATE OR REPLACE PROCEDURE procesar_participantes_por_carrera(
    IN p_id_carrera INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    ref_cursor REFCURSOR;
    rec RECORD;
BEGIN
    -- Llama al procedimiento para obtener el cursor
    CALL obtener_participantesPorCarrera(p_id_carrera, ref_cursor);

    -- Itera sobre las filas del cursor
    LOOP
        FETCH NEXT FROM ref_cursor INTO rec;
        EXIT WHEN NOT FOUND;
        -- Procesa cada fila obtenida aquí
        RAISE NOTICE 'Carrera: %, Competidor: %, Dorsal: %', rec.id_carrera, rec.id_competidor, rec.dorsal_participante;
    END LOOP;

    -- Cierra el cursor
    CLOSE ref_cursor;
END $$;
CALL procesar_participantes_por_carrera(1); -- se pasa #id carrera

CREATE OR REPLACE procedure modificar_participante(
    in p_id_carrera INT,
    in p_id_competidor INT,
    in p_dorsal_participante VARCHAR
)
AS $$
BEGIN
    UPDATE participantes
    SET dorsal_participante = p_dorsal_participante
    WHERE id_carrera = p_id_carrera;
END;
$$ LANGUAGE plpgsql;
CALL modificar_participante(1, 01, 'DOR5678');
--------------------------------------Tiempos Participantes---------------------------------------------
create table tiempos_participantes(
	id serial primary key,
	id_carrera int not null,
	id_trayecto int not null,
	id_competidor int not null,
	tiempo varchar(30) not null
)

CREATE OR REPLACE procedure insertar_tiempoParticipante(
    in p_id_carrera INT,
    in p_id_trayecto INT,
    in p_id_competidor INT,
    in p_tiempo VARCHAR
)
AS $$
BEGIN
    INSERT INTO tiempos_participantes (id_carrera, id_trayecto, id_competidor, tiempo)
    VALUES (p_id_carrera, p_id_trayecto, p_id_competidor, p_tiempo);
END;
$$ LANGUAGE plpgsql;
select * from tiempos_participantes
CALL insertar_tiempoParticipante(1, 1, 02, '01:37:00');
CALL insertar_tiempoParticipante(2, 1, 01, '01:38:00');
CALL insertar_tiempoParticipante(2, 1, 02, '01:33:00');
CREATE OR REPLACE procedure obtener_tiempo_participantes(
    IN p_id_carrera INT,
    IN p_id_trayecto INT,
    OUT result_set REFCURSOR
)
LANGUAGE plpgsql
AS $$
BEGIN
    OPEN result_set FOR
    SELECT id_carrera, id_trayecto, id_competidor, tiempo
    FROM tiempos_participantes
    WHERE id_carrera = p_id_carrera AND id_trayecto = p_id_trayecto;
END;
$$;

CREATE OR REPLACE PROCEDURE procesar_tiempos_participantes(
    IN p_id_carrera INT,
    IN p_id_trayecto INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    ref_cursor REFCURSOR;
    rec RECORD;
BEGIN
    -- Llama al procedimiento para obtener el cursor
    CALL obtener_tiempo_participantes(p_id_carrera, p_id_trayecto, ref_cursor);

    -- Itera sobre las filas del cursor
    LOOP
        FETCH NEXT FROM ref_cursor INTO rec;
        EXIT WHEN NOT FOUND;
        -- Procesa cada fila obtenida aquí
        RAISE NOTICE 'Carrera: %, Trayecto: %, Competidor: %, Tiempo: %', rec.id_carrera, rec.id_trayecto, rec.id_competidor, rec.tiempo;
    END LOOP;

    -- Cierra el cursor
    CLOSE ref_cursor;
END $$;
CALL procesar_tiempos_participantes(1, 1);  -- se pasa #id carrera, #id trayecto 

CREATE OR REPLACE procedure actualizar_tiempo_participante(
    in p_id_carrera INT,
    in p_id_trayecto INT,
    in p_id_competidor INT,
    in p_tiempo VARCHAR
)
AS $$
BEGIN
    UPDATE tiempos_participantes
    SET tiempo = p_tiempo
    WHERE id_carrera = p_id_carrera AND id_trayecto = p_id_trayecto and id_competidor = p_id_competidor;
END;
$$ LANGUAGE plpgsql;
CALL actualizar_tiempo_participante(1, 10, 01, '01:25:00');

CREATE OR REPLACE procedure eliminar_tiempo_participante(
	p_id_competidor INT,
    p_id_carrera INT,
    p_id_trayecto INT
)
AS $$
BEGIN
    DELETE FROM tiempos_participantes WHERE id_carrera = p_id_carrera AND id_trayecto = p_id_trayecto and id_competidor=p_id_competidor ;
END;
$$ LANGUAGE plpgsql;
CALL eliminar_tiempo_participante(01, 1, 10);