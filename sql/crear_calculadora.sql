CREATE TABLE calculadora_ahorro (
id INTEGER PRIMARY KEY AUTOINCREMENT,
    id usuario INTEGER NOT NULL,
    monto mensual REAL NOT NULL,
    meses INTEGER NOT NULL,
    tasa interes REAL DEFAULT 0,
    total ahorrado REAL NOT NULL,
    fecha creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);


CREATE TABLE IF NOT EXISTS detalles_ahorro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id ahorro  INTEGER NOT NULL,
    mes INTEGER NOT NULL,
    monto acumulado REAL NOT NULL,
    FOREIGN KEY (ahorro_id) REFERENCES ahorros(id)
);
