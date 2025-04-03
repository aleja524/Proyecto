import sys
sys.path.append("src")
from model.logic import *
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class Calculadora_de_ahorro(App):
    def build(self):
        contenedor = GridLayout(cols = 2)

        boton_para_calcular = Button()
        self.monto_inicial = TextInput()
        self.tasa_de_interes = TextInput()
        self.numero_de_periodos = TextInput() 
        self.aporte_periodico = TextInput()

        contenedor.add_widget(Label(text = "ingresa monto inicial"))
        contenedor.add_widget(self.monto_inicial)

        contenedor.add_widget(Label(text = "ingresa tasa de interes"))
        contenedor.add_widget(self.tasa_de_interes)

        contenedor.add_widget(Label(text = "ingrese el numero de periodos en los que desea pagar"))
        contenedor.add_widget(self.numero_de_periodos)

        contenedor.add_widget(Label(text = "ingres el aporte periodico"))
        contenedor.add_widget(self.aporte_periodico)

        self.label_del_valor = Label(text="Aqui aparecera el calculo de tu ahorro")
        contenedor.add_widget(self.label_del_valor)
        contenedor.add_widget(boton_para_calcular)

        boton_para_calcular.bind(on_press=self.calcular_ahorro)

        return contenedor
    
    def calcular_ahorro(self, sender):
        monto_inicial, tasa_de_interes, numero_de_periodos, aporte_periodico = float(self.monto_inicial.text), float(self.tasa_de_interes.text), float(self.numero_de_periodos.text), float(self.aporte_periodico.text)
        calcular = calcular_monto(monto_inicial, tasa_de_interes, numero_de_periodos, aporte_periodico)
        resultado = round(calcular,2)
        format_number = f"{resultado: 2f}"
        self.label_del_valor.text = str(format_number)

if __name__ == "__main__":
    Calculadora_de_ahorro().run()
