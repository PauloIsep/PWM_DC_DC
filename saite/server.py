from flask import Flask , render_template , request
 #render template serve para ir buscar os files HTML.

from forms import values

pwm= Flask(__name__)
pwm.config['SECRET_KEY']='PMfr.k33L.'

@pwm.route("/") 
def homepage():
    return render_template('homepage.html') 

@pwm.route("/querry" , methods=["GET" , "POST"])
def querry():
    form = values()
    if form.is_submitted():
        result = request.form #colocar proteçao para ver se ta
        return render_template('display_data.html' , result=result)
    return render_template('initial_querry.html' , form=form) 



@pwm.route("/<type_of_converter>")
def user(type_of_converter):
    return type_of_converter



#site no ar
if __name__ == "__main__": #e importante para o deploy do site
    pwm.run(debug=True) #activa o debuig ou seja tudo o que editar ele exibe no site


