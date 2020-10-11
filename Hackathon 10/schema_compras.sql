-- Database: colegio

-- DROP DATABASE colegio;

CREATE DATABASE colegio
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Peru.1252'
    LC_CTYPE = 'Spanish_Peru.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- ######################################
-- ######## Esquema de Roles ############
-- ######################################

-- roles
-- Table: public.roles

-- DROP TABLE public.roles;

CREATE TABLE public.roles
(
    id_rol SERIAL, --('roles_id_rol_seq'::regclass),
    nombre character varying(150) COLLATE pg_catalog."default",
    contrasena character varying(150) COLLATE pg_catalog."default",
    cargo character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT roles_pkey PRIMARY KEY (id_rol)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.roles
    OWNER to postgres;

-- POR FAVOR COLOCAR LA SENTENCIA SIGUIENTE
-- Esto va generar un usuario administrado, cuyos datos seran:
-- usuario: admin
-- contraseña: password
-- cargo: admin
-- Esto para poder utilizar bien el programa, y se puede registrar más usuarios con cargo admin o lector.

INSERT INTO roles (nombre, contrasena, cargo) VALUES
('admin', 'password', 'admin')

-- ######################################
-- ############# Tablas #################
-- ######################################


-- TABLAS
-- alumnos

-- Table: public.alumnos

-- DROP TABLE public.alumnos;

CREATE TABLE public.alumnos
(
    id_alumno SERIAL, --('alumnos_id_alumno_seq'::regclass),
    nombre character varying(150) COLLATE pg_catalog."default",
    codigo character varying(150) COLLATE pg_catalog."default",
    salon character varying(150) COLLATE pg_catalog."default",
    id_periodo_nota1 SERIAL,
    id_periodo_nota2 SERIAL,
    id_periodo_nota3 SERIAL,
    id_periodo_nota4 SERIAL,
    CONSTRAINT alumnos_pkey PRIMARY KEY (id_alumno)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.alumnos
    OWNER to postgres;

-- alumnos
-- Table: public.alumnos

-- DROP TABLE public.alumnos;


-- TABLAS
-- profesor

-- Table: public.profesor

-- DROP TABLE public.profesor;

CREATE TABLE public.profesor
(
    id_profesor SERIAL, --('profesor_id_profesor_seq'::regclass),
    nombre character varying(150) COLLATE pg_catalog."default",
    dni character varying(150) COLLATE pg_catalog."default",
    curso character varying(150) COLLATE pg_catalog."default",
    salon_1 character varying(150) COLLATE pg_catalog."default",
    salon_2 character varying(150) COLLATE pg_catalog."default",
    salon_3 character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT profesor_pkey PRIMARY KEY (id_profesor)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.profesor
    OWNER to postgres;

-- profesor
-- Table: public.profesor

-- DROP TABLE public.profesor;


-- TABLAS
-- periodo_nota1

-- Table: public.periodo_nota1

-- DROP TABLE public.periodo_nota1;

CREATE TABLE public.periodo_nota1
(
    id_periodo_nota1 SERIAL, --('periodo_nota1_id_periodo_nota1_seq'::regclass),
    matematica decimal,
    religion decimal,
    comunicacion decimal,
    ingles decimal,
    historia decimal,
    promedio decimal,
    CONSTRAINT periodo_nota1_pkey PRIMARY KEY (id_periodo_nota1)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.periodo_nota1
    OWNER to postgres;

-- periodo_nota1
-- Table: public.periodo_nota1

-- DROP TABLE public.periodo_nota1;


-- TABLAS
-- periodo_nota2

-- Table: public.periodo_nota2

-- DROP TABLE public.periodo_nota2;

CREATE TABLE public.periodo_nota2
(
    id_periodo_nota2 SERIAL, --('periodo_nota2_id_periodo_nota2_seq'::regclass),
    matematica decimal,
    religion decimal,
    comunicacion decimal,
    ingles decimal,
    historia decimal,
    promedio decimal,
    CONSTRAINT periodo_nota2_pkey PRIMARY KEY (id_periodo_nota2)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.periodo_nota2
    OWNER to postgres;

-- periodo_nota2
-- Table: public.periodo_nota2

-- DROP TABLE public.periodo_nota2;


-- TABLAS
-- periodo_nota3

-- Table: public.periodo_nota3

-- DROP TABLE public.periodo_nota3;

CREATE TABLE public.periodo_nota3
(
    id_periodo_nota3 SERIAL, --('periodo_nota3_id_periodo_nota3_seq'::regclass),
    matematica decimal,
    religion decimal,
    comunicacion decimal,
    ingles decimal,
    historia decimal,
    promedio decimal,
    CONSTRAINT periodo_nota3_pkey PRIMARY KEY (id_periodo_nota3)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.periodo_nota3
    OWNER to postgres;

-- periodo_nota3
-- Table: public.periodo_nota3

-- DROP TABLE public.periodo_nota3;

-- TABLAS
-- periodo_nota4

-- Table: public.periodo_nota4

-- DROP TABLE public.periodo_nota4;

CREATE TABLE public.periodo_nota4
(
    id_periodo_nota4 SERIAL, --('periodo_nota4_id_periodo_nota4_seq'::regclass),
    matematica decimal,
    religion decimal,
    comunicacion decimal,
    ingles decimal,
    historia decimal,
    promedio decimal,
    CONSTRAINT periodo_nota4_pkey PRIMARY KEY (id_periodo_nota4)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.periodo_nota4
    OWNER to postgres;

-- periodo_nota4
-- Table: public.periodo_nota4

-- DROP TABLE public.periodo_nota4;



-- ###############fin###########
-- ###############fin###########
-- ###############fin###########

-- -- TABLAS
-- -- almacen

-- -- Table: public.almacen

-- -- DROP TABLE public.almacen;

-- CREATE TABLE public.almacen
-- (
--     id_almacen SERIAL, --('almacen_id_almacen_seq'::regclass),
--     codigo character varying(150) COLLATE pg_catalog."default",
--     producto character varying(150) COLLATE pg_catalog."default",
--     precio_por_unidad decimal,
--     cantidad integer,
--     categoria character varying(150) COLLATE pg_catalog."default",
--     CONSTRAINT almacen_pkey PRIMARY KEY (id_almacen)
-- )
-- WITH (
--     OIDS = FALSE
-- )
-- TABLESPACE pg_default;

-- ALTER TABLE public.almacen
--     OWNER to postgres;

-- -- almacen
-- -- Table: public.almacen

-- -- DROP TABLE public.almacen;

-- CREATE TABLE public.ventas
-- (
--     id_ventas SERIAL, --('ventas_id_ventas_seq'::regclass),
--     dni character varying(150) COLLATE pg_catalog."default",
--     producto character varying(150) COLLATE pg_catalog."default",
--     cantidad_comprada integer,
--     precio_total decimal,
--     fecha character varying(150) COLLATE pg_catalog."default",
--     mes_venta character varying(150) COLLATE pg_catalog."default",
--     CONSTRAINT ventas_pkey PRIMARY KEY (id_ventas)
-- )
-- WITH (
--     OIDS = FALSE
-- )
-- TABLESPACE pg_default;

-- ALTER TABLE public.ventas
--     OWNER to postgres;

-- -- ventas
-- -- Table: public.ventas

-- -- DROP TABLE public.ventas;