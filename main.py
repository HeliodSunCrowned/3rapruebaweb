from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None
    nota1 = ''
    nota2 = ''
    nota3 = ''
    asistencia = ''

    if request.method == 'POST':
        nota1 = request.form.get('nota1', '')
        nota2 = request.form.get('nota2', '')
        nota3 = request.form.get('nota3', '')
        asistencia = request.form.get('asistencia', '')

        try:
            n1 = float(nota1)
            n2 = float(nota2)
            n3 = float(nota3)
            asist = float(asistencia)

            promedio = round((n1 + n2 + n3) / 3, 1)

            if promedio >= 40 and asist >= 75:
                estado = 'APROBADO'
            else:
                estado = 'REPROBADO'
        except ValueError:
            estado = 'ERROR: Ingrese valores numéricos válidos'

    return render_template(
        'ejercicio1.html',
        promedio=promedio,
        estado=estado,
        nota1=nota1,
        nota2=nota2,
        nota3=nota3,
        asistencia=asistencia
    )


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mayor = None
    cantidad_caracteres = None
    nombre1 = ''
    nombre2 = ''
    nombre3 = ''

    if request.method == 'POST':
        nombre1 = request.form.get('nombre1', '').strip()
        nombre2 = request.form.get('nombre2', '').strip()
        nombre3 = request.form.get('nombre3', '').strip()

        nombres = [nombre1, nombre2, nombre3]
        nombre_mayor = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mayor)

    return render_template(
        'ejercicio2.html',
        nombre_mayor=nombre_mayor,
        cantidad_caracteres=cantidad_caracteres,
        nombre1=nombre1,
        nombre2=nombre2,
        nombre3=nombre3
    )


if __name__ == '__main__':
    app.run(debug=True)
