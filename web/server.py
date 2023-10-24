from flask import Flask , render_template , request , json
from flask_serialize import FlaskSerialize
 #render template serve para ir buscar os files HTML.
from forms import values
import json
#out_file = open("parameters.json" , "w")
pwm= Flask(__name__)
pwm.config['SECRET_KEY']='PMfr.k33L.'

dictionary={
    "frequecia" : 0,
    "duty_cylce": 0,
}

with open ("parameters.json" , "w") as outfile:
    json.dump(dictionary , outfile)

@pwm.route("/") 
def homepage():
    return render_template('homepage.html') 

@pwm.route("/querry" , methods=["GET" , "POST"])
def querry():
    form = values()
    if form.is_submitted():
        result = request.form #colocar proteçao para ver se ta
        parameters={
            "frequecia": request.form.get('frequency'),
            "duty_cycle":request.form.get('duty_cycle'),
        }
        with open ("parameters.json" , "w") as outfile:
            json.dump(parameters , outfile)
        return render_template('display_data.html' , result=result)
    return render_template('initial_querry.html' , form=form) 

@pwm.route("/<type_of_converter>")
def user(type_of_converter):
    return type_of_converter



#site no ar
if __name__ == "__main__": #e importante para o deploy do site
    pwm.run(debug=True) #activa o debuig ou seja tudo o que editar ele exibe no site


