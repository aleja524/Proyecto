# 💰 Calculadora de Ahorro Programado

## 📌 ¿Qué es y para qué sirve?

La **Calculadora de Ahorro Programado** es una aplicación desarrollada para ayudar a los usuarios a planificar sus ahorros de forma eficiente. Permite calcular el monto total ahorrado durante un período determinado, considerando:

- Aportes periódicos.
- Tasa de interés opcional.
- Tiempo de ahorro.

Además, incluye:

- Gestión de usuarios.
- Conexión con base de datos en la nube mediante [Neon.tech](https://neon.tech).
- Interfaces gráfica (GUI) y de consola.
- Pruebas unitarias.

---

## ⚙️ ¿Cómo lo hago funcionar?

### 🧾 Prerrequisitos

- Python 3.x
- PostgreSQL (se recomienda usar [Neon.tech](https://neon.tech) para facilitar el despliegue en la nube)
- Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

### 🏗️ Crear la base de datos

**NOTA:** se debe tener en cuenta que se debe conectar su propia base de datos en blanco para que se ejecute de manera eficiente.

1. Crear una cuenta en [Neon.tech](https://neon.tech) o usar tu servicio de PostgreSQL local.
2. Crear una base de datos y obtener los siguientes datos:
   - Nombre del host
   - Usuario
   - Contraseña
   - Nombre de la base de datos
   - Puerto

3. Ejecutar los scripts SQL ubicados en la carpeta `sql/`:
   - `crear_usuarios.sql`
   - `crear_calculadora.sql`
---

### 🔐 Configurar `.env`

El archivo `.env` debe contener las credenciales necesarias para conectarse a la base de datos. Este archivo no incluye datos privados y debe ser completado por el usuario.

**Ejemplo de `secret_config.py`:**

```python
DB_HOST=Host de la base de datos
DB_NAME=nombre_de_base_de_datos
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
```

> 🔒 *No subas este archivo a GitHub con tus datos reales. ignóralo con `.gitignore`.*

---

### ▶️ Ejecutar el programa

Desde la raíz del proyecto:

```bash
# Ejecutar pruebas unitarias
py tests/casos.py
py tests/test.py

# Interfaz en consola
py src/view/console/consola.py

# Interfaz gráfica (Tkinter)
py src/view/gui/interfaz.py
```

---

## 🧠 Estructura del Proyecto

```
📦 root/
├── sql/                → Scripts SQL
│
├── src/
│   ├── controller/     → Controladores
│   ├── model/          → Clases lógicas
│   ├── view/
│   │   ├── console/    → Interfaz de consola
│   │   └── gui/        → Interfaz gráfica
│
├── tests/              → Pruebas unitarias
├── secret_config.py    → Archivo de configuración (NO contiene datos privados)
```

---

## 👨‍💻 Autores

- **Andrés Gallego**
- **Kevin Silva**


