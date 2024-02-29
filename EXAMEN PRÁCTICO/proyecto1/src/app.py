from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/', methods=['GET'])
def index2():
    nombre = request.args.get('nombre', '')
    apellido = request.args.get('apellido', '')
    return render_template('index.html', nombre=nombre, apellido=apellido)

@app.route('/', methods=['POST'])
def index():
    correo = request.form['email']
    password = request.form['password']
    return render_template('index.html',correo=correo,password=password)

@app.route('/personales.html')
def personales():
    return render_template('personales.html')

@app.route('/mater.html')
def mater():
    return render_template('mater.html')

@app.route('/hobby.html')
def hobby():
    return render_template('hobby.html')

@app.route('/habilidades.html')
def habilidades():
    return render_template('habilidades.html')



@app.route('/login')
def login():
    
    return render_template('login.html')
   
    

app.run(debug=True)