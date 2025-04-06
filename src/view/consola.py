import sys
sys.path.append("src")
from model import logic
#Variables
monto_inicial = int(input("Ingrese el monto inicial con la que deseas iniciar el ahorro: "))
aporte_periodico = int(input("Ingresee el valor del aporte por periodos que quiere hacer en el ahorro: "))
n_periodos = int(input("Ingresee el tiempo en meses de periodos que desea para hacer el ahorro: "))
tasa_interes = float(input("Ingrese la tasa de intereses que desea pagar en su ahorro: ")) / 100

# Acá es donde se llaman la función de logica para hacer el calculo e imprimirlo en pantalla, el round es para redondear el resultado
try:
    ahorro = logic.calcular_monto(monto_inicial,tasa_interes,n_periodos,aporte_periodico)
    print(f"El ahorro final es: {round(ahorro)}")


#Este es para cuando haga un caso de error imprima el error y el tipo de error
except Exception as err:
    print(f"No se pudo hacer el calculo algo fallo {err}") 

