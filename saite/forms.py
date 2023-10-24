from flask_wtf import FlaskForm
from wtforms import IntegerField ,SubmitField

class values(FlaskForm):
    frequency =IntegerField('frequency')
    duty_cycle =IntegerField('duty_cycle')
    submit_1 =SubmitField('GIBE')

#posso acresentar aqui os restantes valores