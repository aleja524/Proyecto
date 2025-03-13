# Calculadora de Ahorro Programado 

## ¿Quién hizo esto?
Este proyecto fue desarrollado por:
- **Andrés Gallego**
- **Kevin Silva**

## ¿Qué es y para qué es?
La **Calculadora de Ahorro Programado** es una aplicación diseñada para ayudar a los usuarios a planificar sus ahorros de manera eficiente. Permite calcular el monto total ahorrado en un periodo determinado con base en aportes periódicos y una posible tasa de interés.

## ¿Cómo lo hago funcionar?
### Prerrequisitos
Antes de ejecutar la aplicación, asegúrese de tener instalado:
- **Python 3.8 o superior**
- Librerías necesarias (pueden instalarse con `pip`):
  ```sh
  pip install matplotlib numpy pandas
  ```

### Ejecución
Para ejecutar la aplicación, ubíquese en la carpeta raiz del proyecto y ejecute el siguiente comando:
```sh
py src\Console\AhorroCalculator.py
```

## ¿Cómo está hecho?
La aplicación está estructurada en diferentes módulos y capas para facilitar su mantenimiento y escalabilidad.

### Arquitectura
El proyecto sigue una arquitectura modular:
- **src**: Contiene el código fuente de la aplicación.
  - **models**: Define las clases y estructuras de datos.
  - **services**: Implementa la lógica de cálculo del ahorro.
  - **ui**: Interfaz de usuario (si aplica).
  - **Console**: Punto de entrada de la aplicación en consola.
- **tests**: Contiene las pruebas unitarias.
- **docs**: Documentación del proyecto.

### Dependencias
El proyecto usa las siguientes bibliotecas:
- **NumPy**: Para operaciones matemáticas y cálculos.
- **Pandas**: Para estructurar y manejar los datos.
- **Matplotlib**: Para generar gráficas del ahorro en el tiempo.

## Uso
### Ejecutar pruebas unitarias
Para ejecutar las pruebas unitarias, desde la carpeta raíz, ejecute:
```sh
py tests\AhorroTests.py
```
Para que las pruebas funcionen correctamente, asegúrese de incluir la siguiente línea al inicio del módulo de pruebas:
```python
import sys
sys.path.insert(0, "./src")
```

## Cálculo del Ahorro
### Entradas
El usuario debe ingresar:
- **Monto inicial**: Cantidad con la que se empieza el ahorro.
- **Aporte periódico**: Monto a ahorrar en cada periodo.
- **Frecuencia de ahorro**: Diario, semanal, quincenal o mensual.
- **Número de periodos**: Cantidad de periodos a ahorrar.
- **Tasa de interés anual** (opcional): Para calcular el crecimiento del ahorro.

### Proceso
- Se suma el aporte periódico en cada ciclo.
- Si se incluye una tasa de interés, se aplica la fórmula de interés compuesto o simple.
- Se genera una tabla de ahorro detallada y una gráfica de crecimiento.

### Fórmulas utilizadas
- **Sin interés**:
  ```
  A = P + (d × n)
  ```
- **Con interés compuesto**:
  ```
  A = P(1+r)^n + d × ((1+r)^n - 1) / r
  ```

### Salidas
- **Tabla de ahorro**: Detalle de los montos acumulados en cada periodo.
- **Monto total**: Total ahorrado al final del periodo.
- **Gráfica**: Representación visual del crecimiento del ahorro.

---
**Nota:** Para futuras versiones, se planea agregar una interfaz gráfica y soporte para diferentes monedas.


  


