from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("CURRICULUM.html")
@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form.get("Nombre y Apellido")
    fecha= request.form.get("fecha")
    ocupacion = request.form.get("Ocupacion")
    contacto = request.form.get("Contacto")
    nacion = request.form.get("nacion")
    Basico= request.form.get("Basico")
    Intermedio= request.form.get("Intermedio")
    Avanzado= request.form.get("Avanzado")
    Fluido= request.form.get("Fluido")
    lenguajes= request.form.get("lenguajes")
    habilidad1= request.form.get("habilidad1")
    habilidad2= request.form.get("habilidad2")
    perfil= request.form.get("perfil")
    return render_template("mostrar.html", nombre=nombre, ocupacion=ocupacion, contacto=contacto,Basico=Basico,Intermedio=Intermedio,Avanzado=Avanzado,Fluido=Fluido
     ,habilidad1=habilidad1, habilidad2=habilidad2,fecha=fecha,lenguajes=lenguajes,nacion=nacion,perfil=perfil)


   
app.run(debug=True,port=5000)



