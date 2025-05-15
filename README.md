
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


Desde la raíz del proyecto, puedes ejecutar:
  1.Interfaz en consola: py src/view/console/consola.py


  2.Interfaz gráfica (GUI):py src/view/gui/interfaz.py


  3.Pruebas unitarias: py tests/test.py



```

---

## **¿Cómo está hecho?**  

### **Arquitectura del Proyecto**  
El código está organizado en las siguientes carpetas:  

📂 sql/               → Scripts para crear y eliminar tablas (usuarios, calculadora) en la base de datos.
📂 src/
 ├── 📂 controller/   → Controladores de la lógica del sistema.
 │     ├── calculadora_controlador.py
 │     └── usuario_controlador.py
 ├── 📂 model/        → Lógica de negocio y clases principales.
 │     ├── calculadora.py
 │     ├── errores.py
 │     ├── logic.py
 │     └── usar.py
 ├── 📂 view/
 │     ├── 📂 console/ → Interfaz en consola.
 │     │     ├── consola.py
 │     │     └── consolacontrolador.py
 │     └── 📂 gui/     → Interfaz gráfica (Tkinter).
 │           └── interfaz.py
 └── __init__.py      → Indica que src es un paquete.
📂 tests/             → Pruebas unitarias del sistema.
 ├── test.py
 └── testdb.py

---


**Base de Datos (neon.tech)**
La aplicación se conecta a una base de datos PostgreSQL alojada en la nube mediante neon.tech.

Los scripts SQL necesarios para crear o eliminar tablas están en la carpeta sql/.

crear_calculadora.sql, crear_usuarios.sql

eliminar_calculadora.sql, eliminar_usuarios.sql

Las credenciales de conexión están configuradas en SecretConfig.py (NO compartas este archivo públicamente).

El proyecto se conecta automáticamente a la base de datos mediante las funciones definidas en los controladores.


### **Dependencias y Organización de Módulos**  

Desde consola.py, para usar funciones de la lógica: from model.logic import alguna_funcion

Desde tests/test.py, para importar desde src: import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from model.logic import alguna_funcion

Uso
Ejecuta la calculadora desde consola o interfaz gráfica.

Registra usuarios y realiza operaciones de ahorro.

Las transacciones y datos quedan guardados en la base de datos en la nube.

¿Quién hizo esto?
Este proyecto fue desarrollado por Andrés Gallego y Kevin Silva.
 
  
 

