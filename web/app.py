from flask_serialize import FlaskSerialize

# create a flask-serialize mixin instance from
# the factory method `FlaskSerialize`
fs_mixin = FlaskSerialize(db)

class Item(db.Model, fs_mixin):
    id = db.Column(db.Integer, primary_key=True)
    # other fields ...