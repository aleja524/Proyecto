
# Calculadora de Ahorro Programado

## ¿Qué es y para qué es?

La **Calculadora de Ahorro Programado** es una aplicación diseñada para ayudar a los usuarios a planificar sus ahorros de forma eficiente. Permite calcular el monto total ahorrado durante un período determinado, considerando aportes periódicos y una posible tasa de interés.

Además, cuenta con manejo de usuarios, controladores y conexión a base de datos en la nube mediante [Neon.tech](https://neon.tech/).

---

## ¿Cómo lo hago funcionar?

### Prerrequisitos

Antes de ejecutar este proyecto, asegúrate de tener instalado:

- Python 3.x
- Las bibliotecas necesarias (instalables con pip):

```bash
pip install -r requirements.txt


Para ejecutar las pruebas unitarias:  
```sh
py tests/casos.py
```

---

## **¿Cómo está hecho?**  

### **Arquitectura del Proyecto**  
El código está organizado en las siguientes carpetas:  

📂 **`src/`** (Código fuente)  
- 📂 `model/` → Contiene la lógica de la aplicación.  
  - `logic.py`: Funciones principales para el cálculo del ahorro.  
  - `more_logic.py`: Funciones adicionales de procesamiento.  
  - `other_logic.py`: Módulos auxiliares.  
  - `__init__.py`: Permite que Python reconozca `model` como un paquete.  
- 📂 `view/` → Interfaz en consola.  
  - `consola.py`: Punto de entrada para la interacción con el usuario.  

📂 **`tests/`** (Pruebas Unitarias)  
- `casos.py`: Contiene pruebas unitarias para verificar la lógica de cálculo.  
- `libro_casos_prueba_ahorro_con_formula...`: Archivo con casos de prueba.  

---

### **Dependencias y Organización de Módulos**  

En el código, los módulos se importan de la siguiente manera:  

- Desde `view/consola.py`, para usar funciones de `model`:
  ```python
  from model.logic import alguna_funcion
  ```
- Desde `tests/casos.py`, para probar funciones de `logic.py`, primero se añade el directorio `src` a la ruta:
  ```python
  import sys
  import os
  sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

  from model.logic import alguna_funcion
  ```

Esto permite que los módulos se importen correctamente sin importar desde dónde se ejecute el código.  

---

## **Uso**  

Para ejecutar las pruebas unitarias, desde la carpeta raíz, usa:  
```sh
py tests/casos.py
```
## **¿Quién hizo esto?**  
Este proyecto fue desarrollado por **Andrés Gallego y Kevin Silva**. 

  


