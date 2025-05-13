CREATE TABLE IF NOT EXISTS detalles_ahorro (
    id SERIAL PRIMARY KEY,
    ahorro_id INTEGER NOT NULL,
    mes INTEGER NOT NULL,
    monto_acumulado REAL NOT NULL,
    FOREIGN KEY (ahorro_id) REFERENCES calculadora_ahorro(id_usuario)
);
