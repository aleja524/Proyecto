import logica

def main():
    print("\n--- Calculadora de Ahorro Programado ---\n")
    
    try:
        monto_inicial = float(input("Ingrese el monto inicial: "))
        aporte_periodico = float(input("Ingrese el aporte periódico: "))
        n_periodos = int(input("Ingrese el número de períodos: "))
        tasa_interes = float(input("Ingrese la tasa de interés anual (en %): ")) / 100
        
        if monto_inicial < 0 or aporte_periodico <= 0 or n_periodos <= 0:
            raise ValueError("Los valores ingresados deben ser positivos y el aporte periódico mayor a cero.")
        
        resultado = logica.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)
        
        print("\n--- Resultado ---")
        print(f"Monto total ahorrado después de {n_periodos} períodos: ${resultado:,.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    main()
