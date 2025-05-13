CREATE TABLE IF NOT EXISTS usuarios (
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    documento_identidad BIGINT PRIMARY KEY,
    correo TEXT NOT NULL,
    telefono BIGINT NOT NULL
);