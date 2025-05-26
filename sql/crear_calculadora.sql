CREATE TABLE calculadora_ahorro (
    id_calculo SERIAL PRIMARY KEY,
    id_usuario INTEGER NOT NULL,
    monto_mensual REAL NOT NULL,
    meses INTEGER NOT NULL,
    tasa_interes REAL DEFAULT 0,
    total_ahorrado REAL NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
