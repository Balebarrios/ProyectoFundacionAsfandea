CREATE TABLE "profesional" (
  "run_profesional" <type>,
  "especialidad" <type>,
  "nombre" <type>,
  "apellido" <type>,
  "dirección" <type>,
  "telefono" <type>,
  "nacionalidad" <type>,
  "fecha_nacimiento" <type>,
  PRIMARY KEY ("run_profesional")
);

CREATE TABLE "persona_TEA" (
  "run_TEA" <type>,
  "grado_TEA" <type>,
  "nombre" <type>,
  "apellido" <type>,
  "dirección" <type>,
  "telefono" <type>,
  "nacionalidad" <type>,
  "fecha_nacimiento" <type>,
  PRIMARY KEY ("run_TEA")
);

CREATE TABLE "apoderado" (
  "run_apoderado" <type>,
  "run_TEA" <type>,
  "nombre" <type>,
  "apellido" <type>,
  "dirección" <type>,
  "telefono" <type>,
  "nacionalidad" <type>,
  "fecha_nacimiento" <type>,
  PRIMARY KEY ("run_apoderado")
);

