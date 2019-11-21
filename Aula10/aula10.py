# Aula 10 - 20-11-2019
# 
#--- Web - Calculadora
nome_pagina = 'Calculadora'#é o que fica na aba do seu navegador,pra enviar ela pro html tem que dar um nome para ela no render_template
from flask import Flask, render_template, request
from calculo_metodo import *

app = Flask (__name__)


@app.route('/')
def home():
    return render_template('home.html', titulo=nome_pagina)

@app.route('/calcular')
def calcular():
    n1 = int(request.args['numero1'])
    n2 = int(request.args['numero2'])
    r_soma = soma(n1,n2)
    r_subtracao = subtracao(n1,n2)
    r_multiplicacao = multiplicacao(n1,n2)
    r_divisaointeira = divisaointeira(n1,n2)
    r_divisaofracionada = divisaofracionada(n1,n2)
    r_resto = resto(n1,n2)
    r_raiz = raiz(n1,n2)
    resultados = {'soma':r_soma
    ,'subtracao':r_subtracao
    ,'multiplicacao':r_multiplicacao
    ,'divisaointeira':r_divisaointeira
    ,'divisaofracionada':r_divisaofracionada
    ,'resto':r_resto,'raiz':r_raiz}

    return render_template('resultado.html', resultados = resultados)

app.run()