from mimetypes import init
from flask import Flask, flash, redirect, url_for, session
import sys
from functools import wraps
import psycopg2 

sys.path.append('src')


from flask import render_template, request
import model.logic as logic
from model.usuar import Usuario
from model.calculadora import CalculadoraAhorro 
from controller.calculadora_controlador import ControladorCalculadora
from controller.usuario_controlador import ControladorUsuarios

app = Flask(__name__)
app.secret_key = 'kCifuentes829' 

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Debes iniciar sesión para acceder a esta página.', 'error')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.before_first_request
def create_tables():
    try:
        ControladorUsuarios.CrearTabla()
        ControladorCalculadora.CrearTabla()
        print("Tablas verificadas/creadas exitosamente.")
    except Exception as e:
        print(f"Error al crear tablas: {e}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        try:
            documento_identidad = int(request.form['documento_identidad'])
            telefono = int(request.form['telefono'])
        except ValueError:
            flash('Documento y teléfono deben ser números.', 'error')
            return render_template('registrar.html')
            
        correo = request.form['correo']

        # Verificar si el usuario ya existe
        if ControladorUsuarios.BuscarUsuarioPorDocumento(documento_identidad):
            flash('El documento de identidad ya está registrado.', 'error')
        else:
            nuevo_usuario = Usuario(nombre, apellido, documento_identidad, correo, telefono)
            ControladorUsuarios.InsertarUsuario(nuevo_usuario)
            flash('Usuario registrado exitosamente. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
        
    return render_template('registrar.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            documento_identidad = int(request.form['documento_identidad'])
        except ValueError:
            flash('Documento debe ser un número.', 'error')
            return render_template('login.html')

        usuario = ControladorUsuarios.BuscarUsuarioPorDocumento(documento_identidad)
        if usuario:
            session['user_id'] = usuario.documento_identidad
            session['user_nombre'] = usuario.nombre
            flash('Inicio de sesión exitoso.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash('Documento de identidad no encontrado.', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('user_id', None)
    session.pop('user_nombre', None)
    flash('Has cerrado sesión.', 'success')
    return redirect(url_for('index'))


@app.route('/calculadora', methods=['GET', 'POST'])
@login_required
def calculadora():
    if request.method == 'POST':
        try:
            monto_inicial    = float(request.form['monto_inicial'])
            aporte_periodico = float(request.form['aporte_periodico'])
            n_periodos       = int(request.form['n_periodos'])
            tasa_interes     = float(request.form['tasa_interes']) / 100
        except ValueError:
            flash('Por favor, ingresa valores numéricos válidos.', 'error')
            return render_template('calculadora.html', result=None)

        try:
            total_ahorrado   = logic.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)
            result           = round(total_ahorrado, 2)

            id_usuario_actual = session.get('user_id')
            if id_usuario_actual:
                # id_calculo será SERIAL en la BD
                calculo_guardar = CalculadoraAhorro(
                    None,
                    id_usuario_actual,
                    aporte_periodico,
                    n_periodos,
                    tasa_interes,
                    result
                )
                try:
                    ControladorCalculadora.InsertarCalculadora(calculo_guardar)
                    flash('Cálculo guardado exitosamente.', 'success')
                except psycopg2.errors.UniqueViolation:
                    flash('Ya tienes un cálculo guardado. Para guardar uno nuevo, elimina el anterior o esta funcionalidad necesita ser actualizada para múltiples ahorros.', 'error')
                except Exception as e:
                    flash(f'Error al guardar el cálculo: {e}', 'error')
            
            return render_template('calculadora.html', result=result)

        except logic.monto_inicial_negativo as e:
            flash(str(e), 'error')
        except logic.aporte_periodico_menor_a_cero as e:
            flash(str(e), 'error')
        except logic.aporte_periodico_mayor_a_60 as e:
            flash(str(e), 'error')
        except logic.tasa_interes_negativa as e:
            flash(str(e), 'error')
        except Exception as e:
            flash(f"Ocurrió un error inesperado durante el cálculo: {e}", 'error')
        
        return render_template('calculadora.html', result=None)

    return render_template('calculadora.html')

@app.route('/consultar', methods=['GET'])
@login_required
def consultar():
    documento_buscado = request.args.get('documento')
    registros = []
    id_usuario_actual = session.get('user_id')

    if documento_buscado:
        try:
            id_usuario_buscado = int(documento_buscado)
            if id_usuario_buscado != id_usuario_actual:
                flash("Solo puedes buscar tus propios registros.", "error")
            else:
                registros = ControladorCalculadora.BuscarCalculadoraPorUsuario(id_usuario_buscado)
        except ValueError:
            flash("Documento de búsqueda inválido.", "error")
    elif id_usuario_actual:
        registros = ControladorCalculadora.BuscarCalculadoraPorUsuario(id_usuario_actual)
    
    return render_template('consultar.html', registros=registros)

if __name__ == "__main__":
    app.run(debug=True)