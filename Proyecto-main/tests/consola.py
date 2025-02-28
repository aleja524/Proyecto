import logica

monto_inicial = int(input("Ingrese el monto inicial con la que deseas iniciar el ahorro: "))
aporte_periodico = int(input("Ingresee el valor del aporte por periodos que quiere hacer en el ahorro: "))
n_periodos = int(input("Ingresee el tiempo en meses de periodos que desea para hacer el ahorro: "))
tasa_interes = float(input("Ingrese la tasa de intereses que desea pagar en su ahorro: ")) / 100

try:
    ahorro = logica.calcular_monto(monto_inicial,tasa_interes,n_periodos,aporte_periodico)
    print(f"El ahorro final es: {round(ahorro)}")

except Exception as err:
    print(f"No se pudo hacer el calculo algo fallo {err}")

