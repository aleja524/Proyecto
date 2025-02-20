# casos_pruebas/casos.py
casos_de_prueba_normal = [
    (10_000_000, 0.01, 12, 500_000, 17_609_502),  # Caso 1 con ahorro intereses mensual 
    (20_000_000, 0.015, 24, 1_000_000, 57_223_577),  # Caso 2 con mayor tasa de interés
    (5_000_000, 0.01, 12, 250_000, 8_804_751),  # Caso 3 estándar
]

casos_de_prueba_extraordinario = [
    (1_000_000, 0.00, 12, 50_000, 1_600_000),  # Caso 1 sin intereses   
    (1_700_000, 0.01, 4, 80_000, 2_093_859),  # Caso 2 periodo corto
    (0, 0.01, 12, 1_000_000, 12_682_503),  # Caso 3 sin monto inicial
]
