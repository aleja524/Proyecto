CREATE TABLE calculadora_ahorro (
id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    monto_mensual REAL NOT NULL,
    meses INTEGER NOT NULL,
    tasa_interes REAL DEFAULT 0,
    total_ahorrado REAL NOT NULL,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);


CREATE TABLE IF NOT EXISTS detalles_ahorro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ahorro_id INTEGER NOT NULL,
    mes INTEGER NOT NULL,
    monto_acumulado REAL NOT NULL,
    FOREIGN KEY (ahorro_id) REFERENCES ahorros(id)
);
