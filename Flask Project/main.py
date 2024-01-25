from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros_pintura = int(request.form['tarros_pintura'])

        # Calcular descuento
        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        # Calcular total
        total_sin_descuento = tarros_pintura * 9000
        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template('resultado_ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        # Verificar usuario y contraseña
        if usuario == 'juan' and contraseña == 'admin':
            mensaje = 'Bienvenido administrador juan'
        elif usuario == 'pepe' and contraseña == 'user':
            mensaje = 'Bienvenido usuario pepe'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

        return render_template('resultado_ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
