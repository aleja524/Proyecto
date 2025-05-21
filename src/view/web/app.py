from mimetypes import init
from flask import Flask
import sys

sys.path.append('src')

from flask import render_template, request
import model.logic as logic
from controller.calculadora_controlador import ControladorCalculadora

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    if request.method == 'POST':
        monto_inicial    = float(request.form['monto_inicial'])
        aporte_periodico = float(request.form['aporte_periodico'])
        n_periodos       = int(request.form['n_periodos'])
        tasa_interes     = float(request.form['tasa_interes']) / 100
        ahorro           = logic.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)
        result           = round(ahorro, 2)
        return render_template('calculadora.html', result=result)
    return render_template('calculadora.html')

@app.route('/consultar')
def consultar():
    registros = ControladorCalculadora.ListarTodos()
    return render_template('consultar.html', registros=registros)

if __name__ == "__main__":
    app.run(debug=True)