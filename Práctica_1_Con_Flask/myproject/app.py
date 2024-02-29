from flask import Flask, render_template #Es para importar flask

app = Flask(__name__) #creamos una instancia de flask en una variable llamada app(se puede llamar como sea)

@app.route('/')#usamos un decorador(@) para crear una respuesta a la ruta / que es el index o página principal
def Hola(): #creamos la función que va a responder al llamado a  la ruta /
    return '<h1>Hola mundo</h1>' #es lo que devuelve la función es este caso solo un texto (hola mundo)
@app.route('/plantilla')
def plantilla():
    data={
        'Title':'Práctica #1',
        'Message':'Bienvenido al sitio Web (Fernando José Canto Cetina)'
    } #Declaración de diccionario
    return render_template('index.html',data=data) #render_template es para renderizar la plantilla
app.run(debug=True) #es para correr la aplicación o sea nuestro sitio web en el servidor virtual
    
    