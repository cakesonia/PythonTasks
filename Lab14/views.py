from app import app
from flask import request
from app import db
from decoration import Decoration


@app.route('/')
def index():
    firstmember = Decoration.query.first()
    return '<h1> Here you can find decoration list! </h1>'


@app.route('/decoration')
def view():
    decoration = Decoration.query.first()
    if decoration is not None:
        return str('First member name \n' + decoration.__str__())
    else:
        return "Decoration with this id does not exist"


@app.route('/decoration/<id>')
def get_decoration(id):
    decoration = Decoration.query.get(id)
    if decoration is not None:
        return decoration.__str__()
    else:
        return "Decoration with this id does not exist"


@app.route('/decoration', methods=['POST'])
def add_decoration():
    decoration_id = request.json['id']
    type_of_decoration = request.json['type_of_decoration']
    decoration_place = request.json['decoration_place']
    color = request.json['color']

    new_decoration = Decoration()
    new_decoration.decoration_id = decoration_id
    new_decoration.decoration_type = type_of_decoration
    new_decoration.decoration_place = decoration_place
    new_decoration.decoration_color = color

    db.session.add(new_decoration)
    db.session.commit()

    return str(new_decoration.__str__())


@app.route('/decoration/<id>', methods=['PUT'])
def decoration_update(id):
    type_of_decoration = request.json['type_of_decoration']
    decoration_place = request.json['decoration_place']
    color = request.json['color']

    new_decoration = Decoration.query.get(id)
    new_decoration.device_id = id
    new_decoration.device_model = type_of_decoration
    new_decoration.device_producer = decoration_place
    new_decoration.device_power = color

    db.session.commit()

    return new_decoration.__str__()


@app.route('/decoration/<id>', methods=['DELETE'])
def decoration_delete(id):
    decoration = Decoration.query.get(id)
    db.session.delete(decoration)
    db.session.commit()

    return str("Deleting succssesful")
