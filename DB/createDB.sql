-- Creating the BD toy share
CREATE DATABASE toy_share
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'English_United States.1252'
       LC_CTYPE = 'English_United States.1252'
       CONNECTION LIMIT = -1;



CREATE SCHEMA public
  AUTHORIZATION postgres;

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
COMMENT ON SCHEMA public
 IS 'standard public schema';

-- creating tables parents, toy and toy_parents
 

CREATE TABLE public.parents
(
  id integer NOT NULL DEFAULT nextval('parents_id_seq'::regclass),
  name character(150),
  city character(150),
  id_toy integer,
  rate integer,
  CONSTRAINT "PK_parent" PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);


CREATE TABLE public.toy
(
  id integer NOT NULL DEFAULT nextval('toy_id_seq'::regclass),
  name character(150),
  category character(100),
  age character(100),
  picture character(250),
  CONSTRAINT "PK_toy" PRIMARY KEY (id)
)


CREATE TABLE public.toy_parent
(
  id integer NOT NULL DEFAULT nextval('toy_parent_id_seq'::regclass),
  id_toy integer,
  id_parent integer,
  CONSTRAINT "PK_toy_parent" PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
