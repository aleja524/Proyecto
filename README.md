Calculadora de Ahorro Programado
¿Qué es y para qué sirve?
La Calculadora de Ahorro Programado es una aplicación desarrollada para ayudar a los usuarios a planificar sus ahorros de forma eficiente. Permite calcular el monto total ahorrado durante un período determinado, considerando:

Aportes periódicos.

Tasa de interés opcional.

Tiempo de ahorro.

Además, incluye:

Gestión de usuarios.

Conexión con base de datos en la nube mediante Neon.tech.

Interfaces gráfica (GUI) y de consola.

Pruebas unitarias.

⚙️ ¿Cómo lo hago funcionar?
🧾 Prerrequisitos
Python 3.x

Dependencias del proyecto:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecución del proyecto
Desde la raíz del proyecto:

bash
Copiar
Editar
# Ejecutar pruebas unitarias
py tests/casos.py
py tests/test.py

# Interfaz en consola
py src/view/console/consola.py

# Interfaz gráfica (Tkinter)
py src/view/gui/interfaz.py

¿Cómo está hecho?
📁 Arquitectura del Proyecto
pgsql
Copiar
Editar
📦 root/
├── sql/                → Scripts SQL para crear/eliminar tablas.
│   ├── crear_calculadora.sql
│   ├── crear_usuarios.sql
│   ├── eliminar_calculadora.sql
│   └── eliminar_usuarios.sql
│
├── src/
│   ├── controller/     → Lógica del sistema
│   │   ├── calculadora_controlador.py
│   │   └── usuario_controlador.py
│   │
│   ├── model/          → Clases y lógica principal
│   │   ├── calculadora.py
│   │   ├── errores.py
│   │   └── logic.py
│   │
│   ├── view/
│   │   ├── console/    → Interfaz de consola
│   │   │   ├── consola.py
│   │   │   └── consolacontrolador.py
│   │   └── gui/        → Interfaz gráfica (Tkinter)
│   │       ├── interfaz.py
│   │       └── __init__.py
│
├── tests/              → Pruebas unitarias
│   ├── test.py
│   └── testdb.py
🛢️ Base de Datos (PostgreSQL - Neon.tech)
El proyecto utiliza PostgreSQL en la nube para almacenar usuarios y registros.

Credenciales configuradas en SecretConfig.py (no compartir públicamente).

La conexión y gestión de datos se realiza mediante los controladores definidos.

🔁 Dependencias y organización de módulos
Desde consola.py:

python
Copiar
Editar
from model.logic import alguna_funcion
Desde tests/test.py:

python
Copiar
Editar
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from model.logic import alguna_funcion
👨‍💻 Autores
Este proyecto fue desarrollado por:

Andrés Gallego

Kevin Silva

