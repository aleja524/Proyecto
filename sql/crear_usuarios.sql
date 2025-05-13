CREATE TABLE usuarios (
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    documento_identidad integer primary key,
    correo TEXT NOT NULL,
    telefono BIGINT NOT NULL
);